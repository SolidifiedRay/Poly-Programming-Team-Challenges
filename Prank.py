#unsolved
'''
JATC and his friend Giraffe are currently in their room, solving some problems. Giraffe has written on the board an array a1, a2, ..., an of integers, such that 1≤a1<a2<…<an≤103, and then went to the bathroom.

JATC decided to prank his friend by erasing some consecutive elements in the array. Since he doesn't want for the prank to go too far, he will only erase in a way, such that Giraffe can still restore the array using the information from the remaining elements. Because Giraffe has created the array, he's also aware that it's an increasing array and all the elements are integers in the range [1,103].

JATC wonders what is the greatest number of elements he can erase?

Input
The first line of the input contains a single integer n (1≤n≤100) — the number of elements in the array.

The second line of the input contains n integers ai (1≤a1<a2<⋯<an≤103) — the array written by Giraffe.

Output
Print a single integer — the maximum number of consecutive elements in the array that JATC can erase.

If it is impossible to erase even a single element, print 0.
'''

num_int_input = input()
int_array_input = input()

num = int(num_int_input)
int_array = int_array_input.split()

output_list = []

if num == 1000:
    output_list.append(1000)

if int(int_array[0]) == 1:
    max_num = 0
    for i in range(0, len(int_array)-1):
        if int(int_array[i]) == int(int_array[i+1])-1:
            max_num += 1
        else:
            break
        if i == len(int_array) - 1:
            max_num += 1
    output_list.append(max_num)
elif int(int_array[len(int_array)-1]) == 1000:
    max_num = 0
    for i in range(len(int_array)-1, -1, -1):
        if int(int_array[i]) == int(int_array[i-1])+1:
            max_num += 1
        else:
            break
        if i == 0:
            max_num += 1
    output_list.append(max_num)

cont_num = 0
i = 1
while i < len(int_array):
    if int(int_array[i]) == int(int_array[i-1])+1:
        while (i < len(int_array)) and (int(int_array[i]) == int(int_array[i-1])+1):
            cont_num += 1
            i += 1
    if(cont_num >= 2):
        output_list.append(cont_num-1)
    cont_num = 0
    i += 1

def find_max():
    max = int(output_list[0])
    for num in output_list:
        if(max <= int(num)):
            max = int(num)
    return max

print(find_max())