"""
    Problem: Given an arr[] of size N, the task is to find the number of distinct pairs in the array
    whose sum is > 0

    Input: arr[] = { 3, -2, 1 }
    Output: 2
    Explanation:
    There are two pairs of elements in the array whose sum is positive. They are:
    {3, -2} = 1
    {3, 1} = 4

    Input: arr[] = { -1, -1, -1, 0 }
    Output: 0
    Explanation:
    There are no pairs of elements in the array whose sum is positive.
"""

from bisect import bisect_left

def findNumOfPairs(a, n):
    a = sorted(a)

    ans = 0

    for i in range(n):
        if (a[i] > 0):
            continue

        j = bisect_left(a, -a[i] + 1)
        ans += i - j
    return ans
if __name__ == "__main__":
    a=[3, -2, 1] 
    n =len(a) 
  
    ans = findNumOfPairs(a, n) 
    print(ans)
