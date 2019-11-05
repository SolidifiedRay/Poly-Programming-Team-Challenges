#Week 9
'''
A - Ania and Minimizing

Ania has a large integer S. Its decimal representation has length n and doesn't contain any leading zeroes. Ania is allowed to change at most k digits of S. She wants to do it in such a way that S still won't contain any leading zeroes and it'll be minimal possible. What integer will Ania finish with?

Input
The first line contains two integers n and k (1≤n≤200000, 0≤k≤n) — the number of digits in the decimal representation of S and the maximum allowed number of changed digits.

The second line contains the integer S. It's guaranteed that S has exactly n digits and doesn't contain any leading zeroes.

Output
Output the minimal possible value of S which Ania can end with. Note that the resulting integer should also have n digits.
'''
first_line = input().split()
n = int(first_line[0])
k = int(first_line[1])
S = input()

if k == 0:
    print(S)
elif n == 1:
    print("0")
else:
    if S != 1:
        k -= 1
        S = "1" + S[1:]
    index = 1
    while k > 0 and index < n:
        if S[index] != "0":
            S = S[0: index] + "0" + S[index+1:]
            k -= 1
        index += 1
    print(S)