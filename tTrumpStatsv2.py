#!/usr/bin/env python3
#idea: initally add all the hours up and just put the total in the trumpData
#that way you can do daily stats with transferArr and totalStats with trumpData
#total hours analyzed = number of days * 24
import shelve, os, datetime, pprint, re
import redditBot

trumpData = shelve.open('trumpData')
hourFile = shelve.open('hourFile')

now = datetime.datetime.now()
day = str(now.day)
month = str(now.month)
date = month+day

transferArr = []
hoursToday = 0
for i in range(len(hourFile)):
	transferArr.append(list(hourFile.values())[i])

hoursToday = sum(list(hourFile.values()))
todayAvgP = hoursToday/(25*(len(transferArr)))
todayAvg = todayAvgP * 25
print('today avg: %f' % todayAvgP)
trumpData[date] = todayAvg

totalHours = sum(list(trumpData.values()))
totalAvgP = totalHours/(25*(len(trumpData)))
totalAvg = totalAvgP * 25
largestFlag = False
smallestFlag = False
if list(trumpData.values())[len(trumpData)-1] == max(list(trumpData.values())):
	largestFlag == True
	if list(trumpData.values())[len(trumpData)-1] == min(list(trumpData.values())):
		smallestFlag = True
highestToday = max(transferArr)  #Highest and lowest hours for # of articles
smallestToday = min(transferArr)
print('smallest today: %d' % smallestToday)
print('largest today: %d' % highestToday)
if smallestFlag == True:
	print('smallest')
if largestFlag == True:
	print('largest')


stringList = []
for n in range(len(transferArr)):
	stringList.append("At %d:00 there were %d articles\n" % (int(list(hourFile.keys())[n]), transferArr[n]))

def atoi(text):
	return int(text) if text.isdigit() else text

def natural_keys(text):
	return [atoi(c) for c in re.split('(/d+)', text)]

stringList.sort(key=natural_keys)
print(stringList)

resultFile = open('RESULTS.txt', 'a')
resultFile.write('\nData for %s/%s/%s:\n' % (month, day, str(now.year)))
resultFile.write('Today %f of articles were based on Trump, or %f out of 25' % (todayAvgP, todayAvg))
if largestFlag == True:
	resultFile.write(". Thats a new high!")
if smallestFlag == True:
	resultFile.write(". That's a new low!")
resultFile.write('\nAt the highest point today %d out of 25 articles were about Trump, and at the lowest point %d were about Trump.\n' % (highestToday, smallestToday))
resultFile.write('The breakdown was as follows:\n')
for m in range(len(transferArr)):
	resultFile.write(stringList[m])
	resultFile.write('Since this experiment start %f of articles have been based on Trump, or %f out of 25.\n' % (totalAvgP, totalAvg))

hourFile.close()
trumpData.close()

redditBot.runBot()
