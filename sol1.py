bigger = 0
smaller = 0
currentDepth = 0
with open("input.txt","r") as fp:
    currentDepth = int(fp.readline())
    lines = fp.readlines()
    for x in lines:
        if int(x) > currentDepth:
            bigger +=1
        else:
            smaller+=1
        currentDepth = int(x)
print (bigger)
print(smaller)