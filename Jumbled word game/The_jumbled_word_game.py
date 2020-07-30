import random

def choose():
    word=['random','windows','laptop','brazzers','beach','dubai','russia','canada','india','amazon','audi','microsoft']
    pick=random.choice(word)
    return pick

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled

def thank(p1,p2,pp1,pp2):
    print('\t',p1,' Your score is:',pp1)
    print('\t',p2,' Your score is:',pp2)
    print('********THANKS FOR PLAYING******** ')


def play():
    print('-------------------------------------------Jumbled Word Game-------------------------------------------\n\n\n')
    p1=input("Player 1, Please enter your name:")
    p2=input("Player 2, Please enter your name:")
    pp1=0
    pp2=0
    turn=0
    while(1):
        #computer task
        picked_word=choose()
        question=jumble(picked_word)
        print('Guess the correct word formed by these alphabet:')
        print('\t\t','"',question,'"','\n\n\n')
        if turn%2==0:
            #player 1
            print('\t\t',p1,"It's your turn*")
            ans=input("GUESS THE ANSWER:")
            if ans==picked_word:
                pp1=pp1+1
                print('Correct answer  ')
                print('Your new score:',pp1,'\n\n\n')
            else:
                print('OOPS!!!!!!!!!!! ')
                print('Wrong answer *********')
                print('The correct answer is:','"',picked_word,'"','\n\n\n')
            
        else:
            #player 2
            print(p2,"It's your turn*")
            ans=input("GUESS THE ANSWER:")
            if ans==picked_word:
                pp2=pp2+1
                print('Correct answer  ')
                print('Your new score:',pp2,'\n\n\n')
            else:
                print('OOPS!!!!!!!!!!! ')
                print('Wrong answer *********')
                print('The correct answer is:','"',picked_word,'"','\n\n\n')
        turn=turn+1
        print('PRESS 1 to continue ')
        print('PRESS 0 to END')
        l=int(input('Enter your choice:'))
        if l==0:
            thank(p1,p2,pp1,pp2)
            break;

play()
        
        
