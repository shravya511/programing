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
hands = [rock , paper , scissors]
import random
human_hand = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_hand = random.randint(0,2)
if human_hand > 2 or human_hand < 0:
    print("You typed invalid number.")
else:    
    if human_hand == computer_hand:
        print("Your choice")
        print(hands[ human_hand ])
        print("\n Computer's choice")
        print(hands[ computer_hand ])
        print("\n It's a draw.")
    elif human_hand == 0 and computer_hand == 1 or human_hand == 1 and computer_hand == 2 or human_hand == 2 and computer_hand == 0:
        print(f"Your choice {hands[ human_hand ]} Computer's choice {hands[ computer_hand ]}")
        print("\n You loose.")
    else:
        print(f"Your choice {hands[ human_hand ]} Computer's choice {hands[ computer_hand ]}")
        print("\n You win.")