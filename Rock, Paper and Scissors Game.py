import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
game_choice = [rock, paper, scissors]
my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_choice[my_choice])
computer_choice = random.randint(0,2)
print("Computer chose:\n")
print(game_choice[computer_choice])
if my_choice >= 3 or my_choice < 0:
    print("You put an invalid number!")
elif my_choice == 0 and computer_choice == 1:
    print("You lose")
elif my_choice == 0 and computer_choice == 2:
    print("You win")
elif my_choice == 1 and computer_choice == 0:
    print("You win")
elif my_choice == 1 and computer_choice == 2:
    print("You lose")
elif my_choice == 2 and computer_choice == 0:
    print("You lose")
elif my_choice == 2 and computer_choice == 1:
    print("You win")
else:
    print("It is a draw")


