import random

user_wins = 0
computer_wins = 0

optionsuser = ["r", "p", "s"]
optionscpu = ["rock", "paper", "scissors"]


while True:
    user_input = input("Type R for Rock/ P for Paper/ S for Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in optionsuser:
        continue

    if user_input == "r" :     
        random_number = random.randint(1, 2)
        # rock: 0, paper: 1, scissors: 2
        computer_pick = optionscpu[random_number]
    if user_input == "s" :    
        random_number = random.randint(0, 1)
        # rock: 0, paper: 1, scissors: 2
        computer_pick = optionscpu[random_number]
    if user_input == "p" :    
        random_number = random.randint(0, 2)
        # rock: 0, paper: 1, scissors: 2
        computer_pick = optionscpu[random_number]
    if user_input == "p" and computer_pick == "paper":
        random_number = random.randint(0, 1)
        # rock: 0, paper: 1, scissors: 2
        if random_number == 0 :
            computer_pick = optionscpu[random_number]
        else :
            computer_pick = "scissors"

    print("Computer picked", computer_pick + ".")

    if user_input == "r" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "p" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "s" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    
    elif user_input == "r" and computer_pick == "rock":
        print("Mesma escolha, sem ganhador!")
        
    elif user_input == "p" and computer_pick == "paper":
        print("Mesma escolha, sem ganhador!")

    elif user_input == "s" and computer_pick == "scissors":
        print("Mesma escolha, sem ganhador!")

    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")