import random 
def showbord(xo):
    for i in range(3):
        for j in range(3):
            print(f"| {xo[i][j]} | " , end='')
        print()

numbers = {1:[0,0], 2:[0,1], 3:[0,2] , 4:[1,0] , 5:[1,1] , 6:[1,2] , 7:[2,0], 8:[2,1], 9:[2,2]}
    
def check(xo):
    for i in range(3):
        if xo[i][0] == xo[i][1] == xo[i][2]:
            return True
        elif xo[0][i] == xo[1][i] == xo[2][i]:
            return True

    if xo[0][0] == xo[1][1] == xo[2][2]:
        return True
    elif xo[0][2] == xo[1][1] == xo[2][0]:
        return True

    return False


def playwithfriends(xo):
    showbord(xo)   
    while(True):    
        n = int(input("Enter a number 1-9 player 1 , 0 to break: "))
        if n ==0:
            break
        num_player1 , num_player2 = numbers[n][0] , numbers[n][1]
        
        while (xo[num_player1][num_player2] == 'x' or xo[num_player1][num_player2] =='o'):
            print ("Its already present Enter new value x player 1")
            n = int(input("Enter a number 1-9 player 1, 0 to break: "))
            num_player1 , num_player2 = numbers[n][0] , numbers[n][1]


        xo[num_player1][num_player2] = 'x'
        showbord(xo)
        if(check(xo)):
            print("Game Ended player 1 wins")
            break

        v = int(input("Enter a number 1-9 player 2 , 0 to break: "))
        if v == 0:
            break   
        num_com1 , num_com2 = numbers[v][0] , numbers[v][1]    
    
        while(xo[num_com1][num_com2] == 'x' or xo[num_com1][num_com2] =='o'):
            print ("Already present Enter new number player 2")
            v = int(input("Enter a number 1-9 player 2 , 0 to break: "))
            num_com1 , num_com2 = numbers[v][0] , numbers[v][1]
        
        
        xo[num_com1][num_com2] = 'o'
        showbord(xo)
        if(check(xo)):
            print("Game Ended player 2 wins")
            break


def playwithcomputer(xo):
    showbord(xo)
    k = [1,2,3,4,5,6,7,8,9]
    while(True):        
        n = int(input("Enter a number 1-9 , 0 to break: "))
        if n ==0:
            break
        num_player1 , num_player2 = numbers[n][0] , numbers[n][1]

        while (xo[num_player1][num_player2] == 'x' or xo[num_player1][num_player2] =='o'):
            print ("Its already present Enter new value x player 1")
            n = int(input("Enter a number 1-9 player 1, 0 to break: "))
            num_player1 , num_player2 = numbers[n][0] , numbers[n][1]
                
        xo[num_player1][num_player2] = 'x'
        k.remove(n)
        if(check(xo)):
            showbord(xo)
            print("You win")
            break

        v = random.choice(k)            
        num_com1 , num_com2 = numbers[v][0] , numbers[v][1]
        k.remove(v)
        xo[num_com1][num_com2] = 'o'
        showbord(xo)
        if(check(xo)):
            print("Computer wins")
            break


xo = [[1,2,3],[4,5,6],[7,8,9]]
print("Enter 1 to play with friends: ")
print("Enter 2 to play with computer")
n = int(input("Enter a number: "))
if n == 2:
    playwithcomputer(xo)
elif n ==1:
    playwithfriends(xo)
else:
    print("Wrong choise")