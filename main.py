# Derek
# SE

import random

games = []


def show_menu():
    # IH1
    print("\n Video Game Tracker / Manager ")

    # IH3
    print("1. Add a game (add a title to your library)")
    print("2. View my games (see saved titles)")
    print("3. Delete a game (remove a title permanently)")
    print("4. Pick a game for me (random suggestion)")
    print("5. Exit")


def add_game():
    # IH6
    game = input("Enter the name of the game you want to add and press Enter: ")

    if game.strip() == "":
        # IH8
        print("You didn’t enter anything.")
        return

    if game in games:
        # IH8
        print("That game is already in your library.")
        return

    games.append(game)
    print(f'"{game}" has been added to your library.')


def view_games():
    if not games:
        print("Your game list is empty.")
        return

    print("\nYour Game Library:")
    for index, game in enumerate(games, start=1):
        print(f"{index}. {game}")


def delete_game():
    if not games:
        print("There are no games to delete.")
        return

    # IH2
    print("\nWARNING: Deleting a game is permanent and cannot be undone.")

    view_games()

    # IH7
    choice = input("Enter the number OR the name of the game you want to delete: ")

    # reinforces IH2
    confirm = input("Are you sure you want to permanently delete this game? (yes/no): ")
    if confirm.lower() != "yes":
        print("Deletion cancelled.")
        return

    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(games):
            removed = games.pop(choice - 1)
            print(f'"{removed}" has been removed from your library.')
        else:
            print("That number doesn’t match any game.")
    elif choice in games:
        games.remove(choice)
        print(f'"{choice}" has been removed from your library.')
    else:
        print("Invalid input. No game deleted.")


def pick_random_game():
    if not games:
        print("You need to add some games first.")
        return

    print(f"You should play: {random.choice(games)}")


while True:
    show_menu()

    # IH6
    choice = input("Choose an option (1-5) and press Enter to continue: ")

    # IH8
    while choice not in ["1", "2", "3", "4", "5"]:
        print("Invalid option. Please choose a number between 1 and 5.")
        choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_game()
    elif choice == "2":
        view_games()
    elif choice == "3":
        delete_game()
    elif choice == "4":
        pick_random_game()
    elif choice == "5":
        print("See you next time!")
        break

        # Ih4 shown from familiar design
        # Ih5 shown from ability to recover / continue


