import random

def play_hangman():
    words = ["array", "banana", "jolly", "funny", "kiwi"]
    secret_word = random.choice(words)
    guessed_letters = []
    attempts_left = 6

    print("\n🎮 Welcome to Hangman!")
    print("Guess the word one letter at a time.\n")

    while attempts_left > 0:
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print("Word:", display_word.strip())

        guess = input("Enter a letter: ").lower().strip()

        if guess in guessed_letters:
            print("🔁 You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("✅ Correct guess!\n")
        else:
            attempts_left -= 1
            print(f"❌ Wrong guess! Attempts left: {attempts_left}\n")

        all_guessed = True
        for letter in secret_word:
            if letter not in guessed_letters:
                all_guessed = False
                break

        if all_guessed:
            print("🎉 You guessed the word:", secret_word)
            break

    if not all_guessed:
        print("💀 Game Over! The word was:", secret_word)

while True:
    play_hangman()
    again = input("\n🔄 Do you want to play again? (yes/no): ").lower().strip()
    if again != "yes":
        print("👋 Thanks for playing Hangman!")
        break