#3 Unknown Bags
import random
bag=['A','B','C']
temp=bag
Candi=random.choice(bag)
bag.remove(Candi)
#print(bag,Candi)
print("One Of The Boxes Has A Candi.")
print("BOXES:\tA\tB\tC")
print('Choose any 1 box from above:')
t=input()
if (t!=Candi):
    bag.remove(t)
l=random.choice(bag)
print('HINT: BOX ',l,"Does't have a Candi")
m=input('PRESS 1 to Swap the Selected Box or PRESS 2 to Confirm:')
if m=='1':
    print('Your Choice has been Swaped ')
    if t==Candi:
        
        print('You Loss Motherfucker:')
    else:
        print('Congratulation You Found the Candi\n Now Fuck Your Self')
if t==Candi:
    print('Congratulation You Found the Candi\n Now Fuck Your Self')
else:
    print('You Loss Motherfucker:')


print('Box:',Candi,'Had The Candi')
        

