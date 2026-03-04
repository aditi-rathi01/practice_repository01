# -------- Generate Parentheses --------

# Program: Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]


# Example 2:

# Input: n = 1
# Output: ["()"]
 


# NOTE: What Makes Parentheses VALID?

# Two simple rules:

# At any time, 
# number of ")" <= number of "("              [You cannot close more than you opened ]

# Rule 2: At the end,
# number of "(" = number of ")"


# Visual Example(n=2)

# We must use 2 open and 2 close brackets.

# Start:  
# ""

# Step 1: we can only add "(".

# Step 2: We can:
# - Add "("
# - Add ")"(because we have 1 open)

# ((
# ()


n = int(input("Enter your number: "))

result = []

# Stack will store: (current_string, open_count, close_count)

stack = [("", 0, 0)]       

# What is this?
# This a list (used as a stack)
# Inside it, we put a tuple:

# Stack works like:
# - Add using append()
# - Remove using pop()

# so, 
# current, open_count, closes_coumt = stack.pop()

while stack:
    current, open_count, close_count = stack.pop()              # pop means: Take one unfinished work.

    # If complete string formed

    if len(current) == 2 * n:
        result.append(current)
        continue

    # Add "(" if we still formed

    if open_count < n:
        stack.append((current + "(", open_count + 1, close_count))

    # Add ")" if it won't break rule
    if close_count < open_count:

        stack.append((current + ")", open_count, close_count + 1))
print(result)




# Meaning of while stack:

# Empty list -> False
# Non-Empty list -> True

# Means:
# "Keep running the loop as long as stack is NOT empty."


# NOTE: Steps :
 
# 1.) We Created a stack that stores unfinished strings.
#  stack = [("", 0, 0)]


# 2.) While stack is not empty:
# Take one unfinished string.

# current, open_count, close_count = stack.pop()


# 3.) if string length == 2 * n

# It's complete.
# Put it in result.

# 4.) If open_count< n

# We can add "("
# Push new version into stack.


#5.) If close_count < open_count

# we can add ")"
# Push new version into stack.


#  Stack = Unfinished Paretheses
#  result = finished Paretheses




# Now the most confusing Part is:

# The code is Not forcing pattern like:
# open,close, open, close, open 

# It does NOT control order.
# It explores ALL possibilities


# Here, both IF IF condition are indenpented, so they run independtly.