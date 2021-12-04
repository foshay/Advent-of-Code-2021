posX = 0
posY = 0
with open("input.txt","r") as fp:
    lines = fp.readlines()
    for x in lines:
        command, amount = x.split(' ')
        if command == 'forward':
            posX += int(amount)
        elif command == 'down':
            posY += int(amount)
        elif command == 'up':
            posY -= int(amount)
    print(posX*posY)