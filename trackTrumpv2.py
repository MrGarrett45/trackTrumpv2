#!/usr/bin/env python3
#Track trumpv2

import requests, sys, bs4, shelve, datetime, time

def getSite():
    while True:
        url = 'https://www.reddit.com/r/politics/'             
        res = requests.get(url)             #Getting the HTML for the page
        try:
            res.raise_for_status()
        except:
            pass
            print("Failed")
        else:
            break
        time.sleep(2)        
    return res.text

theText = getSite()
soup = bs4.BeautifulSoup(theText, "html.parser")
pic = soup.select('.title')                    #Finding titles with bs
#print(len(pic))

del pic[0]
titleList = pic[1::2] 

if titleList[0].getText().find("self") != -1:
        del titleList[0]

if titleList[0].getText().find("self") != -1:
        del titleList[0]

del titleList[(len(titleList)-1)]
                                               #After these deletions titleList now contains the 25 corrent frontpage titles
trumpCounter = 0
russiaCounter = 0
tNrCounter = 0
for i in range(len(titleList)-1):
    print(titleList[i].getText())
    titleText = titleList[i].getText()
    #print(i)

    if titleText.find("Trump") != -1:
        trumpCounter = trumpCounter + 1
        #print(trumpCounter)

    if titleText.find("Russia") != -1  or titleText.find("Putin") != -1 or titleText.find("Kremlin") != -1:
        russiaCounter = russiaCounter + 1

    if titleText.find("Trump") != -1 and (titleText.find("Russia") != -1  or titleText.find("Putin") != -1 or titleText.find("Kremlin") != -1):
        tNrCounter = tNrCounter + 1

dailyPercent = trumpCounter/(len(titleList)-1)
print("Today %d out of %d articles were about Trump" % (trumpCounter, (len(titleList)-1)))
print("Todays trump percent is: %f" % dailyPercent)

now = datetime.datetime.now()
month = str(now.month)                         #Will use the date as the key for
day = str(now.day)
hour = str(now.hour)                               #the shelf file
key = month+day

hourFile = shelve.open('hourFile')

hourFile[hour] = trumpCounter
if int(hour) == 0:
	for j in range(1, len(hourFile) - 1):
		del hourFile[str(j)]	
	del hourFile['23']

hourFile.close()

#tTrumpStatsv2.run()
#time.sleep(1)   #let the RESULTS.txt populate
#redditBot.runBot()
