import random 
# rock = 1, paper = 2, scissors = 3
computeranswer = random.randint(1,3)
useranswer = int(input("Choose rock, paper, or scissors"))
print(computeranswer)
if computeranswer == 1 and useranswer == 3:
    print("Computer Wins")
if computeranswer == 3 and useranswer == 1:
    print("You Win")
if computeranswer == 1 and useranswer == 1:
    print("Tie")
if computeranswer == 2 and useranswer == 2:
    print("Tie")
if computeranswer == 3 and useranswer == 3:
    print("Tie")
if computeranswer == 2 and useranswer == 3:
    print("You Win")
if computeranswer == 2 and useranswer == 1:
    print("Computer Wins")
if computeranswer == 3 and useranswer == 2:
    print("Computer Wins")
if computeranswer == 1 and useranswer == 2:
    print("You Win")
