# Example: Given an integer n, return the number of prime numbers that are strictly less than n.

# Example 1:

# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.


# Example 2:

# Input: n = 0
# Output: 0


# Example 3:

# Input: n = 1
# Output: 0
 
n = 100
l = []

for i in range(2, n+1):
    is_prime = True

    for j in range(2,i):
        if i % j == 0:
            is_prime = False
            break
        
    if is_prime:
        l.append(i)
print(l)
print(len(l))

n2 = 100
l2 = []

for i in range(2, n2+1):
    for j in range(2,i):
        if i % j == 0:                     # NOTE: "Run else only if loop finishes without finding any divisor."
            break                          # if we write else just down the if then, so, for every j:
    else:                                  # if condition is false -> else runs -> append happens.
            l2.append(i)

print(l2)

# Example: i = 5
# j = 2
# 5 % 2 != 0 -> append 5
# j = 3 -> append again
# j = 4 -> append again



