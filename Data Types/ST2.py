
s = "Prevention is better"
words = s.split()
words[2] = words[2][::-1]  # reverse "better"
print(" ".join(words))