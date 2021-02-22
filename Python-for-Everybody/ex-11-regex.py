"""
In this assignment you will read through and parse a file with text and numbers. 
You will extract all the numbers in the file and compute the sum of the numbers. 
"""
import re

name = input("Enter file:")
if len(name) < 1:
    name = "regex_sum_1103387.txt"
handle = open(name)
numsum = 0
number_strings = []

for line in handle:
    line_numbers = re.findall('[0-9]+', line)
    number_strings.extend(line_numbers)

for num_string in number_strings:
    numsum += int(num_string)

print(str(numsum))
