#! python3
#Daily graph

import matplotlib.pyplot as plt
import shelve, datetime, pyimgur

now = datetime.datetime.now()
day = now.day
month = now.month

hourFile = shelve.open('hourFile')

x_axis = list(range(0, len(hourFile)-1)) 

transferArr = []
for i in range(len(hourFile) -1):
	temp = str(i)
	#print(temp)
	transferArr.append(hourFile[temp])

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('Daily Graph for %d/%d' % (month, day))
ax.set_xlabel('Hour (military time)')
ax.set_ylabel('Number of Articles Out of 25')
plt.plot(x_axis, transferArr)
plt.axis([0,24,0,25])
PATH = './dailyGraphs/daily_%d%d.png' % (month, day)
plt.savefig(PATH)

#imgur bot below
CLIENT_ID = "client_id"
im = pyimgur.Imgur(CLIENT_ID)
uploaded_image = im.upload_image(PATH,title="Daily Graph")
print(uploaded_image.link)

#writing the imgur link to RESULTS.txt
resultFile = open('RESULTS.txt', 'a')
resultFile.write('Click [here](%s) to see the daily graph\n' % uploaded_image.link)
resultFile.close()
