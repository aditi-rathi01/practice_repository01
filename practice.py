# Problem: You are given a string s and an array of strings words. All the strings of words are of the same length.

# A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

#For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" 
# are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.

# Example 1:

# Input: s = "barfoothefoobarman", words = ["foo","bar"]

# Output: [0,9]

# Example 2:

# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

# Output: []

# Explanation:

# There is no concatenated substring.



# Solution: 

# Core Idea: Because all words have the same length, we silde the window word-by-word, not charcter-by-character.

# Window:- Window is moving continous part. which move according to given step size.(strings)

# ----- Logic Step-by-step -----

# 1.) Every word have a common length which is "word_len" that's why we are going to check string from different different points
# So, that words cannot break.(0,3,6....), (1,4,7....),(2,5,8.....)

# 2.) Windows are adjust in a way that only valid words are allowed. and valid words are not exclude more than limit.(Where is Window)

# 3.) (What is inside the window and how many times it appers).

# 4.) In Inside the window:
#     - When every valid word appear. with exact number of words(word count is right)
#     - Then, we storing index of starting window.



# -------- Now, Writting The CODE ------

s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]

word_len = len(words[0])
word_count = len(words)

total_len = word_len * word_count

# Going to know valid words and  Counting of valid words.
words_map = {}                           # It's a fix dictionary.
for w in words:
    words_map[w] = words_map.get(w, 0) + 1

    result = []

# Now, we are going to check the word inside the string. with the given interval step: here word_len = 3
    for offset in range(word_len):            # We are move word by word. so'that word cannot be break.

        left = offset                 # Start word aligment from the most starting.(If offset = 1, Starting from 1 character.)
        right = offset                # At how far, window will expand?
        seen = {}                     # Seen dictionary used for live status. it's change according to window.
        count = 0

# left -> Start of window
# right -> End of window.

        while right + word_len <= len(s):             # (right + 3 <= 18) yes, valid.[right only moves when getting complete word]
            word = s[right: right + word_len]          # word = s[0:3], s[3:6], s[6:9]
            right += word_len                         

            if word in words_map:
                seen[word] = seen.get(word,0)+1

                count +=1

                while seen[word] > words_map[word]:             # If a word apperas more than allowed times then, we have to remove
                    left_word = s[left:left + word_len]         # Which word going to remove.
                    seen[left_word] -= 1                        # reduce the count of that word. 
                    left += word_len                            # Move forward of left. 

                    count -=1                                   # Count tell's how many word we get at window.

                if count == word_count:
                        result.append(left)                     # left is start of window.
            
            else:
                seen.clear()
                count = 0
                left = right
    
print(result)


# ----- Summary -------

# PROBLEM: we have to find the continous word from the string. which contains words form list exactly ones.


# Core Idea: 
 
# Every word have same lenght
# we have to check the string in small windows.
# window will move from left to right.


# VARIABLES:


# left : Starting point of left.
# right: Ending side of window.
# word_map: How many time a word will appear.
# seen : Right now, which word found at how many time.
# count : How many valid words match till now.



# FLOW OF CODE : 


# *** first while loop:****  while right + word_len <= len(s):
# run until you can get complete word. from right. for example:
# s = "barfoothe"
# len(s) = 9, lenght of every word = 3
# right = 0, 0 +3 <=9 (valid)  "bar" -> loop will run
# right = 3 , 3 +3 <=9 (valide) "foo"  -> loop will run

# Take out word: word = s[right:right + word_len]
# taking word from right. why? to check from sequence taking word from right is mandatory.
# right  word
# 0      bar
# 3      foo
# 6      the


# Word is in list:
# if word in words_map:
# seen[word] +=1
# count +=1

# alloted more than allowed time:
# while seen[word] > words_map[word]: 
# removing word form left


