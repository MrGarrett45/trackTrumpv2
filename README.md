# trackTrumpv2

Revamped trackTrump program

How does it work?

trackTrump.py is responsible for collecting the titles of the frontpage of r/politics and analyzing what percentage of them are about Trump. It runs and collects data every hour.

tTrumpStats.py is then responsible for collecting this hourly data and analyzing it over the course of the day as well as the entire project. This data is then output to RESULTS.txt. 

redditBot.py is responsible for posting this data on r/trumpPercent at the end of every day.

These programs are all run via cron jobs on a raspberry pi 3.

Update 7/7: Now includes graphs! Uses matplotlib to create a daily graph as well as a total graph for the whole project. Contains an imgur bot in dailyGraph.py and totalGraph.py to give the image an imgur link and add it to the content of the reddit post. Check out the graphs directories for pictures.

Check out r/trumpPercent or RESULTS.txt for updated data!
