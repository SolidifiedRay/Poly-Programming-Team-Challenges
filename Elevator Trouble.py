#Week 7
'''
C - Elevator Trouble (unsolved) (Breadth First Search)

You are on your way to your first job interview as a program tester, and you are already late. The interview is in a skyscraper and you are currently in floor s, where you see an elevator. Upon entering the elvator, you learn that it has only two buttons, marked "UP u" and "DOWN d". You conclude that the UP-button takes the elevator u floors up (if there aren't enough floors, pressing the UP-botton does nothing, or at least so you assume), whereas the DOWN-button takes you d stories down (or none if there aren't enough). Knowing that the interview is at floor g, and that there are only f floors in the building, you quickly decide to write a program that gives you the amount of button pushes you need to perform. If you simply cannot reach the correct floor, your program halts with the message "use the stairs".

Given input f, s, g, u and d (floors, start, goal, up, down), fi nd the shortest sequence of button presses you must press in order to get from s to g, given a building of floors, or output "use the stairs" if you cannot get from s to g by the given elevator.

Input
The input will consist of one line, namely f s g u d, where 1 <= s, g <= f <= 1000000 and 0 <= u, d <= 1000000. The floors are one-indexed, i.e. if there are 10 stories, s and g be in [1; 10].

Output
You must reply with the minimum numbers of pushes you must make in order to get from s to g, or output "use the stairs" if it is impossible given the con guration of the elevator.

Example
Input:
10 1 10 2 1

Output:
6
Input:
100 2 1 1 0

Output:
use the stairs
'''
first_line_input = input()
var_lists = first_line_input.split()

floors = int(var_lists[0])
start = int(var_lists[1])
goal = int(var_lists[2])
up = int(var_lists[3])
down = int(var_lists[4])

if start < goal:
    if up != 0:
        if (goal-start) % up == 0:
            print((goal-start)/up)
        else:
            up_times = int((goal-start)/up) + 1
            diff = up_times * up + start - goal
            if down != 0 and diff % down == 0:
                if(diff/down < up_times):
                    print(int(up_times + diff/down))
                else:
                    print("use the stairs")
            else:
                print("use the stairs")
    else:
        print("use the stairs")
elif start > goal:
    if down != 0:
        if(start-goal) % down == 0:
            print((start-goal)/down)
        else:
            down_times = int((start-goal)/down) + 1
            diff = goal - (start - down_times * down)
            if up != 0 and diff % up == 0:
                if(diff/up < down_times):
                    print(int(down_times + diff/up))
                else:
                    print("use the stairs")
            else:
                print("use the stairs")
    else:
        print("use the stairs")
else:
    print("use the stairs")

