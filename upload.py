import json
import requests
from pprint import pprint
import scipy.stats as ss
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

# Input: file name
# Output: read into python
def read_json(file):

	with open(file) as f:
		data = json.load(f)
	return data

# Input: json in python
# Output: data in dictionary for plot
def get_data(json_loaded):

	user = {"time_len":[], "date":[], "name": []}

	for day in data:
		user["time_len"].append(day['time'])
		user["date"].append(day['date'])
		user["name"].append(day['type'])

	return user

# Input: dictionary
# Output: graph for analysis 
def trend(dictionary):
	length = pd.Series(dictionary['time_len'])
	date = pd.Series(dictionary['date'])
	plt.figure()
	plt.hist([length, date], histtype='barstacked', normed=True);
	concatenate = np.concatenate((length,date))
	sns.kdeplot(concatenate);
	plt.show()

if __name__ == "__main__":
	file  = "data.json"
	data = read_json(file)
	user = get_data(data)
	trend(user)