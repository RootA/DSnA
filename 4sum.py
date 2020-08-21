# usr/bin/python3
"""
Problem: Given an unsorted array of integers arr and a number s, 
         write a function that finds four numbers (quadruplet) in arr that sum up to s.  
"""

def find_array_quadruplet(arr, s, n):
    # store sum of all pairs in a hash table
    # traverse through all pairs and search for n-1 in the hash table
    # if pair is found of requuired sum, perform a set on the [], 
    # elements are not repeated
    map = {} # store sum of all pairs in a hash table
    for i in range(n-1):
        for j in range(i + 1, n):
            map[arr[i] + arr[j]] = [i, j]
    # traverse through all pairs and search for s - (current pair sum)
    for i in range(n-1):
        for j in range(i + 1, n):
            summ = arr[i] + arr[j]
            # check if s - summ in hash table
            if (s - summ) in map:
                p = map[s - summ]
                if (p[0] != i and p[0] != j and p[1] != i and p[1] !=j):
                    print(f"[{arr[i]}, {arr[j]}, {arr[p[0]]}, {arr[p[1]]}]")
                    return

# driver code
arr = [2, 7, 4, 0, 9, 5, 1, 3]
s = 21
find_array_quadruplet(arr, s, len(arr))