# Program: Given two binary strings a and b, return their sum as a binary string.

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"


# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
 


# Algorithm : 

#  Example:
#  Add

#  a = "11"
#  b = "01"

# Step 1: Start from right

# Rightmost digits:
# 1 + 1 + carry(0) = 2
# result_value = 2 % 2 = 0
# carry = 2 // 2 = 1

# Step 2: Move Left

# 1 + 0 + carry(1) = 2
# result = 00


# Step 3: Loop Finished 

# Carry is still 1 -> add it
# result = 100


a = "1010"
b = "1011"
output = ""

i = len(a) - 1
j = len(b) - 1

carry = 0

while i>= 0 or j>= 0 or carry:

    bit1 = int(a[i]) if i>= 0 else 0
    bit2 = int(b[i]) if j>= 0 else 0

    total = bit1 + bit2 + carry

    output += str(total % 2)
    carry = total // 2

    i -= 1
    j -= 1

output = output[::-1]

print(output)


# NOTE: In this loop code don't take value like (0,0), (0,1), (0,2), (0,3), (1,0),........
#       because it's not nested loop. 