#! python3
#Graph of the project over time

import matplotlib.pyplot as plt
import shelve, datetime, pyimgur

now = datetime.datetime.now()
day = now.day
month = now.month

trumpData = shelve.open('trumpData')

x_axis = list(range(0, len(trumpData)))

transferArr = []
moveDate = datetime.datetime.now()-datetime.timedelta(len(trumpData)-1)
for i in range(len(trumpData)):
	temp = str(i)
	newDate = moveDate + datetime.timedelta(i)
	print(newDate)
	key = str(newDate.month) + str(newDate.day)
	transferArr.append(trumpData[key])
	#print(transferArr[i])

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('Total Graph As Of %d/%d' % (month, day))
ax.set_xlabel('Day #')
ax.set_ylabel('Number of Articles Out of 25')
plt.plot(x_axis, transferArr)
plt.axis([0,100,0,25])
PATH = './totalGraphs/total_%d%d.png' % (month, day)
plt.savefig(PATH)

#imgur bot below
CLIENT_ID = "client_id"
im = pyimgur.Imgur(CLIENT_ID)
uploaded_image = im.upload_image(PATH,title="Total Graph")
print(uploaded_image.link)

#writing the imgur link to RESULTS.txt
resultFile = open('RESULTS.txt', 'a')
resultFile.write('\nOr [here](%s) to see the average number of articles per day being graphed over 100 days\n' % uploaded_image.link)

