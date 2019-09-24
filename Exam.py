#
'''
An exam for n students will take place in a long and narrow room, so the students will sit in a line in some order. The teacher suspects that students with adjacent numbers (i and i + 1) always studied side by side and became friends and if they take an exam sitting next to each other, they will help each other for sure.

Your task is to choose the maximum number of students and make such an arrangement of students in the room that no two students with adjacent numbers sit side by side.

Input
A single line contains integer n (1 ≤ n ≤ 5000) — the number of students at an exam.

Output
In the first line print integer k — the maximum number of students who can be seated so that no two students with adjacent numbers sit next to each other.

In the second line print k distinct integers a1, a2, ..., ak (1 ≤ ai ≤ n), where ai is the number of the student on the i-th position. The students on adjacent positions mustn't have adjacent numbers. Formally, the following should be true: |ai - ai + 1| ≠ 1 for all i from 1 to k - 1.

If there are several possible answers, output any of them.
'''

num_input = input()
n = int(num_input)

if n == 1:
    print("1")
    print("1")
elif n == 2:
    print("1")
    print("1")
elif n == 3:
    print("2")
    print("1 3")
else:
    print(str(n))
    end = int(n/2)+1
    mid = int(n/2)+1
    start = 1
    while(mid <= n and start < end):
       print(str(mid), end=' ')
       print(str(start), end=' ')
       mid += 1
       start += 1
    if(n%2 != 0):
        print(str(mid))
