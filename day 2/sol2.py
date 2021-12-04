posX = 0
posY = 0
aim = 0
with open("input.txt","r") as fp:
    lines = fp.readlines()
    for x in lines:
        command, amount = x.split(' ')
        if command == 'forward':
            posX += int(amount)
            posY += int(amount)*aim
        elif command == 'down':
            aim += int(amount)
        elif command == 'up':
            aim -= int(amount)
    print(posX*posY)