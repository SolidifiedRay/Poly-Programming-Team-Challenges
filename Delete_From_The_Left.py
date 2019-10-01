#
'''
Week 4
A-Delete From The left

You are given two strings s and t. In a single move, you can choose any of two strings and delete the first (that is, the leftmost) character. After a move, the length of the string decreases by 1. You can't choose a string if it is empty.

For example:

by applying a move to the string "where", the result is the string "here",
by applying a move to the string "a", the result is an empty string "".
You are required to make two given strings equal using the fewest number of moves. It is possible that, in the end, both strings will be equal to the empty string, and so, are equal to each other. In this case, the answer is obviously the sum of the lengths of the initial strings.

Write a program that finds the minimum number of moves to make two given strings s and t equal.

Input
The first line of the input contains s. In the second line of the input contains t. Both strings consist only of lowercase Latin letters. The number of letters in each string is between 1 and 2⋅105, inclusive.

Output
Output the fewest number of moves required. It is possible that, in the end, both strings will be equal to the empty string, and so, are equal to each other. In this case, the answer is obviously the sum of the lengths of the given strings.
'''
s = input()
t = input()

count = 0

def leftSame(s, t):
    count = 0
    s_index = len(s) - 1
    t_index = len(t) - 1
    while(s_index >= 0 and t_index >= 0):
        if(s[s_index] == t[t_index]):
            count += 1
            s_index -= 1
            t_index -= 1
        else:
            return count
    return count

print(len(s)+len(t)-leftSame(s,t)*2)