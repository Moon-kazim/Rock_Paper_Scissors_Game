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
print("Welcome To Rock, Paper and Scissors game")
import random
# image = [rock, paper, scissors]
random_numb = random.randint(0,2)
# 0 == rock
# 1 == paper
# 2 == scissors
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

# print(f"Computer Choice: {random_numb}")

#stone
if choice == 0 and random_numb == 2:
    print("Your Choice: rock")
    print(rock)
    print("Computer Choice: scissors")
    print(scissors)
    print("You Win!!")
elif choice == 0 and random_numb == 1:
    print("Your Choice: rock")
    print(rock)
    print("Computer Choice: paper")
    print(paper)
    print("You Lost!!")

#paper
elif choice == 1 and random_numb == 0:
    print("Your Choice: paper")
    print(paper)
    print("Computer Choice: rock")
    print(rock)
    print("You Win!!")
elif choice == 1 and random_numb == 2:
    print("Your Choice: paper")
    print(paper)
    print("Computer Choice: scissors")
    print(scissors)
    print("You Lost!!")

#scissors
elif choice == 2 and random_numb == 1:
    print("Your Choice: scissors")
    print(scissors)
    print("Computer Choice: paper")
    print(paper)
    print("You Win!!")
elif choice == 2 and random_numb == 0:
    print("Your Choice: scissors")
    print(scissors)
    print("Computer Choice: stone")
    print(rock)
    print("You Lost!!")

#Draw
elif choice == random_numb:
    print(f"Your Choice: {choice}")
    print(f"Computer Choice: {random_numb}")
    print("DRAW!!")

#invalid entery    
else:
    print("invalid number")
