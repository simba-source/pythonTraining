'''There is always an integer in Rakesh's mind.
Initially, the integer in Rakesh's mind is 0. Rakesh is now going to eat some symbols, each of which is either + or -. When he eats +, the integer in his mind increases by 1; when he eats -, the integer in his mind decreases by 1.
The symbols Rakesh is going to eat are given to you as a string S. The ith character in S is the ith symbol for him to eat.
Find the integer in Rakesh's mind after he eats all the symbols.
Input
One string, denoting the sequence of symbols eaten by Rakesh.
Output
One integer, denoting the result.
Example
Input
+-++
Output
2
'''
input_str=input("enter the operation string")
mind=0
for char in input_str:
    if char=='+' :
        mind+=1
    elif char=='-':
        mind-=1
    else:
        print("string is invalid")
print(mind)

    