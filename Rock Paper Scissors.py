print("Let's play rock paper scissors!")


def rps_game():
    p1_choice = input("p1 Enter the choice: ")
    p2_choice = input("p2 Enter the choice: ")

    if (p1_choice == "rock" and p2_choice == "scissors") or (p1_choice == "scissors" and p2_choice == "paper") or (p1_choice == "paper" and p2_choice == "rock"):
        print("p1 wins!")

    elif (p2_choice == "rock" and p1_choice == "scissors") or (p2_choice == "scissors" and p1_choice == "paper") or (p2_choice == "paper" and p1_choice == "rock"):
        print("p2 wins!")

    elif p1_choice == p2_choice:
        print("Match Draw! Try Again")
    else:
        print("Invalid input! only rock, paper, scissors, allowed as inputs.")

    def play_again():
        response = input("Do you wanna play again? ")
        if response in ["yes", "Yes", "Y", "y"]:
            rps_game()
        else:
            print("Goodbye!")

    play_again()


rps_game()
