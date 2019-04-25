import json
import requests
from pprint import pprint
import scipy.stats as ss
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import random
import nltk
from textblob import TextBlob
from watson_developer_cloud import ToneAnalyzerV3
from watson_developer_cloud import WatsonApiException
import json
from nltk.tokenize import TweetTokenizer
import numpy as np 
from twilio.rest import Client
import sys, fileinput

tknzr = TweetTokenizer(strip_handles=True, reduce_len=True)

# Input: file name
# Output: read into python
def read_json(file):

	with open(file) as f:
		data = json.load(f)

	return data


# Input: data dictionary, new date
# Output: suggested video, time and cloth 
def suggestion_today(data_dict, today):

	video_list = []
	cloth_list = []
	time_len = range(120)

	for key in data_dict["date"].keys():
		video_list.append(data_dict["date"][key][0]["video"])
		cloth_list.append(data_dict["date"][key][0]["dress"])

	if today not in data_dict["date"].keys():
		today_video = random.choice(video_list)
		today_time = random.choice(time_len)
		today_cloth = random.choice(cloth_list)
	else:
		pass
	
	return today_video, today_time, today_cloth

# Input: suggested video, time and cloth, firebase url, today, old json file
# Output:  
def new_replace_old(url, old_dict, day, v_time, v_type, cloth, today_diary):

	delete_old = requests.delete(url)   # delete old version json

	new_json_data = old_dict

	if day not in new_json_data["date"].keys():

		new_json_data["date"].update({day: [{"video": v_type, "time": v_time, "dress": cloth, "diary": today_diary}]})
	
	response = requests.put(url, data = json.dumps(new_json_data))
	
	return new_json_data

# sentiment analysis
# Input: today's diary
# Output: tone list
def tone_analysis(dictionary, today):

	diary = dictionary["date"][today][0]["diary"]
	tone_analyzer = ToneAnalyzerV3(
						version='2017-09-21',
						iam_apikey = 'EWXcYvK8jEhxlasD-ptCuuVRGJq3xcSUeqWYYRaZYQ2G',
						url='https://gateway.watsonplatform.net/tone-analyzer/api')

	tone_analysis = tone_analyzer.tone({'text': diary}, 'application/json').get_result()
	
	tone_list = []
	score = []
	for each_sentence in tone_analysis["document_tone"]["tones"]:
		
		tone_list.append(each_sentence["tone_id"])
		score.append(each_sentence["score"])

	order_tone = []
	for mood in tone_list:
		count = tone_list.count(mood)
		order_tone.append(count)
	index = order_tone.index(max(order_tone))

	dominant_mood = tone_list[index]


	new_score = []
	subjectivity = []
	red_flag = ["kill","hurt","cut","hate","worst","horrible","awful","repulsive",
				"loathsome","obnoxious","disgusting","pesky","sad","crying","depressed",
				"anxious","scared","afraid","lethal","die","harm","pointless","fatal","injure",
				"violent","toxic","murder","suicidal"]

	red = 0
	for sentence in diary.split():
		blob = TextBlob(sentence)
		new_score.append(blob.sentiment[0])
		subjectivity.append(blob.sentiment[1])
		sentence = tknzr.tokenize(sentence)
		for word in sentence:
			if word in red_flag:
				red = red + 1
	# get average score in range [-1.0, 1.0]
	new_score = np.array(new_score)
	subjectivity = np.array(subjectivity)
	mean_score = np.mean(new_score)+ red*(-0.2)
	mean_subjectivity = np.mean(subjectivity) 

	return dominant_mood, mean_score

# if you are "negative" and the score in high, send a message
# Your Account SID from twilio.com/console
account_sid = "ACc14997ab59b5e9fe9182fc777e010211"
# Your Auth Token from twilio.com/console
auth_token  = "e92b8104780a706f2ee8d1cd89daa379"
def send_message(dominant_mood, score):
	client = Client(account_sid, auth_token)
	message = client.messages.create(
		to="+16086987679",
		from_="+16085355091",
		body="Hello from Beauty and Best!")

	print(message.sid)
	if dominant_mood in ["sadness", "angry", "fear"] and score < float(-0.6):
        
		message = client.messages.create(
			to="+16086987679",
			from_="+16085355091",
			body="Hello from Beauty and Best! Your friend, Erica, is in need of your friendship and support right now!")

		print(message.sid)



if __name__ == "__main__":
	data = read_json("easy_json.json")
	using_data = data
	today = sys.argv[1]
	today_video, today_time, today_cloth = suggestion_today(using_data, today)
	url = "https://project-2a5c4.firebaseio.com/bb.json"
	
	response = requests.put(url, data = json.dumps(using_data))

	today_diary = sys.argv[2]
	updated_data = new_replace_old(url, using_data, today, today_video, today_time, today_cloth, today_diary)
	dominant_mood, mean_score = tone_analysis(updated_data, today)
	send_message(dominant_mood, mean_score)
