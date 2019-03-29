import json
import requests
from pprint import pprint
import seaborn as sns
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates


# Input: file name
# Output: read into python
def read_json(file):

	with open(file) as f:
		data = json.load(f)
	return data

# Input: json in python
# Output: data in dictionary for plot
def get_data(json_loaded):

	user = {"time_len":[], "date":[], "name": [], "wear": []}

	for day in data:
		user["time_len"].append(day['time'])
		user["date"].append(day['date'])
		user["name"].append(day['type'])
		user["wear"].append(day['cloth'])

	return user

sns.set_style('darkgrid')

# Input: dictionary
# Output: graph for analysis 
def plot_time_vs_day(dictionary):
	data_df = pd.DataFrame.from_dict(dictionary)
	data_df.plot(kind='bar',x='date',y='time_len')
	plt.show()

# Input: dictionary
# Output: Time vs date curve, type curve 
def day_time_curve(dictionary):
	data_df = pd.DataFrame.from_dict(dictionary)
	data_df.set_index('date',inplace=True)
	#plot data
	fig, ax = plt.subplots(figsize=(15,7))
	data_df.plot(ax=ax)
	#set ticks every week
	ax.xaxis.set_major_locator(mdates.DayLocator())
	#set major ticks format
	ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))	


if __name__ == "__main__":
	file  = "data.json"
	data = read_json(file)
	user = get_data(data)
	plot_time_vs_day(user)