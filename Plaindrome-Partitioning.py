# Program: Given a string s, partition s such that every substring of the partition is a palindrome. Return
#          all possible palindrome partitioning of s.

# Example 1:

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]


# Example 2:

# Input: s = "a"
# Output: [["a"]]
 

s = "banana"
result = []

# Using Backtracking:->          "go forward + come back " is called backtracking.

def backtrack(start, path):                    # start = Where we are in string,   path = current pieces we have taken
#                                                (start = 0, path = [] ),        (start = 1, path = ["a"])

    if start == len(s):                             # if we reached end of string
        result.append(path[:])                      # save current answer. [:] -> Start from beginning Go till end.
        return                                      # Stop the path and go back.
    
    for end in range(start, len(s)):                # Try all substrings from current position.
#                                                   Example : end = 0 -> "a", end = 1 -> "aa", end = 2 -> "aab"
       
        substring = s[start: end + 1]               # s[0:1] -> "a",    s[0:2] -> "aa" 
        if substring == substring[::-1]:
            path.append(substring)
            backtrack(end+1, path)
            path.pop()

backtrack(0,[])
print(result)



s = "nitin"

# Step 1: (start = 0)

# Take "n" (index 0 to 0)
# backtrack(end + 1)
# backtrack(0+1)

# -> New: 
# start = 1
# Path = ["n"]


# Step 2: (start = 1)
# Now take "i"
# backtrack(1+1) -> backtrack(2)

# -> New: 
# Start = 2
# Path = ["n", "i"]


# Now, at the end start == len(s):
# Means: string finished
# So, we saved ["n", "i", "t", "i", "n"]



n = "banana"
result2 = []

def backtrack2(start2, path2):
    if start2 == len(n):
        result2.append(path2[:])
        return
    
    for i in range(start2, len(n)):

        substring2 = n[start2: i+1]
        if substring2 == substring2[::-1]:
            path2.append(substring2)
            backtrack2(i+1, path2)
            path2.pop()

backtrack2(0,[])
print(result2)

    

