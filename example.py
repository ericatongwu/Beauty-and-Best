import requests
import random
from textblob import TextBlob
from watson_developer_cloud import ToneAnalyzerV3
from watson_developer_cloud import WatsonApiException
import json
from nltk.tokenize import TweetTokenizer
import numpy as np
from twilio.rest import Client

tknzr = TweetTokenizer(strip_handles=True, reduce_len=True)

class Example:
	def __init__(self):
		self.data = self.read_json("easy_json.json")
		self.url = "https://project-2a5c4.firebaseio.com/bb.json"
		self.upload_data()
		self.account_sid = "ACc14997ab59b5e9fe9182fc777e010211"
		self.auth_token = "e92b8104780a706f2ee8d1cd89daa379"

	def get_online_json(self):

		response = requests.get(self.url)
		new_json_dic = response.json()

		return new_json_dic
	# Input: file name
	# Output: read into python
	def read_json(self, file):

		with open(file) as f:
			data = json.load(f)

		return data

	def get_suggestions_today(self, dictionary, today):
		video_list = []
		cloth_list = []
		time_len = range(120)

		for key in dictionary["date"].keys():
			video_list.append(dictionary["date"][key][0]["video"])
			cloth_list.append(dictionary["date"][key][0]["dress"])

		if today not in dictionary["date"].keys():
			today_video = random.choice(video_list)
			today_time = random.choice(time_len)
			today_cloth = random.choice(cloth_list)
		else:
			pass

		return today_video, today_time, today_cloth

	def upload_data(self):
		response = requests.put(self.url, data=json.dumps(self.data))

	def new_replace_old(self, new_json_dic, day, v_time, v_type, cloth, today_diary):

		delete_old = requests.delete(self.url)   # delete old version json

		if day not in new_json_dic["date"].keys():
			new_json_dic["date"].update({day: [{"video": v_type, "time": v_time, "dress": cloth, "diary": today_diary}]})

		response = requests.put(self.url, data=json.dumps(new_json_dic))

		return new_json_dic

	def tone_analysis(self, new_json_data, today):

		diary = new_json_data["date"][today][0]["diary"]
		tone_analyzer = ToneAnalyzerV3(
			version='2017-09-21',
			iam_apikey='EWXcYvK8jEhxlasD-ptCuuVRGJq3xcSUeqWYYRaZYQ2G',
			url='https://gateway.watsonplatform.net/tone-analyzer/api')

		tone_analysis = tone_analyzer.tone({'text': diary}, 'application/json').get_result()

		tone_list = []
		score = []
		for each_sentence in tone_analysis["document_tone"]["tones"]:
			tone_list.append(each_sentence["tone_id"])
			score.append(each_sentence["score"])
		# print(tone_list)
		order_tone = []
		for mood in tone_list:
			count = tone_list.count(mood)
			order_tone.append(count)
		index = order_tone.index(max(order_tone))

		dominant_mood = tone_list[index]

		new_score = []
		subjectivity = []
		red_flag = ["kill", "hurt", "cut", "hate", "worst", "horrible", "awful", "repulsive",
					"loathsome", "obnoxious", "disgusting", "pesky", "sad", "crying", "depressed",
					"anxious", "scared", "afraid", "lethal", "die", "harm", "pointless", "fatal", "injure",
					"violent", "toxic", "murder", "suicidal"]

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
		mean_score = np.mean(new_score) + red * (-0.2)
		mean_subjectivity = np.mean(subjectivity)

		return dominant_mood, mean_score

	def send_message(self, dominant_mood, score):
		client = Client(self.account_sid, self.auth_token)
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


