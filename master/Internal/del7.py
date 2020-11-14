# 1 ----------------------------------------------------------
d1 = open("d1.txt", "r+").readlines()

templen = 0
lineno = 0

for i in d1:
    if len(i) > templen:
        templen = len(i)
        lineno = (d1.index(i))

print("Longest line with length: ", templen)
print("Line number: ", lineno + 1)
print("Line: ", d1[lineno])