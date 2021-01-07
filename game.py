import random
print("\tSnake, Water and Gun")
r = random.randint(1,3)
if r==1:
    comp = 's'
elif r==2:
    comp = 'w'
elif r==3:
    comp = 'g'

user = input("Your turn: type s for snake, g for gun, w for water \n")
def result(comp,user):
    if comp==user:
        return None
    elif comp=='s':
        if user=='g':
            return True
        elif user=='w':
            return False
    elif comp=='w':
        if user=='s':
            return True
        elif user=='g':
            return False
    elif comp=='g':
        if user=='w':
            return True
        elif user=='s':
            return False   

print("Computer's turn: s for snake, g for gun, w for water ")
print(comp)
rst=result(comp,user)

if rst==True:
    print("You Win\n")
elif rst==False:
    print("You Lose\n")
elif rst==None:
    print("Draw\n")
