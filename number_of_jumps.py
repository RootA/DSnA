"""
    Problem: Find the number of jumps to reach X in the number line from zero
    Example:
        Input: X = 8
        Output: 4
        Explanation: 0 -> -1 -> 1 -> 4 -> 8 are the possible stages     
"""

# Calculate sum of numbers frrom 1 to X
def summation(x):
    return int((x * (x + 1)) / 2)

# find the number of jumps to reach X in the number line from zero
def getJumps(n):
    # convert number to positive
    n = abs(n)

    answer = 0

    # continue till number is lesser or not in the same parity
    while (summation(answer) < n or (summation(answer) -n ) & 1):
        answer +=1
    
    return answer

if __name__ == '__main__':
    n = 10
    print(getJumps(n))


