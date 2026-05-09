import random

hangman_pictures = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

def show_menu():
    print("----Hangman----")
    answer = input("Hello, do you want to play Hangman? (Yes/No): ").strip().lower()
    if answer == "yes":
        print("Let's go!!!")
        return True
    elif answer == "no":
        print("Bye...")
        return False
    else:
        print("Please write Yes or No.")
        return show_menu()

def load_words():
    words_list = []
    try:
        with open("answer.txt", "r") as file:
            for line in file:
                word = line.strip().lower()
                if word:
                    words_list.append(word)
    except Exception as error:
        print("Error while reading words:", error)
    return words_list

def save_history(secret_word, result_text, attempts_used):
    try:
        with open("history.txt", "a") as file:
            file.write(f"{secret_word} | {result_text} | attempts used: {attempts_used}\n")
    except Exception as error:
        print("Error while saving history:", error)

def show_history():
    try:
        with open("history.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("History is empty.")
                return
            print("----- Game History -----")
            for line in lines:
                print(line.strip())
    except Exception as error:
        print("Error while reading history:", error)

def play_game():
    words_list = load_words()

    secret_word = random.choice(words_list)
    hidden_word = ["_"] * len(secret_word)
    used_letters = set()
    attempts_left = 6
    attempts_used = 0

    while attempts_left > 0 and "_" in hidden_word:
        print()
        print("Word:", " ".join(hidden_word))
        print("Used letters:", ", ".join(sorted(used_letters)) if used_letters else "none")
        print(f"Attempts left: {attempts_left}")
        print(hangman_pictures[6 - attempts_left])

        guess = input("Enter a letter or word: ").strip().lower()

        if not guess:
            print("Empty input. Try again.")
            continue

        if guess == secret_word:
            hidden_word = list(secret_word)
            break

        if guess in used_letters:
            print("You already used this letter.")
            continue

        used_letters.add(guess)
        attempts_used += 1

        found = False
        for index in range(len(secret_word)):
            if secret_word[index] == guess:
                hidden_word[index] = guess
                found = True

        if not found:
            attempts_left -= 1
            print("Wrong letter!")
        else:
            print("Correct!")

    won = "_" not in hidden_word

    print()
    print(hangman_pictures[6 - attempts_left])
    print("Secret word:", secret_word)

    if won:
        print("You win!")
        save_history(secret_word, "WIN", attempts_used)
    else:
        print("You lose!")
        save_history(secret_word, "LOSE", attempts_used)

def menu():
    while True:
        print()
        print("1. New game")
        print("2. Show history")
        print("3. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            if show_menu():
                play_game()
        elif choice == "2":
            show_history()
        elif choice == "3":
            print("Bye!")
            break
        else:
            print("Wrong choice. Try again.")

menu()