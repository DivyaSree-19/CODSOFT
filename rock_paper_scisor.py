import random

def play_game():
    possible_actions = ["rock", "paper", "scissors"]
    
    while True:
        while True:
            print("Rock")
            print("paper")
            print("scissors")
            player = input("\nEnter a choice: ").lower()
            if player in possible_actions:
                break
            else:
                print("Invalid choice. Please choose rock, paper, or scissors.")
        
        computer = random.choice(possible_actions)
        print(f"\nYou chose {player}, computer chose {computer}.\n")

        if player == computer:
            print(f"Both players selected {player}. It's a tie!")
        elif player == "rock":
            if computer == "scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif player == "paper":
            if computer == "rock":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        elif player == "scissors":
            if computer == "paper":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()

