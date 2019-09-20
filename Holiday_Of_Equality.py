#
'''
In Berland it is the holiday of equality. In honor of the holiday the king decided to equalize the welfare of all citizens in Berland by the expense of the state treasury.

Totally in Berland there are n citizens, the welfare of each of them is estimated as the integer in ai burles (burle is the currency in Berland).

You are the royal treasurer, which needs to count the minimum charges of the kingdom on the king's present. The king can only give money, he hasn't a power to take away them.

Input
The first line contains the integer n (1 ≤ n ≤ 100) — the number of citizens in the kingdom.

The second line contains n integers a1, a2, ..., an, where ai (0 ≤ ai ≤ 106) — the welfare of the i-th citizen.

Output
In the only line print the integer S — the minimum number of burles which are had to spend.
'''

citizens_input = input()
citizens_welfare_input  = input()

citizens = int(citizens_input)
citizens_welfare_list = citizens_welfare_input.split()

def find_max():
    max = int(citizens_welfare_list[0])
    for num in citizens_welfare_list:
        if(max <= int(num)):
            max = int(num)
    return max

def min_spend():
    max_welfare = find_max()
    total = 0;
    if citizens == 1:
        print(total)
    else:
        for welfare in citizens_welfare_list:
            total += (max_welfare-int(welfare))
        print(total)

min_spend()