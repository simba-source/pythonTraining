"""
Given first 3 number of a arthimetic progression, predict the next number.
For details about arithmetic progression, you can visit the following link https://en.wikipedia.org/wiki/Arithmetic_progression
Input
3 integers, each should be taken as a input
Output
single integer
Example
Input:
2
5
8
Output:
11
"""

x = int(input())
y = int(input())
z = int(input())

difference = y - x

print(z + difference)