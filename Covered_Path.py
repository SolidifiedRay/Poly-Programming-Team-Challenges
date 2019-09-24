#
'''
The on-board computer on Polycarp's car measured that the car speed at the beginning of some section of the path equals v1 meters per second, and in the end it is v2 meters per second. We know that this section of the route took exactly t seconds to pass.

Assuming that at each of the seconds the speed is constant, and between seconds the speed can change at most by d meters per second in absolute value (i.e., the difference in the speed of any two adjacent seconds does not exceed d in absolute value), find the maximum possible length of the path section in meters.

Input
The first line contains two integers v1 and v2 (1 ≤ v1, v2 ≤ 100) — the speeds in meters per second at the beginning of the segment and at the end of the segment, respectively.

The second line contains two integers t (2 ≤ t ≤ 100) — the time when the car moves along the segment in seconds, d (0 ≤ d ≤ 10) — the maximum value of the speed change between adjacent seconds.

It is guaranteed that there is a way to complete the segment so that:

the speed in the first second equals v1,
the speed in the last second equals v2,
the absolute value of difference of speeds between any two adjacent seconds doesn't exceed d.
Output
Print the maximum possible length of the path segment in meters.
'''

first_line_input = input().split()
second_line_input = input().split()
v1 = int(first_line_input[0])
v2 = int(first_line_input[1])
t = int(second_line_input[0])
d = int(second_line_input[1])

max = v1
step = 2
num = v1

while(step < t):
    if(v2+(t-step)*d) > (num+d):
        num += d
    else:
        num += (v2+(t-step)*d) - num
    max += num
    step += 1

max += v2

print(max)
