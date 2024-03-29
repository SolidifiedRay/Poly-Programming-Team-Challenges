# Week 7
'''
B - Coins And Triangle

Read problems statements in Mandarin Chinese , Russian and Vietnamese as well.
Chef belongs to a very rich family which owns many gold mines. Today, he brought N gold coins and decided to form a triangle using these coins. Isn't it strange?

Chef has a unusual way of forming a triangle using gold coins, which is described as follows:

He puts 1 coin in the 1st row.
then puts 2 coins in the 2nd row.
then puts 3 coins in the 3rd row.
and so on as shown in the given figure.
A.png
Chef is interested in forming a triangle with maximum possible height using at most N coins. Can you tell him the maximum possible height of the triangle?

Input
The first line of input contains a single integer T denoting the number of test cases.

The first and the only line of each test case contains an integer N denoting the number of gold coins Chef has.

Output
For each test case, output a single line containing an integer corresponding to the maximum possible height of the triangle that Chef can get.

Constraints
1 ≤ T ≤ 100
1 ≤ N ≤ 109
Subtasks
Subtask 1 (48 points) : 1 ≤ N ≤ 105
'''

first_input = input()
n = int(first_input)
tests = []
for i in range(n):
    line_input = input()
    tests.append(int(line_input))


def return_max_height(n):
    height = 1
    while(1+height)*height/2 <= n:
        height += 1

    return height-1


for coins in tests:
    print(return_max_height(coins))

