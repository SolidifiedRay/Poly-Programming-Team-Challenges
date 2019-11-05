#Week 9
'''
B - Dawid and Bags of Candies

Dawid has four bags of candies. The i-th of them contains ai candies. Also, Dawid has two friends. He wants to give each bag to one of his two friends. Is it possible to distribute the bags in such a way that each friend receives the same amount of candies in total?

Note, that you can't keep bags for yourself or throw them away, each bag should be given to one of the friends.

Input
The only line contains four integers a1, a2, a3 and a4 (1≤ai≤100) — the numbers of candies in each bag.

Output
Output YES if it's possible to give the bags to Dawid's friends so that both friends receive the same amount of candies, or NO otherwise. Each character can be printed in any case (either uppercase or lowercase).
'''

bags = input().split()

num = (int(bags[0]) + int(bags[1]) + int(bags[2]) + int(bags[3]))/2
can_divide = False

for i in range(4):
    if(int(bags[i])==num):
        print("YES")
        can_divide = True

if(not can_divide):
    if(int(bags[0])+int(bags[1])) == (int(bags[2])+int(bags[3])):
        print("YES")
    elif(int(bags[0])+int(bags[2])) == (int(bags[1])+int(bags[3])):
        print("YES")
    elif(int(bags[0])+int(bags[3])) == (int(bags[1])+int(bags[2])):
        print("YES")
    else:
        print("NO")

