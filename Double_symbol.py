#DOUBLE FIND THE COMMON SYMBOL



import random
import string
symbol=[]
symbol=list(string.ascii_letters)
card1=[0]*8
card2=[0]*8
pos1=random.randint(0,7)
pos2=random.randint(0,7)
same=random.choice(symbol)
symbol.remove(same)
if pos1==pos2:
    card1[pos1]=same
    card2[pos1]=same
else:
    card1[pos1]=same
    card2[pos2]=same
    card1[pos2]=random.choice(symbol)
    symbol.remove(card1[pos2])
    card2[pos1]=random.choice(symbol)
    symbol.remove(card2[pos1])

i=0
while i<8:
    if (i!=pos1 and i!=pos2):
        card1[i]=random.choice(symbol)
        symbol.remove(card1[i])
        card2[i]=random.choice(symbol)
        symbol.remove(card2[i])
    i+=1

print(card1,"\n")
print(card2)
ch=input("Enter the common symbol:")
if (ch==same):
    print("****Correct answer you won****")
else:
    print("OOPS(';') Better Luck Next Time")
