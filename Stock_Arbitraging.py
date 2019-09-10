#
'''
Welcome to Codeforces Stock Exchange! We're pretty limited now as we currently allow trading on one stock, Codeforces Ltd. We hope you'll still be able to make profit from the market!

In the morning, there are n opportunities to buy shares. The i-th of them allows to buy as many shares as you want, each at the price of si bourles.

In the evening, there are m opportunities to sell shares. The i-th of them allows to sell as many shares as you want, each at the price of bi bourles. You can't sell more shares than you have.

It's morning now and you possess r bourles and no shares.

What is the maximum number of bourles you can hold after the evening?

Input
The first line of the input contains three integers n,m,r (1≤n≤30, 1≤m≤30, 1≤r≤1000) — the number of ways to buy the shares on the market, the number of ways to sell the shares on the market, and the number of bourles you hold now.

The next line contains n integers s1,s2,…,sn (1≤si≤1000); si indicates the opportunity to buy shares at the price of si bourles.

The following line contains m integers b1,b2,…,bm (1≤bi≤1000); bi indicates the opportunity to sell shares at the price of bi bourles.

Output
Output a single integer — the maximum number of bourles you can hold after the evening.
'''

first_line = input()
second_line = input()
third_line = input()

first_line_int = first_line.split()
s = second_line.split()
b = third_line.split()

r = int(first_line_int[2])

def find_buy_min():
    min = int(s[0])
    for num in s:
        if(min >= int(num)):
            min = int(num)
    return min

def find_sell_max():
    max = int(b[0])
    for num in b:
        if(max <= int(num)):
            max = int(num)
    return max

def maximum_bourles():
    num_buy = (r//find_buy_min())
    remain = r - num_buy * find_buy_min() + num_buy * find_sell_max()
    if(remain > r):
        print(remain)
    else:
        print(r)

maximum_bourles()


