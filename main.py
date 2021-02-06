#Welcom to my tic tac toe
import random
print("tic tac toe")
print("built by Hassan Ammar")
print("#"*45)
ha = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
winChance = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6]
]

listname = [1,2,3,4,5,6,7,8,9]

def print_shape():
    print(f"{ha[:3]} \n {ha[3:6]} \n {ha[6:]}")

def is_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

my_turn=True

def x_round (x):
    if x in listname and ha[x-1] not in ['x','o'] : 
        ha[x-1] = "x"
        listname.remove(x)
        global my_turn
        my_turn = not my_turn
        return 1
    else : 
        print("pleas enter number not played with")
def y_round():
    index = random.randint(0,len(listname)-1)
    ha[listname[index]-1]='o'
    listname.pop(index)
    global my_turn
    my_turn = not my_turn

def win_los_draw():
    for chances in winChance :
        if ha[chances[0]]==ha[chances[1]]==ha[chances[2]] :
            return ha[chances[0]]
    if len(listname) == 0 :
        return 0  
    return 1

while True:
    if my_turn:
        print_shape()
        while True:
            x = input("your tern enter number from 1 to 9:")
            if not (is_int(x)):
                print("pleas enter number")
            else:
                x = int(x)
                print(f"listname befor x_round {listname}")
                t=x_round(x)
                if t ==1:
                    break
                x_round(x)
    elif listname !=[] :
        y_round()

    state= win_los_draw()
    if state == "x" or state == "o" :
        if state == "x":
            print_shape()
            print("you win")
            break
        elif state == "o" :
            print_shape()
            print("you lost")
            print(f"player {state} is the winner")
            break

    elif state == 0 :
        print_shape()
        print("draw")
        break 


