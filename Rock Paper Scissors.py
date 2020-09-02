print("Let's play Rock Paper Scissors!")


def rps_game():
    p1_choice = input("p1 Enter the choice: ")
    p2_choice = input("p2 Enter the choice: ")
    if (p1_choice == "Rock" and p2_choice == "Scissors") or (p1_choice == "Scissors" and p2_choice == "Paper") or (p1_choice == "Paper" and p2_choice == "Rock"):
        print("p1 wins!")

    elif (p2_choice == "Rock" and p1_choice == "Scissors") or (p2_choice == "Scissors" and p1_choice == "Paper") or (p2_choice == "Paper" and p1_choice == "Rock"):
        print("p2 wins!")

    elif p1_choice == p2_choice:
        print("Match Draw! Try Again")
    else:
        print("Invalid input! only Rock, Paper, Scissors, allowed as inputs.")

    def play_again():
        response = input("Do you wanna play again? ")
        if response == "Yes" or "yes" or "Y" or "y":
            rps_game()
        else:
            print("Goodbye!")

    play_again()


rps_game()
