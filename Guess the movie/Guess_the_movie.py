#GUESS THE MOVIE

import random


movie=['Dangal','Baahubali','Secret Superstar','PK','Sultan','Dhoom','Dhoom 2','Dhoom 3','3 Idiots','Sholay','Gangs of Wasseypur','Gangs of Wasseypur 2']
def thank(p1,p2,pp1,pp2):
    print('THANKS FOR PLAYING')
    print('\n\nScore Card:')
    print('1.',p1,'  ',pp1)
    print('2.',p2,'  ',pp2)
def createQ(movie):
    n=len(movie)
    letter=list(movie)
    temp=[]
    for i in range (n):
        if letter[i]==' ':
            temp.append(' ')
        else:
            temp.append('*')
    qn=''.join(str(x) for x in temp)
    return qn
    
def is_present(letter ,movie):
    c=movie.count(letter)
    if c==0:
        return False
    else:
        return True
    

def unlock(qn,movie,letter):
    ref=list(movie)
    qnlist=list(qn)
    temp=[]
    n=len(movie)
    for i in range(n):
        if ref[i]==' ' or ref[i]==letter:
            temp.append(ref[i])
        else:
            if qnlist[i]=='*':
                temp.append('*')
            else:
                temp.append(qnlist[i])
    qn=''.join(str(x) for x in temp)
    return qn

                
        
    
    
def play():
    print('------------------------------------------------GUESS THE MOVIE NAME------------------------------------------------')
    print('Enter Names')
    p1=input("Player 1:")
    p2=input("Player 2:")
    pp1=0
    pp2=0
    turn=0
    while 1:
        if turn%2==0:
            #player 1
            picked_word=random.choice(movie)
            question=createQ(picked_word)
            print('\n\n\t\t\t',p1," It's your turn.")
            print('\n\n\t\t','Guess the movie name:','"',question,'"')
            new_ques=question
            while 1:
                key=input('Which letter do you think:')
                if(is_present(key,picked_word)):
                    #unlock KEY
                    
                    new_ques=unlock(new_ques,picked_word,key)
                    print('\n\n\t\t','Guess the movie now:',new_ques)
                    d=int(input('PRESS 1 to Guess the movie or PRESS 2 to unlock another letter:'))
                    if d==1:
                        ans=input('Your Answer:')
                        if ans==picked_word:
                            pp1+=1
                            print('\n\n\tAbsolutly correct**')
                            print('Your Score:',pp1)
                            break
                        else:
                            print('OOPS Wrong Answer \n Better Luck Next Time')
                            c=input('PRESS 1 to Continue or 0 To Quit:')
                            if c=='0':
                                thank(p1,p2,pp1,pp2)
                                break

                    else:
                        print('Good Luck')
                else:
                    print(key,'Is not present in that movie_name')
            



        else:
            #Player 2
            picked_word=random.choice(movie)
            question=createQ(picked_word)
            print('\n\n\t\t\t',p2," It's your turn.")
            print('\n\n\t\t','Guess the movie name:','"',question,'"')
            new_ques=question
            while 1:
                key=input('Which letter do you think:')
                if(is_present(key,picked_word)):
                    #unlock KEY
                    
                    new_ques=unlock(new_ques,picked_word,key)
                    print('\n\n\t\t','Guess the movie now:',new_ques)
                    d=int(input('PRESS 1 to Guess the movie or PRESS 2 to unlock another letter:'))
                    if d==1:
                        ans=input('Your Answer:')
                        if ans==picked_word:
                            pp2+=1
                            print('\n\n\tAbsolutly correct**')
                            print('Your Score:',pp2)
                            break
                        else:
                            print('OOPS Wrong Answer \n Better Luck Next Time')
                            c=input('PRESS 1 to Continue or 0 To Quit:')
                            if c=='0':
                                thank(p1,p2,pp1,pp2)
                                break
                    else:
                        print('Good Luck')
                else:
                    print(key,'Is not present in that movie_name')
            

        turn+=1


play()   
