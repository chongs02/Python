
import string
words = str(input())
word = words.split()

w = []
for s in word:
    w.append(s.strip(string.punctuation))

print(w.count('the'))

