import random
from time import sleep
board=["-","-","-","-","-","-","-","-","-"]
def create_board():
    print(board[0],"|",board[1],"|",board[2])
    print(board[3],"|",board[4],"|",board[5])
    print(board[6],"|",board[7],"|",board[8])
current_player="x"
winner=None
def flip_player():
    global current_player
    if current_player=="x":
        current_player="o"
    elif current_player=="o":
        current_player="x"



def check_row():
    global s
    r1=board[0]==board[1]==board[2]!="-"
    r2=board[3]==board[4]==board[5]!="-"
    r3=board[6]==board[7]==board[8]!="-"
    if r1 or r2 or r3:
        s=False

    if r1:
        return board[0]
    if r2:
        return board[3]
    if r3:
        return board[6]
    

def check_col():
    global s
    r1=board[0]==board[3]==board[6]!="-"
    r2=board[1]==board[4]==board[7]!="-"
    r3=board[2]==board[5]==board[8]!="-"
    if r1 or r2 or r3:
        s=False
    if r1:
        return board[0]
    if r2:
        return board[1]
    if r3:
        return board[2]
   
def check_diag():
    global s
    r1=board[0]==board[4]==board[8]!="-"
    r2=board[2]==board[4]==board[6]!="-"
    if r1 or r2:
        s=False
    
    if r1:
        return board[0]
    if r2:
        return board[2]
    

def check_tie():
    global s
    global winner
    if "-" not in board[0:10] and winner==None:
        winner="tt"
        s=False
        print("tie")
        
    




        
def check_w():
    global winner
    row=check_row()
    col=check_col()
    diagonal=check_diag()
    if row:
        winner=row
        print(winner," wins")
    if col:
        winner=col
        print(winner," wins")
    if diagonal:
        winner=diagonal
        print(winner," wins")
    
        
        


def check():
    check_w()
    check_tie()
def handle(current_player):
    validate=False
    print(current_player," turns")
    pos=input("Enter choice from 1-9")
    
    print("enternumber:",pos)
     
    while not validate:
        
        while pos not in ["1","2","3","4","5","6","7","8","9"]:
             pos=input("enter valid number a:")
        
        pos=int(pos)-1
        if board[pos]=="-":
            validate=True
        else:
            print("you can't go there")
    board[pos]=current_player
    create_board()


        

def comp_player(current_player):
    validate=False
    print(current_player," turns")
    pos=random.randint(1,9)
    sleep(0.2)
    print("enternumber:",pos)
     
    while not validate:
        
        
        
        pos=pos-1
        if board[pos]=="-":
            validate=True
        else:
            print("you can't go there")
            pos=random.randint(1,9)
            print("enter number:",pos)
    board[pos]=current_player
    create_board()
    
s=True
print("Enter 1 for 2 player")
print("Enter 2 for 1 player ")
ch=int(input("Enter choice"))
if ch==1:
    while s:
        handle(current_player)
        check()
        flip_player()
elif ch==2:
    while s:
        if winner=="x" or winner=="0" or winner=="tt":
            break
        handle(current_player)
        check()
        if winner=="x" or winner=="0"or winner=="tt":
            break
        flip_player()
        sleep(0.2)
        comp_player(current_player)
        check()
    
        sleep(0.2)
        flip_player()

else:
    print("wrong option")
    
   

    
            
    
    
    

    
            
    
        

        




