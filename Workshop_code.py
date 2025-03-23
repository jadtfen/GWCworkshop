#First part 5-7 min
#create  print statements for you rock paper Scissors game
print(" Welcome to Rock, Paper, Scissors!")
print("Let's play a fun game against the computer ")

#Second part 5-7 min 
#set user input to which one they will choose
# .lower can be changed if any other function ways since this is just taking in the string and returning it as a prefrence as lower  
user_choice = input("Choose rock, paper, or scissors: ").lower()

#Third part 5-7 min 
# we can move this to the top if needed but I put it here for nwo to show the steps of needeing to access it 
import random
#allows for the computer to be able to choose randomly form our options 

choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)

print(f"The computer chose: {computer_choice}")


# if elif and else statements to show the output of the computer_choice and user_choice
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("You win! Rock crushes scissors.")
    else:
        print("You lose! Paper covers rock.")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("You win! Paper covers rock.")
    else:
        print("You lose! Scissors cut paper.")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("You win! Scissors cut paper.")
    else:
        print("You lose! Rock crushes scissors.")
else:
    print("Oops! Please choose rock, paper, or scissors next time.")

#If we have time this allows it to return to play again 




"""import random

#def play_game():
    print(" Welcome to Rock, Paper, Scissors!")
    print("Let's play a fun game against the computer🤖")

    options = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()

        if user_choice not in options:
            print(" Invalid choice. Please type rock, paper, or scissors.")
            continue

        computer_choice = random.choice(options)
        print(f"The computer chose: {computer_choice}")

        # Decide the winner
        if user_choice == computer_choice:
            print("It's a tie! ")
        elif user_choice == "rock":
            if computer_choice == "scissors":
                print("You win!  Rock crushes scissors.")
            else:
                print("You lose!  Paper covers rock.")
        elif user_choice == "paper":
            if computer_choice == "rock":
                print("You win! Paper covers rock.")
            else:
                print("You lose!  Scissors cut paper.")
        elif user_choice == "scissors":
            if computer_choice == "paper":
                print("You win!  Scissors cut paper.")
            else:
                print("You lose!  Rock crushes scissors.")

        # Ask to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! See you next time!")
            break

# Start the game
play_game()"
"""