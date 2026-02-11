# Program: Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...

# Example 1:

# Input: columnNumber = 1
# Output: "A"


# Example 2:

# Input: columnNumber = 28
# Output: "AB"


# Example 3:

# Input: columnNumber = 701
# Output: "ZY"




# For Number to Title:

n = int(input("Enter Your Number: "))

result = ""
while n > 0:
   n -= 1                                          # because n = 1 will give the value "result = chr(26 + 1) = chr(27) = 'B' ".

   result = chr(65+ (n % 26)) + result             # chr(65) = "A",| ord("A") = 65.
   n //= 26

print(result)


# From title to Number

str = input("Enter: ")
res = 0
for letter in str:
   res = res*26 + (ord(letter)-ord("A")+ 1)

print(res)


