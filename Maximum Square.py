#Week 11
'''
Maximum Square

'''
cases = input()
output = []
for n in range(int(cases)):
    first = input()
    second = input()
    num_planks = int(first)
    planks_string = second.split()
    planks = []
    for plank in planks_string:
        planks.append(int(plank))
    planks.sort()
    planks.reverse()

    max = num_planks
    while max > 0:
        if planks[max-1] >= max:
            output.append(max)
            break
        max -= 1

for num in output:
    print(num)