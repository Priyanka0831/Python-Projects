//Rock,Paper,Scissor Game in Python
import random

def game(computer,user):
    if computer == user:
        return None
    elif computer == 'r':
        if user == 'p':
            return True
        elif user == 's':
            return False
    elif computer == 'p':
        if user == 's':
            return True
        elif user == 'r':
            return False
    elif computer == 's':
        if user == 'r':
            return True
        elif user == 'p':
            return False
            
print("Computer Turn: Rock(r) or Paper(p) or Scissor(s)?")
randomNo = random.randint(1,3)
if randomNo == 1:
    computer = 'r'
elif randomNo == 2:
    computer = 'p'
elif randomNo == 3:
    computer = 's'

user = input("Your Turn: Rock(r) or Paper(p) or Scissor(s)?")
a =game(computer,user)

print(f"Computer Chose {computer}")
print(f"You Chose {user}")

if a == None:
    print("This game is a tie!")
elif a:
    print("You Win!")
else: 
    print("You Lose!")
