# Problem: Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the
# order of characters. No two characters may map to the same character, but a character may
# map to itself.

# Example 1:

# Input: s = "egg", t = "add"
# Output: true

# Explanation:

# The strings s and t can be made identical by:

# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.

# Example 2:

# Input: s = "f11", t = "b23"

# Output: false


s = "f11"
t = "b23"


# NOTE: Positions matters in isormphic string.
#       s[0] -> t[0]
#       s[1] -> t[1]
#       s[2] -> t[2]

if len(s) != len(t):
    print(False)
else:

    map_st = {}
    map_ts = {}
    is_isomrphic = True
    
    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]

        # checks s -> t

        if char_s in map_st:
            if map_st[char_s] != char_t:
                is_isomrphic = False

                break

        else:
            map_st[char_s] = char_t

        # checks t -> s mapping

        if char_t in map_ts:
            if map_ts[char_t] != char_s:
                is_isomrphic = False
                break 
        
        else:

            map_ts[char_t] = char_s
    
    print(is_isomrphic)


# NOTE: Why Reverse Mapping Is Important?

# because we must ensure one-to-one mapping.

# That means:
# One letter in s -> Only one letter in t
# one letter in t -> Only one letter in s

s = "ab"
t = "aa"

# Here, {"a": "a"} 
# and {"b": "a"}

# Now, check is "b" already in dictionary? NO.
# So, that's Why reversing is important.

# {"a": "a"}
# and {"a":"b"}, Now a is already present in dictionary. So, it doesn't map again to "b". when once already map to "a".





