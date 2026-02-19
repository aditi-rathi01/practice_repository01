# Program: Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"


# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 


strs = ["flower","flow","flight"]

# Important Observation: The prefix must start from index zero. We cannot check from middle. It must check from the beginning.

# Next Step: Instead of comparing whole words, we should check letter to letter. first letter, second letter, thrid letter.

# As soon as one mismatch happens -> stop immediatly.


prifix = ""              # Create an empty string. This will store the common prefix.

for i in range(len(strs[0])):
    
    char = strs[0][i]                 # Here, we are only taking first word from the list. ["flower"]. It's fixed and used to compare index wise.
    match = True                      # Because, we start with an assumption. "Maybe all strings match at this position."
    
    for word in strs:
        if i >= len(word) or word[i] != char:

            match = False                  # At list one string is different.
            break

    if match:                        # if match means: "Only add this character to prefix if all strings matched at this position".
        prifix += char
    else:
        break

print(prifix)



# Taking an another example to understand, "match" concept.

numbers = [2,4,6,8]           # Checking, all Number are even or not.

match = True                  # Assume all are even

for num in numbers:
    if num % 2 != 0:
        match = False

if match:
    print("print all numbers are even")

else:
    print("Not all numbers are even")




# Example 2: All Students passed?

marks = [60, 75,66,45]

match = True                    # Assuming all numbers are matched.

for m in marks:

    if m < 50:
        match = False
        break
if match:
    print(m)
else:
    print("Some students are falid")


# Example 3: All letters are capital?

word = "HELLO"
match = True                       # Assume, that all are capital

for char in word:
    if char.islower():
        match = False
        break
if match:
        print("All letters are capital")
else:
        print("Some letters are small")

