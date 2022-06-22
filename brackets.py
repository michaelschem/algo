import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

opens = {"{": "}", "[": "]", "(": ")"}
closes = {"}": "{", "]": "[", ")": "("}

def isBalanced(s):
    stack = []

    for i in s:
        if i in opens:
            stack.append(i)
        elif i in closes:
            if len(stack) == 0:
                return "NO"
            if closes[i] == stack[-1]:
                stack.pop()
            else:
                return "NO"

    if stack == []:
        return "YES"
    return "NO"

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        # fptr.write(result + '\n')
        print(result + '\n')

    # fptr.close()
