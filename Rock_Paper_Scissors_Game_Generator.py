print("Welcome To Rock, Paper and Scissors game")
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
#game images
game_images = [rock, paper, scissors]

#input from the user
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n"))
print("")

#indexing of image
if choice >= 0 and choice <=2:
    print("YOU choice")
    print(game_images[choice])
    
    #input from the computer
    random_numb = random.randint(0,2)
    print("Computer Choice:")
    print(game_images[random_numb])

#invalid entery    
if choice >=3 or choice<0:
    print("invalid number enter,\nYOU LOST!!")

#stone
elif choice == 0 and random_numb == 2:
    print("You Win!!")
elif choice == 0 and random_numb == 1:
    print("You Lost!!")

#paper
elif choice == 1 and random_numb == 0:
    print("You Win!!")
elif choice == 1 and random_numb == 2:
    print("You Lost!!")

#scissors
elif choice == 2 and random_numb == 1:
    print("You Win!!")
elif choice == 2 and random_numb == 0:
    print("You Lost!!")

#Draw
elif choice == random_numb:
    print("DRAW!!")



















# #input from the computer
# random_numb = random.randint(0,2)
# # rock == 0
# # paper == 1
# # scissors == 2

# #input from the user
# choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

# # print(f"Computer Choice: {random_numb}")


# #invalid entery    
# if choice >=3 or choice<0:
#     print("invalid number enter,\nYOU LOST!!")

# #stone
# elif choice == 0 and random_numb == 2:
#     print("Your Choice: rock")
#     print(rock)
#     print("Computer Choice: scissors")
#     print(scissors)
#     print("You Win!!")
# elif choice == 0 and random_numb == 1:
#     print("Your Choice: rock")
#     print(rock)
#     print("Computer Choice: paper")
#     print(paper)
#     print("You Lost!!")

# #paper
# elif choice == 1 and random_numb == 0:
#     print("Your Choice: paper")
#     print(paper)
#     print("Computer Choice: rock")
#     print(rock)
#     print("You Win!!")
# elif choice == 1 and random_numb == 2:
#     print("Your Choice: paper")
#     print(paper)
#     print("Computer Choice: scissors")
#     print(scissors)
#     print("You Lost!!")

# #scissors
# elif choice == 2 and random_numb == 1:
#     print("Your Choice: scissors")
#     print(scissors)
#     print("Computer Choice: paper")
#     print(paper)
#     print("You Win!!")
# elif choice == 2 and random_numb == 0:
#     print("Your Choice: scissors")
#     print(scissors)
#     print("Computer Choice: stone")
#     print(rock)
#     print("You Lost!!")

# #Draw
# elif choice == random_numb:
#     print(f"Your Choice: {choice}")
#     print(f"Computer Choice: {random_numb}")
#     print("DRAW!!")

# #invalid entery    
# # else:
# #     print("invalid number")
