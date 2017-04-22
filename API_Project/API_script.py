#!/usr/bin/env python
import urllib2
import json
import requests

page = 1
while True:
	url = 'https://api.github.com/repos/holbertonschool/Betty/commits?page=%d' % page
	info = urllib2.urlopen(url).read()
	r = requests.head(url=url, headers={'User-Agent': 'Wabluekey', 'Authorization': 'token d50c9558a8c630dd87bb31192db4c79cd61a1337'})
	the_data = json.loads(info)
	i = 0
	dict_len = len(the_data)
	while i < dict_len:
		date = (the_data[i]['commit']['committer']['date'])
		user_name = the_data[i]['commit']['committer']['name']
		commit_id = the_data[i]['sha']
		message = the_data[i]['commit']['message']
		output = (date,": ",commit_id," - ",user_name," - ", message)
		print "".join(output)
		i +=1
	page += 1
	if (len(the_data) == 0):
		break
