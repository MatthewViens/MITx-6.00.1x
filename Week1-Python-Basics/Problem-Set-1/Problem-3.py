# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters
# occur in alphabetical order. For example, if s = 'azcbobobegghakl', then
# your program should print
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd',
# then your program should print
# Longest substring in alphabetical order is: abc
# Note: This problem may be challenging. We encourage you to work smart. If
# you've spent ore than a few hours on this problem, we suggest that you move on
# to a different part of the course. If you have time, come back to this problem
# after you've had a break and cleared your head.

substring = s[0]
temp = ''

for i in range(len(s) - 1):
    if s[i] <= s[i + 1]:
        temp = s[i]
        for j in range(i, len(s) - 1):
            if s[j] <= s[j + 1]:
                temp += s[j + 1]
            else:
                break;
        if len(temp) > len(substring):
            substring = temp
        temp = ''

print('Longest substring in alphabetical order is:', substring)
