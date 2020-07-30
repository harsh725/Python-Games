#SNAKES & LADDERS
import random
import Image

def dipaly():
    img=Image.open('Snake & ladder.jpg')
    img.show()
def snake(points):
    if points==17:
        return 7
    if points==54:
        return 34
    if points==62:
        return 19
    if points==64:
        return 60
    if points==87:
        return 36
    if points==93:
        return 73
    if points==95:
        return 75
    if points==98:
        return 79
def play():
    p1=input('Payer 1, Enter your name: ')
    p2=input('Payer 2, Enter your name: ')
    pp1=0
    pp2=0
    turn=0
    while 1:
        #Player 1
        if turn%2==0:
            print(p1,' Its your turn.')
            t=input('Press Enter to Roll The Dice')
            dice=random.randint(1,6)
            pp1+=dice
            pp1=snake(pp1)
            pp1=ladder(pp1)
            while dice==6:
                print("Wow It's a 6 You Got Anothet Chance")
                t=input('Press Enter to Roll The Dice')
                dice=random.randint(1,6)
                pp1+=dice
                pp1=snake(pp1)
                pp1=ladder(pp1)


        #Player 2
        else:
            print(p2,' Its your turn.')
            t=input('Press Enter to Roll The Dice')
            dice=random.randint(1,6)
            pp2+=dice
            pp2=snake(pp2)
            pp2=ladder(pp2)
            while dice==6:
                print("Wow It's a 6 You Got Anothet Chance")
                t=input('Press Enter to Roll The Dice')
                dice=random.randint(1,6)
                pp2+=dice
                pp2=snake(pp2)
                pp2=ladder(pp2)
        turn+=1

t=input("PRESS ANY KEY TO START")
play()
        
