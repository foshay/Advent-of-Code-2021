bigger = 0
depthA = 0
smaller=0
with open("input.txt","r") as fp:
    lines = fp.readlines()
    depthA = int(lines[0])
    for x in range(3,len(lines)):
        #print(depthA)
        #print(lines[x])
        if int(lines[x]) > depthA:
            bigger +=1
        else:
            smaller +=1
        depthA = int(lines[x-2])
        #print(depthA)
print (bigger)
print (bigger+smaller)