import random
import time

def roll_dice():
    return random.randint(1, 6)

def main():
    print("Welcome to Mini Ludo Dice Game!\n")

    # Ask the user for the number of players
    while True:
        try:
            num_players = int(input("Enter number of players (2-4): "))
            if 2 <= num_players <= 4:
                break
            else:
                print("Please enter a number between 2 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    players = {f"Player {i+1}": 0 for i in range(num_players)}
    winner = None

    while not winner:
        for player in players:
            print(f"{player}'s turn. Current position: {players[player]}")

            dice = roll_dice()
            print(f"{player} rolled a {dice}.")
            players[player] += dice
            print(f"{player} moves to {players[player]}.")

            if players[player] >= 50:
                winner = player
                print(f"\n{winner} has reached 50 or more and wins the game!")
                break

            if dice == 6:
                print(f"{player} rolled a 6 and gets an extra turn!")
                while True:
                    dice = roll_dice()
                    print(f"{player} rolled a {dice} on extra turn.")
                    players[player] += dice
                    print(f"{player} moves to {players[player]}.")

                    if players[player] >= 50:
                        winner = player
                        print(f"\n{winner} has reached 50 or more and wins the game!")
                        break

                    if dice != 6:
                        break
                if winner:
                    break

            print("")  # Blank line for clarity
            time.sleep(1)

    print("\nThanks for playing Mini Ludo Dice Game!")

if __name__ == "__main__":
    main()
