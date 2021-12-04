
def main():
    with open("input.txt","r") as fp:
        list0 = fp.read().splitlines()
        lineLen = len(list0[0])
        list1 = list0
        for i in range(lineLen):
            #print(len(list0))
            #print(len(list1))
            if len(list0) > 1:
                list0= partO(list0,i)
            if len(list1) > 1:
                list1= partC(list1,i)
            #print(list0[0])
            print(len(list0))
            print(len(list1))
        print(list0)
        print(int(list0[0], 2))
        print(list1)
        print(int(list1[0], 2))
        o=int(list0[0], 2)
        c=int(list1[0], 2)
        print(o*c)

def partO(listx,col):
    listA = []
    listB = []
    for j in listx:
        if j[col] == '1':
            listA.append(j)
        else:
            listB.append(j)
    if len(listA) >= len(listB):
        return listA
    else:
        return listB

def partC(listx,col):
    listA = []
    listB = []
    for j in listx:
        if j[col] == '1':
            listA.append(j)
        else:
            listB.append(j)
    if len(listA) < len(listB):
        return listA
    else:
        return listB


if __name__ == "__main__":
    main()