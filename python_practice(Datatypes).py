# Number in strings can be converted into float and integer
x = "35"
print(float(x))  
print(int(x))

# Finding Substring
name = "my name is aditi rathi" 
 # It return boolean expression. to verify that substring is present in a single line.
print("aditi" in name)
print("mca" in name)

# Generally we don't use more than 79 characters in string.
# so, there are two ways to do that
# 1. using back slash(\), and second is using """___"""

s = "This is a String."
print(s.startswith("This"))
print(s.endswith("log"))
print("this".replace("is", "at"))


# Perfoming Two functions in single line

string = "This a PYthON coDE. UPLOAd in GitHUb."
print(string.lower().find("github"))

# Joining characters in array

array = ["a", "b", "c"]
print(''.join(array))
print('+'.join(array))

# List
my_list = [1,67,"aditi", "python", 2.54, True]
print(67 in my_list)
my_list +="noida"  # This case add noida by add every single charcter one by one in list.
print(my_list)

# But if we want to add a complete word. we need to make another dictonary

city = ["noida"]
print(my_list + city)


list = [1,2,3,4]*3   # It doesn't multiply by 3 each individual number. but repeat every number three times.
print(list)


# Remove opreator

my_list.remove("o")  # Note: Remove opreator can remove the first element it finds that matches, not all of them.
print(my_list)

# Delete opreator

del my_list[1]   # Note2: if we want to delete element from list by thier index number. then, we used del opreator
print(my_list)


# pop opreator

my_list.pop()   # Using, pop is when we want to delete by index number. and when no index number is given. then delete last element
print(my_list)


# Append opreator

my_list.append(78)  # When we want to add elements in last of list
print(my_list)

my_list.insert(0,10) # When want to add elements index wise.


