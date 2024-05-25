'''A programming competition site regularly holds programming contests at different levels.
The first level contest is called ABC, which is open for contestants with ranking less than 1200.
The contest level after the ABC is called ARC, which is open for contestants with ranking less than 2800.
The contest level after the ARC is called AGC, which is open for all contestants.
Help Ramesh in figuring out which is the next level for him given his current rank 'R'.
Input
One Integer, denoting R.
Output
Print the name of the next contest rated for Ramesh (ABC, ARC or AGC).
Example
Input1:
1199
Output1:
ABC
Explanation1:
1199 is less than 1200, so ABC will be rated.
Input2:
1200
Output2:
ARC'''
rank=int(input("enter rank"))
if rank<1200:
    print('ABC contest')
elif rank<2800:
    print('ARC contest')
else:
    print("AGC contest")
    