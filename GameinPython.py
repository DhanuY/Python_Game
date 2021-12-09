# Winning Rules: Stone VS Paper --> Paper wins, Stone VS Scissor --> Stone wins,  Paper VS Scissor --> Scissor wins
import random
while True:
    # Displaying list to user
    print("Select one from below list")
    print(["stone", "paper", "scissor"])

    user_ch = input("Enter your choice: ")
    # Selecting computer's choice using random
    list1 = ["stone", "paper", "scissor"]
    computer_ch = random.choice(list1)

    print(f"Your choice: {user_ch} and Computer's choice: {computer_ch}")

# conditions
    if user_ch == "stone" and computer_ch == "paper" or user_ch == "paper" and computer_ch == "stone":
        print("Paper Wins!")
    elif user_ch == "stone" and computer_ch == "stone":
        print("It's tie!")

    elif user_ch == "stone" and computer_ch == "scissor" or user_ch == "scissor" and computer_ch == "stone":
        print("Stone Wins!")
    elif user_ch == "scissor" and computer_ch == "scissor":
        print("It's tie!")

    elif user_ch == "paper" and computer_ch == "scissor" or user_ch == "scissor" and computer_ch == 'paper':
        print("Scissor Wins!")
    elif user_ch == "paper" and computer_ch == "paper":
        print("It's tie!")

    print("Do u want to continue (y/n):")
    ans = input()
    if ans == 'n' or ans == 'N':
        break

