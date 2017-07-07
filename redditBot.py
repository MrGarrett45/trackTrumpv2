#!/usr/bin/env python3
#Testing out new reddit bot

import praw, shelve

#def runBot():

r = praw.Reddit(client_id='client_id',
		client_secret='secret',
		user_agent='trumpPercentBot',
		username='trumpTrackerBot',
		password='fakepasswd')
subreddit = r.subreddit('trumpPercent')
resultFile = open('RESULTS.txt', 'r')
resultsTxt = resultFile.readlines()

hourData = shelve.open('hourFile')
howManyHours = len(hourData)
title = resultsTxt[len(resultsTxt)-(howManyHours+10)]
#title = resultsTxt[1]
body = resultsTxt[len(resultsTxt)-(howManyHours+9):len(resultsTxt)]
newBody = ' '.join(body)
message = subreddit.submit(title, newBody, send_replies=False)
