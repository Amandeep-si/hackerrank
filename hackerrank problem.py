#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findSubstring' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def findSubstring(s,k):
    # Write your code here
    N = len(s)

    # Initialize prefix sum array
    pre = [0 for i in range(N)]

    # create the prefix sum array
    for i in range(N):
        # Store 1 at the index if it is a vowel
        if (s[i] == 'a' or
            s[i] == 'e' or
            s[i] == 'i' or
            s[i] == 'o' or
            s[i] == 'u'):
            pre[i] = 1
        # Otherwise, store 0
        else:
            pre[i] = 0
        # Process the prefix array
        if (i):
            pre[i] += pre[i - 1]

    # Initialize the variable to store maximum count of vowels
    max = pre[k- 1]
    # Initialize the variable to store substring with maximum count of vowels
    res = s[0 : k]

    # Loop through the prefix array
    for i in range(k, N):
        # Store the current count of vowels
        curr = pre[i] - pre[i - k]

        # Update the result if current count is greater than maximum count
        if (curr > max):
            max = curr
            res = s[i - k + 1 : i + 1]

        elif (curr == max):
            temp = s[i - k + 1 : i + 1]

            if (temp <= res):
                print(res)
            elif(temp==res):
                res="Not Found!"

    # Return the result
    return res

if __name__ == '__main__':
  #  'fptr = open(os.environ['OUTPUT_PATH'], 'w')'
    s = input()

    k = int(input().strip())

    result = findSubstring(s, k)
    print(result)

 #   fptr.write(result + '\n')

  #  fptr.close()
