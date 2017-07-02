#!/usr/bin/env python3
#Testing out new reddit bot

import praw, shelve

def runBot():

	r = praw.Reddit(client_id='client_id',
			client_secret='secret',
			user_agent='trumpPercentBot',
			username='trumpTrackerBot',
			password='passwd')
	subreddit = r.subreddit('trumpPercent')
	resultFile = open('RESULTS.txt', 'r')
	resultsTxt = resultFile.readlines()

	hourData = shelve.open('hourFile')
	howManyHours = len(hourData)
	title = resultsTxt[len(resultsTxt)-(howManyHours+5)]
	body = resultsTxt[len(resultsTxt)-(howManyHours+4):len(resultsTxt)]
	newBody = '\n'.join(body)
	message = subreddit.submit(title, newBody, send_replies=False)
