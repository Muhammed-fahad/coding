import random

numbers = {1:[0,0], 2:[0,1] , 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2]}

def showbord(xo):  
  for i in range(3):
    for j in range(3):
      print(f"| {xo[i][j]} |", end="")
    print("")

def check(xo):
  for i in range(3): 
    if (xo[i][0] == xo[i][1] == xo[i][2]):
      return True
    
    elif xo[0][i] == xo[1][i] == xo[2][i]:
      return True
  
  if xo[0][0] == xo[1][1] == xo[2][2]:
    return True
  
  elif xo[0][2] == xo [1][1] == xo[2][0]:
    return True

  return False
    
  

def playwithfriends(xo):
  showbord(xo)
  
  while(True):
    n = int(input("Enter a number player 1 , X: "))
    n1 , n2 = numbers[n][0] , numbers[n][1]

    while(xo[n1][n2] == 'X' or xo[n1][n2] == 'O'):
      print("\nThe number is already occupied , Enter other number")
      n = int(input("Enter a number player 1 , X: "))
      n1 , n2 = numbers[n][0] , numbers[n][1]

    xo[n1][n2] = 'X'
    showbord(xo)
    
    if(check(xo)):
      print("\nPlayer 1 wins")
      return
    
    v = int(input("Enter a number player 2 , 0: "))
    v1 , v2 = numbers[v][0] , numbers[v][1]

    while(xo[v1][v2] == 'X' or xo[v1][v2] == 'O'):
      print("\nThe number is already occupied , Enter other number")
      v = int(input("Enter a number player 1 , X: "))
      v1 , v2 = numbers[n][0] , numbers[n][1]
      
    xo[v1][v2] = 'O'
    showbord(xo)
    
    if(check(xo)):
      print("\nplayer 2 wins")
      return
  


def playwithcomputer(xo):
  values = [1,2,3,4,5,6,7,8,9]
  while(True):
    n = int(input("Enter a number player 1 , X: "))
    n1 , n2 = numbers[n][0] , numbers[n][1]

    while(xo[n1][n2] == 'X' or xo[n1][n2] == 'O'):
      print("\nThe number is already occupied , Enter other number")
      n = int(input("Enter a number player 1 , X: "))
      n1 , n2 = numbers[n][0] , numbers[n][1]
      showbord(xo)

    xo[n1][n2] = 'X'
    values.remove(n)
    
    if(check(xo)):
      print("\nPlayer 1 wins")
      return
    
    v = random.choice(values)
    v1 , v2 = numbers[v][0] , numbers[v][1]
    xo[v1][v2] = 'O'
    showbord(xo)
    
    if(check(xo)):
      print("\nplayer computer wins")
      return
    


def main():
  print("Press 1 To play with friends")
  print("press 2 to play with computer")
  
  val = int(input("Enter the value: "))  
  xo = [[1,2,3],[4,5,6],[7,8,9]]
  
  if val == 1:
    playwithfriends(xo)
  
  elif val == 2:
    playwithcomputer(xo)
  
  else:
    print("You Enter a wrong option")
    

if __name__ == "__main__":
  main()