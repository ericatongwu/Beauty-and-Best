import json
import requests
from pprint import pprint
import scipy.stats as ss
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import random

# Input: file name
# Output: read into python
def read_json(file):

	with open(file) as f:
		data = json.load(f)

	return data

# Input: dictionary
# Output: graph for analysis 
# def trend(dictionary):
# 	length = pd.Series(dictionary['time_len'])
# 	date = pd.Series(dictionary['date'])
# 	plt.figure()
# 	plt.hist([length, date], histtype='barstacked', normed=True);
# 	concatenate = np.concatenate((length,date))
# 	sns.kdeplot(concatenate);
# 	plt.show()

# clean old data, add new data
# Input: new data
# Output: new json update to firebase

def new_change_old(url, old_json_data, day, v_time, v_type, cloth):

	delete_old = requests.delete(url)
	new_json_data = old_json_data
	new_json_data["time_len"].append(v_time)
	new_json_data["date"].append(day)
	new_json_data["name"].append(v_type)
	new_json_data["dress"].append(cloth)
	
	new_json = json.dumps(new_json_data)

	with open('new_json_data.json', 'w') as fp:
		json.dump(new_json, fp)

	return new_json

# make suggestion
# Input: date
# Output suggestions

def suggestion_today(dic, today):

	if today not in dic["date"]:
		today_video = random.choice(dic["name"])
		today_time = random.choice(range(100))
		today_cloth = random.choice(dic["dress"])
	else:
		pass
	print(today_video, today_time, today_cloth)
	return today_video, today_time, today_cloth


if __name__ == "__main__":
	file  = "data.json"
	data = read_json(file)
	url = "https://project-2a5c4.firebaseio.com/bb.json"

	day = "Mar 29"
	today_video, today_time, today_cloth = suggestion_today(data, day)
	print(suggestion_today(data,day))
	new_json = new_change_old(url, data, day, today_time, today_video, today_cloth)
	with open("new_json_data.json", "r") as fp:
		acc_file = str(fp.read())
	# upload_firebase(url, json_file)
	
	response = requests.put(url, acc_file)
	