import random
import time

g = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]


def block(b):
    index = {
        1: [0, 0],
        2: [0, 1],
        3: [0, 2],
        4: [1, 0],
        5: [1, 1],
        6: [1, 2],
        7: [2, 0],
        8: [2, 1],
        9: [2, 2]
    }

    if g[index[b][0]][index[b][1]] != "O" and g[index[b][0]][index[b][1]]!= "X":
        g[index[b][0]][index[b][1]] = "X"
        return True
    else:
        return False
       
def bot():
    take_place = False
    #Easy Mode
    while take_place != True:
        a = random.randint(0,2)
        b = random.randint(0,2)

        if g[a][b] != "X" and g[a][b] != "O":
            g[a][b] = "O"
            take_place = True
        else:
            take_place = False    

def third(ct):
    for num in "123456789":
        if num in ct:
            match num:
                case "1":
                    g[0][0] = "O"
                case "2":
                    g[0][1] = "O"
                case "3":
                    g[0][2] = "O"
                case "4":
                    g[1][0] = "O"
                case "5":
                    g[1][1] = "O"
                case "6":
                    g[1][2] = "O"
                case "7":
                    g[2][0] = "O"
                case "8":
                    g[2][1] = "O"
                case "9":
                    g[2][2] = "O"

def bot_hard():
    #Hard Mode
    Xs = [
        g[0][:],
        g[1][:],
        g[2][:],
        [g[0][0], g[1][0], g[2][0]],
        [g[0][1], g[1][1], g[2][1]],
        [g[0][2], g[1][2], g[2][2]],
        [g[0][0], g[1][1], g[2][2]],
        [g[0][2], g[1][1], g[2][0]]
    ]

    isPlayed = False
    for ct in Xs:
        if ct.count("O") == 2 and ct.count("X") == 0:
            third(ct)
            isPlayed = True
            break
        elif ct.count("X") == 2 and ct.count("O") == 0:
            third(ct)
            isPlayed = True
            break
        else:
            isPlayed = False

    if isPlayed == False:   
        if g[1][1] != "X" and g[1][1] != "O":
            g[1][1] = "O"
        else:
            c = []
            for j in range(0,3,2):
                for jj in range(0,3,2):
                    if g[j][jj] != "X" and g[j][jj] != "O":
                        c.append(g[j][jj])
                    else:
                        pass 

            if len(c) > 0:
                match random.choice(c):
                    case "1":
                        g[0][0] = "O"
                    case "3":
                        g[0][2] = "O"
                    case "7":
                        g[2][0] = "O"
                    case "9":
                        g[2][2] = "O"
            else:
                bot()

def draw():
    w = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

    for d in range(0,3):
        for dd in range(0,3):
            if g[d][dd] == "X" or g[d][dd] == "O":
                w[d][dd] = g[d][dd]

    print(f"  {w[0][0]}  |  {w[0][1]}  |  {w[0][2]}  \n-----------------\n  {w[1][0]}  |  {w[1][1]}  |  {w[1][2]}  \n-----------------\n  {w[2][0]}  |  {w[2][1]}  |  {w[2][2]}  \n")               


run = False
mode = int(input("Choose the mode of game (1) for easy mode and (2) for hard mode: "))
if 0 >= mode or mode >= 3:
    print("\nYou should enter (1) or (2):\n1 => Easy Mode\n2 => Hard Mode\n\n**Please run the code again!**")
    run = False
else:
    print("\nSTART!!\n")
    run = True


win = ""
rounds = 0
while win == "":

    if run == False:
        break
    else:
        pass

    print("Your turn!")
    x = int(input("Choose your block: "))
    if block(x) == False:
        print("**You choosed a taken block**")
        continue
    else:
        block(x)
    draw()

    time.sleep(0.5)
    print("Bot\'s turn!")
    match mode:
        case 1:
            bot()
        case 2:
            bot_hard()
    draw()

    win_x = ""
    win_y = ""
    win_z1 = ""
    win_z2 = ""
    for i in range(0,3):
        win_z1 += g[i][i]
        for j in range(0,3):
            win_x += g[i][j]
            win_y += g[j][i]
            win_z2 += g[i][2-i]

        if win_x[-3:] == "XXX" or win_x[-3:] == "OOO":
            win = win_x[-1]
            break
        elif win_y[-3:] == "XXX" or win_y[-3:] == "OOO":
            win = win_y[-1]
            break
        elif win_z1[-3:] == "XXX" or win_z1[-3:] == "OOO":
            win = win_z1[-1]
            break
        elif win_z2[:] == "X"*9 or win_z2[:] == "O"*9:
            win = win_z2[-1]
            break
    
    rounds += 2
    if rounds >= 8:
        match win:
            case "X":
                print("Yay! You Won 🥳")
                break
            case "O":
                print("Opps! You Lost 😓")
                break
            case _:
                print("Draw! 🤔")
                break
    else:
        match win:
            case "X":
                print("Yay! You Won 🥳")
                break
            case "O":
                print("Opps! You Lost 😓")
                break
