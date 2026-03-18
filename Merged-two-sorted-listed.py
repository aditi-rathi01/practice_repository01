# Program : You are given the heads of two sorted linked lists list1 and list2.
#          Merge the two lists into one sorted list. The list should be made by splicing together 
#          the nodes of the first two lists.

# Return the head of the merged linked list.


# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2: 
# Input list1 = [0], list2 = []
# Output: [0]

# Example 3: 
# Input list1 = [], list2 = []
# Ouput: []

list1 = []
list2 = [0]

l = list1 + list2

s = sorted(l)
print(s)



# NOTE: 
# when, doing it in leetcode these are not list they worked as linked list.
# Now, 
# 1.) Convert them -> Python list
# 2.) Merge Using +
# 3.) Sort
# 4.) Covert back -> linked list.

