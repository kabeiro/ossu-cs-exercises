"""
Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour.
"""

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
timeDict = {}

for line in handle:
    if line.startswith("From "):
        pieces = line.split()
        time = pieces[5].split(':')
        hour = time[0]
        if hour in timeDict:
            timeDict[hour] += 1
        else:
            timeDict[hour] = 1
sortedDict = sorted(timeDict.items())

for k, v in sortedDict:
    print(k, v)
