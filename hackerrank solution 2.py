#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'longestSubarray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def longestSubarray(arr):
    # Write your code here
    n = len(arr)
    k = 1
    Max = 1
    # Initialize set
    s = set()
    for i in range(n - 1):
        # Store 1st element of sub-array into set
        s.add(arr[i])
        for j in range(i + 1, n):
            # Check absolute difference between two elements
            if (abs(arr[i] - arr[j]) == 0 or
                    abs(arr[i] - arr[j]) == k):

                # If the new element is not present in the set
                if (not arr[j] in s):

                    # If the set contains two elements
                    if (len(s) == 2):
                        break

                    # Otherwise
                    else:
                        s.add(arr[j])

            else:
                break

        if (len(s) == 2):

            # Update the maximum length
            Max = max(Max, j - i)

            # Remove the set elements
            s.clear()

        else:
            s.clear()

    return Max


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = longestSubarray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
