val = [0] * 12
rows = 0
g = 0
e = 0
with open("input.txt","r") as fp:
    lines = fp.read().splitlines()
    for x in lines:
        for i in range(len(x)):
            val[i]+=int(x[i])
        rows+=1
valLen = len(val)
for i in range(valLen):
    if val[i] > 500:
        g+=pow(2,valLen-1-i)
    else:
        e+=pow(2,valLen-1-i)
print(g*e)
        