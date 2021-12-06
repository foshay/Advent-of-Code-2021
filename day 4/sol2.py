import numpy
def main():
    
    with open("input.txt","r") as fp:
        numbs = fp.readline().split(',')
        _ = fp.readline()
        list0 = fp.read().splitlines()
        #boards = [[[0]*5]*5]*len(list0)
        boards = numpy.zeros((100,5,5))
        #print(boards[0][0][0])
        row=0
        boardnum=0
        for x in range(len(list0)):
            row %= 5
            if len(list0[x]) != 0:
                col = 0
                for y in range(0, len(list0[x]), 3):
                    #print(list0[x][y:y+2])
                    if list0[x][y] == ' ': 
                        boards[boardnum][row][col] = int(list0[x][y:y+2].split(" ")[1])
                    else:
                        boards[boardnum][row][col] = int(list0[x][y:y+2])
                    #print("row: " + str(row) + " col: "+ str(col))
                    #print (boards[boardnum])
                    col+=1
                row += 1
            if row == 5:
                #print ("i: " + str(row) + " j: " + str(col) + " board: " + str(boardnum))
                #print(boards[boardnum][0])
                #print(boardnum)
                boardnum+=1
        b = None
        fin = -1
        winners = []
        for n in numbs:
            for i in range(len(boards)):
                if i not in winners:
                    boards[i] = editBoard(boards[i],int(n))
                    if checkBoard(boards[i]):
                        print('found')
                        b = boards[i]
                        fin = n
                        winners.append(i)
                    #print(boards[i])
                    #print(calc(boards[i])*int(n))
        print(b)
        print(calc(b)*int(fin))
        
        #for i in range(len(boards)):
        #    boards[i] = editBoard(boards[i],17)
        #    break
        #print(boards[0])
        return
        if(checkBoard(boards[0])):
            print("found")
        #print(boards)
        #print(numbs)
def calc(board):
    total = 0
    for i in board:
        for j in i:
            #print(int(j))
            if int(j) != -1:
                total+=int(j)
    return total

def editBoard(board,num):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == num:
                print('oop')
                board[i][j] = -1
    return board

def checkBoard(board):
    for i in range(len(board)):
        hits = 0
        for j in range(len(board[i])):
            if board[i][j] == -1:
                hits+=1
            else:
                break
            if hits == 5:
                return 1
    for i in range(len(board[0])):
        hits = 0
        for j in range(len(board)):
            if board[j][i] == -1:
                print("hit")
                hits+=1
            else:
                break
            #print(board[j][i])
            if hits == 5:
                return 1
    return 0
    


if __name__ == "__main__":
    main()

