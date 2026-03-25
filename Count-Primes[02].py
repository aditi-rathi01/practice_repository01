# ------ Second Method ------

# In first part, the code we right is accurate and 100 % correct. but not good for time effecient and space effeicent.

# So, here we write a code in another form so that it can be time and space effiecent.

n = 100

if n <= 2:
    print(0)

else:
    is_prime = [True] * (n//2)       # Making list [True, True, True, ......]

    for i in range(3, int(n**0.5)+1, 2):     # (20)^1/2  = 4.4 = 4 -> Loop runs:  
                                             # i = 2,3,4
        if is_prime[i//2]: 
                              
            for j in range(i*i, n , 2*i):
                
               is_prime[j//2] = False
    print(sum(is_prime))



# Simple Sieve(Easy Version):

n = 20

# Step 1: Make a list.

# Write numbers from 0 to 19:
#           0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19


# Step 2: Assume all are primes

#         F F T T T T T T T T T T T T T T T T T T T T T
#      (0 and 1 are not prime)


# Step 3: Start from 2

# Remove multiples of 2: 
#      4 6 8 10 12 14 16 18 

# Step 4: Move to 3
#     6 9 12 15 18

# Step 5: Move to 4:
#         Already removed -> Skip

# Step 6: Move to 5:
#         10 15

# FINAL PRIMES LEFT 
# 2 3 5 7 11 13 17 19

