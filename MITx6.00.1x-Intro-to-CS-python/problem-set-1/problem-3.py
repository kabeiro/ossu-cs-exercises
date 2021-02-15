"""
Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
"""

s = 'azcbobobegghakl'
longword = ''

for x in range(len(s)-1):
    for y in range(len(s)+1):
        word = s[x:y]
        if word == ''.join(sorted(word)):
            if len(word) > len(longword):
                longword = word

print('Longest substring in alphabetical order is: ' + longword)
