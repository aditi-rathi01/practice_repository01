import string 

text = "my name is aditi rathi. aditi rathi wants to  learn data science. full name of aditi is aditi rathi"

text = text.lower()

for p in string.punctuation:
    text = text.replace(p, "")

words = text.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)
    