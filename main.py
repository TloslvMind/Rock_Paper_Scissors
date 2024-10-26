from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

flag = True

while flag:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))
    comp_choice = randint(0, 2)
    if user_choice != comp_choice and 0 <= user_choice <= 2:
        flag = False
    if user_choice == 0:
        print(f"You chose rock: {rock}")
        if comp_choice == 0:
            print(f"Computer also chose rock: {rock}")
            print("\n        Draw! Let's play again!")
        elif comp_choice == 1:
            print(f"Computer chose paper: {paper}")
            print("\n        You lose!")
        elif comp_choice == 2:
            print(f"Computer chose scissors: {scissors}")
            print("\n        You win!")
    elif user_choice == 1:
        print(f"You chose paper: {paper}")
        if comp_choice == 0:
            print(f"Computer chose rock: {rock}")
            print("\n        You win!")
        elif comp_choice == 1:
            print(f"Computer also chose paper: {paper}")
            print("\n        Draw! Let's play again!")
        elif comp_choice == 2:
            print(f"Computer chose scissors: {scissors}")
            print("\n        You lose!")
    elif user_choice == 2:
        print(f"You chose scissors: {scissors}")
        if comp_choice == 0:
            print(f"Computer chose rock: {rock}")
            print("\n        You lose!")
        elif comp_choice == 1:
            print(f"Computer chose paper: {paper}")
            print("\n        You win!")
        elif comp_choice == 2:
            print(f"Computer also chose scissors: {scissors}")
            print("\n        Draw! Let's play again!")
    else:
        print("Invalid number. Try again.")
        continue