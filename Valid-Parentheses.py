# Program: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

# An input string is valid if:
# 1.Open brackets must be closed by the same type of brackets.
# 2.Open brackets must be closed in the correct order.
# 3.Every close bracket has a corresponding open bracket of the same type.

# Example 1:

# Input: s = "()"

# Output: true

#Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 5:

# Input: s = "([)]"

# Output: false


# --> So, Here let's do this problem with the help of stack. (LIFO) last in first out.
# let's take an example which is example no.2

# Simple Logic: 
# Open Bracket -> Save in somewhere.
# close barcket -> remove from the saving point.
# At, last if stack gone empty with sequence wise. then, paranthesis is valid.

s = ([])
stack = []

mapping = {
"(": ")", "[":"]", "{": "}"
}

for char in s:
    if char in mapping:

        stack.append(char)
    else:                                                 # else, runs when char is closing bracket.
                                                          # In Python, an empty list consider as false, and non-empty list is True.
        if not stack or mapping[stack[-1]] != char:       # If not stack means, empty list. stack is empty.
                                                          # Why we check empty list because if are looking for close bracket. then
                                                          # there should be exists of open bracket. and if list is empty then there is no open bracket.
# stack[-1] means last opend bracket.
            print(False)
        stack.pop()
print(len(stack)== 0)                              # After all condition if stack becomes empty it givesssss true.