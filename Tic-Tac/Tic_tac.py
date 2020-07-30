#TIC-TAC

board=['_','_','_','_','_','_','_','_','_',]
pp1=[]
pp2=[]
def rules():
    print("Positions:\t  1 | 2 | 3")
    print("\t\t____|___|____")
    print("\t\t  4 | 5 | 6")
    print("\t\t____|___|____")
    print("\t\t  7 | 8 | 9")
    print("\t\t    |   |   ")
def check(pos):
    #Checking Weather the requested place is empty
    if(board[pos-1]=='_'):
        return True
    return False
def won(player):
    print()
    print("\n\n\t\t",player," Won The Match")
def check_row(symbol):
    for i in range (3):
        count=0
        for j in range (3):
            if(board[(3*i)+j]==symbol):
                count+=1
            else:
                break
        if count==3:
            print(i+1,'Row')
            return True
    
    return False

        
def check_column(symbol):
    for i in range (3):
        count=0
        for j in range (3):
            if(board[i+(3*j)]==symbol):
                count+=1
            else:
                break
        if count==3:
            print(i+1,'Column')
            return True
    
    return False

def check_dia(symbol):
    if board[0]==symbol and board[4]==symbol and board[8]==symbol:
        return True
    elif board[2]==symbol and board[4]==symbol and board[6]==symbol:
        return True
    else :
        return False
        
def result(symbol):
    return (check_row(symbol) or check_column(symbol) or check_dia(symbol))
def display():
    print("\t\t ",board[0]," | ",board[1]," | ",board[2],)
    print("\t\t_____|_____|_____")
    print("\t\t ",board[3]," | ",board[4]," | ",board[5],)
    print("\t\t_____|_____|_____")
    print("\t\t ",board[6]," | ",board[7]," | ",board[8],)
    print("\t\t     |     |   ")
    
def play():
    print('*************************************************TIC-TAC*************************************************')
    print('Player 1:" X "')
    print('Player 2:" O "')
    rules()
    print('Enter Names')
    p1=input("Player 1:")
    p2=input("Player 2:")
    turn=0
    while turn<9:
        if turn%2==0:
            #player 1
            print(p1," It's Your Turn:-")
            while 1:
                pos=int(input("Enter the block no."))
                if pos<1 or pos>9:
                    pass
                elif(check(pos)):
                    break
                
                print("Bosdike Dekh k Daal:\tChutiya")
            board[pos-1]='X'
            pp1.append(pos)
            display()
            if (result('X')):
                won(p1)
                break
        else:
            #player 2
            print(p2," It's Your Turn:-")
            while 1:
                pos=int(input("Enter the block no."))
                if pos<1 or pos>9:pass
                elif(check(pos)):
                    break
                
                print("Bosdike Dekh k Daal:\tChutiya")
            board[pos-1]='O'
            pp2.append(pos)
            display()
            if (result('O')):
                won(p2)
                break

        turn+=1
    if turn==10:
        print('************DRAW************')
print(board)              
play()
