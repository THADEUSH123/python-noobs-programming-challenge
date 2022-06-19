

# Create the best possible data structure to group this data set better.
devices = [
'ssw001.atn1', 'ssw002.atn1', 'ssw003.atn1', 'ssw012.prn1',
'ssw004.atn1', 'ssw005.atn1', 'ssw006.prn1', 'ssw007.prn1',
'ssw008.lla2', 'ssw009.lla2', 'ssw010.lla2', 'ssw011.lla2',
'esw001.atn1', 'esw002.atn1', 'esw003.atn1', 'esw004.atn1',
'esw005.atn1', 'esw006.atn1', 'esw007.lla2', 'esw008.lla2',
'fsw001.atn1', 'fsw002.atn1', 'fsw003.atn1', 'fsw004.atn1',
'fsw001.atn1', 'fsw002.atn1', 'fsw003.lla2', 'fsw004.lla2',
]


def organize(devices):
    struct = {}
    for d in devices:
        pre, dc = d.split(".")
        if dc not in struct.keys():
            struct[dc] = [pre]
        else:
            struct[dc].append(pre)
    return struct

print(organize(devices))
print("---------")









# Exercise 2:
# Given a free text, write a function that finds
# all valid IPv4 addresses.
text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, 192.168.1.1 sed do
eiusmod tempor incididunt ut labore a.b.n.f et dolore magna 10.0.0.1.1 jh. Ut enim ad
veniam, quis 58.23.14.12 nostrud exercitation ullamco laboris nisi ut aliquip
ex ea commodo consequat. 255.255.255.1 Duis aute 300.2.1.1 dolor in reprehenderit
192.168.256.0 in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
as 12.a.1.1 Excepteur sint occaecat cupidatat non proident, 10.0.0.10
sunt in culpa qui officia deserunt mollit anim id est laborum 20.25.a.10
0.2.3.4 and 0.168.256.0
"""

import re

def ip_adresses(t):
    ips = []
    pattern = r'\d+.\d+.\d+.\d+'
    dot_dec_format = re.findall(pattern,t)  # Mat

    for dot_dec in dot_dec_format:
        b1, b2, b3, b4 = re.findall(r'\d+',dot_dec)
        if int(b1) > 255 or int(b2) > 255 or int(b3) > 255 or int(b4) > 255:
            pass  # All values must be bytes(256 bits) in binary i.e. between 0 and 255
        elif int(b1) == 0:
            pass # First octet/byte cannot be 0 bits / 000 per RFC specification.
        else:
            ips.append(dot_dec)
    return ips

# for ip in ip_adresses(text):
#    print(ip)


# Exercise 1
# Given a list of integers greater than zero, write a class or function to
# find if there is a way to split the array in two (without reordering
# any elements) such that the numbers before the split add up to the numbers
# after the split. If so, return the two resulting arrays.
# e.g.
# [1,3,4,6,2] should return [1,3,4] and [6,2] (summ of elements in both
# lists is 8)
# [1,7,8] should return [1,7] and [8]

def split(l):
    for i in range(0,len(l)):
        if sum(l[0:i]) == sum(l[i:]):
            return (l[0:i], l[i:])
    return l


lst = [1,3,4,6,2,0,0]
# print(split(lst))


for i in ("yo", "yo", "ma"):
    print(i)


# Exercise 3
# Given unsorted list, return the top int in the array

a = [2,3,4,5,1,3,2,4,1,5,7,8,5,2,2,1]

print(max(a))


# Write a function that checks in place whether the given string, ignoring non-letter characters and capitalization, is a palindrome. For example:


def palindrome(input):
    return input == input[::-1]

print(palindrome("racecar"))
