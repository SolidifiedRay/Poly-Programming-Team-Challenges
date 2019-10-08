#B Cloning Toys
'''
Imp likes his plush toy a lot.


Recently, he found a machine that can clone plush toys. Imp knows that if he applies the machine to an original toy, he additionally gets one more original toy and one copy, and if he applies the machine to a copied toy, he gets two additional copies.

Initially, Imp has only one original toy. He wants to know if it is possible to use machine to get exactly x copied toys and y original toys? He can't throw toys away, and he can't apply the machine to a copy if he doesn't currently have any copies.

Input
The only line contains two integers x and y (0 ≤ x, y ≤ 109) — the number of copies and the number of original toys Imp wants to get (including the initial one).

Output
Print "Yes", if the desired configuration is possible, and "No" otherwise.

You can print each letter in arbitrary case (upper or lower).
'''

num_input = input().split()
x = int(num_input[0])
y = int(num_input[1])
original = 1
copy = 0

if y == 0:
    print("NO")
elif y == 1 and x > 0:
    print("NO")
elif y == 1 and x == 0:
    print("YES")
elif ((x-(y-1))%2 == 0 and (x-(y-1))>0):
    print("YES")
else:
    print("NO")
