#A Turn the Rectangles
'''
There are n rectangles in a row. You can either turn each rectangle by 90 degrees or leave it as it is. If you turn a rectangle, its width will be height, and its height will be width. Notice that you can turn any number of rectangles, you also can turn all or none of them. You can not change the order of the rectangles.

Find out if there is a way to make the rectangles go in order of non-ascending height. In other words, after all the turns, a height of every rectangle has to be not greater than the height of the previous rectangle (if it is such).

Input
The first line contains a single integer n (1≤n≤105) — the number of rectangles.

Each of the next n lines contains two integers wi and hi (1≤wi,hi≤109) — the width and the height of the i-th rectangle.

Output
Print "YES" (without quotes) if there is a way to make the rectangles go in order of non-ascending height, otherwise print "NO".

You can print each letter in any case (upper or lower).
'''

num_int_input = input()
n = int(num_int_input)
rect_list = []
for i in range(n):
    rectangle = input().split()
    width = int(rectangle[0])
    height = int(rectangle[1])
    rect_list.append([width, height])
can_order = True
width = rect_list[0][0]
height = rect_list[0][1]
highest = width if width > height else height
for i in range(n):
    width = rect_list[i][0]
    height = rect_list[i][1]
    if width > highest and height > highest:
        can_order = False
        break
    else:
        if width > highest and height <= highest:
            highest = height
        elif width <= highest and height > highest:
            highest = width
        else:
            highest = width if width > height else height

if can_order:
    print("YES")
else:
    print("No")
