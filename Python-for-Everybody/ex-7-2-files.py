"""
Write a program that prompts for a file name, then opens that file 
and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines 
and compute the average of those values and produce an output as shown below:
Average spam confidence: 0.7507185185185187 
Do not use the sum() function or a variable named sum in your solution. 
"""

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
number = 0
avgnum = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    formatted = line.strip()
    singlenum = formatted[20:]
    number = number + float(singlenum)
    avgnum = number / count
print("Average spam confidence:", avgnum)
