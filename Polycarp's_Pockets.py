#Week 7
'''
A - Polycarp's Pockets (can use pigeon hole)

Polycarp has n coins, the value of the i-th coin is ai. Polycarp wants to distribute all the coins between his pockets, but he cannot put two coins with the same value into the same pocket.

For example, if Polycarp has got six coins represented as an array a=[1,2,4,3,3,2], he can distribute the coins into two pockets as follows: [1,2,3],[2,3,4].

Polycarp wants to distribute all the coins with the minimum number of used pockets. Help him to do that.

Input
The first line of the input contains one integer n (1≤n≤100) — the number of coins.

The second line of the input contains n integers a1,a2,…,an (1≤ai≤100) — values of coins.

Output
Print only one integer — the minimum number of pockets Polycarp needs to distribute all the coins so no two coins with the same value are put into the same pocket.
'''

first_line = input()
second_line = input()
n = int(first_line)
coins = second_line.split()

min_used = 1
for i in range(0, n):
    count = 1
    current = coins[i]
    for j in range(i+1, n):
        if coins[j] == current:
            count += 1
    if count > min_used:
        min_used = count
print(min_used)
