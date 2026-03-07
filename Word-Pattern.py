# Program: Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern
# and a non-empty word in s. Specifically:

# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"

# Output: true

# Explanation:

# The bijection can be established as:

# 'a' maps to "dog".
# 'b' maps to "cat".
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"

# Output: false

# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"

# Output: false


pattern = "abba"
s = "dog cat cat dog"
result = {}

word = s.split()

if len(pattern) != len(word):
    print(False)

else:

    for i in range(len(pattern)):
        
        p = pattern[i]
        w = word[i]

        if p in result:
            if result[p] != w:
                print(False)
                break
        
        else:
            if w in result.values():
                print(False)
                break
            result[p] = w

    
    else:
        print(True)
