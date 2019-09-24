total_distance = 6000
station = 4
station_wait = 26
distance_between = 2000
max_speed = 26.4
a = 1.1
d = -2.0

t1 = (max_speed-0)/a
print("t1 "+str(t1))
s1 = (max_speed * max_speed)/(2 * a)
print("s1 "+str(s1))
t3 = (0-max_speed)/d
print("t3 "+str(t3))
s3 = (-(max_speed*max_speed))/(2*d)
print("s3 "+str(s3))

s2 = distance_between-(s1+s3)
print("s2 "+str(s2))
t2 = s2/max_speed
print("t2 "+str(t2))

total_travel_time_between = t1 + t2 + t3
print("total_travel_time_between "+str(total_travel_time_between))
total_time = (station-1)*total_travel_time_between + (station-2)* station_wait
print(total_time)