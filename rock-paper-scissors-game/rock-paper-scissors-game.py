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

game_replies = [rock, paper, scissors]
reply = random.choice(game_replies)

choice = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors. "))

if choice == 0:
    print(rock)
    print("Computer chose:\n", reply)
    if reply == paper :
        print("You win!")
    else :
        print("You lose!")

if choice == 1:
    print(paper)
    print("Computer chose:\n", reply)
    if reply == scissors :
        print("You win!")
    else :
        print("You lose!")

if choice == 2:
    print(scissors)
    print("Computer chose:\n", reply)
    if reply == rock :
        print("You win!")
    else :
        print("You lose!")

else :
    print("You typed an invalid number, You lose!")






