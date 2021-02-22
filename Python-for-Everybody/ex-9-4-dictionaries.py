"""
Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
emailDict = {}
for line in handle:
    if line.startswith("From "):
        pieces = line.split()
        email = pieces[1]
        if email in emailDict:
            emailDict[email] += 1
        else:
            emailDict[email] = 1

max_key = None
max_val = None

for key, val in emailDict.items():
    if max_val is None or val > max_val:
        max_val = val
        max_key = key

print(max_key, max_val)
