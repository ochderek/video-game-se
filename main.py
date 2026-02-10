# Derek
# SE


import random

games = []


def show_menu():
    print("\n Video Game Tracker / Manager")
    print("1. Add a game")
    print("2. View my games")
    print("3. Delete a game")
    print("4. Pick a game for me")
    print("5. Exit")


def add_game():
    game = input("Enter a game name: ")
    if game != "":
        games.append(game)
        print(f'"{game}" has been added to your library.')
    else:
        print("You didn’t enter anything.")


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

    view_games()
    choice = input("Enter the number of the game you want to delete: ")

    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(games):
            removed = games.pop(choice - 1)
            print(f'"{removed}" has been removed from your library.')
        else:
            print("That number doesn’t match any game.")
    else:
        print("Please enter a valid number.")


def pick_random_game():
    if not games:
        print("You need to add some games first.")
        return

    print(f"You should play: {random.choice(games)}")


while True:
    show_menu()
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
    else:
        print("That’s not a valid option.")


