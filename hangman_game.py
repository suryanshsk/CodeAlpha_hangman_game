import random

def hangman():
    # List of predefined words
    word_list = ["python", "developer", "hangman", "codealpha", "internship"]

    # Randomly choose one word
    chosen_word = random.choice(word_list)

    # To keep track of guessed letters
    guessed_letters = []

    # Total incorrect guesses allowed
    attempts_left = 6

    print("🎯 Welcome to the Hangman Game!")
    print("📌 You have 6 attempts to guess the word.")
    print("🟢 Word to guess: " + "_ " * len(chosen_word))

    # Main game loop
    while attempts_left > 0:
        guess = input("🔡 Enter a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single alphabet only.")
            continue

        if guess in guessed_letters:
            print("🔁 You already guessed that letter.")
            continue

        # Add guess to list
        guessed_letters.append(guess)

        # Correct guess
        if guess in chosen_word:
            print("✅ Nice! That letter is in the word.")
        else:
            # Incorrect guess
            attempts_left -= 1
            print(f"❌ Oops! Wrong letter. Attempts left: {attempts_left}")

        # Display the current guessed word status
        display_word = ""
        for letter in chosen_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("📖 Word: " + display_word.strip())

        # Check if word is completely guessed
        if "_" not in display_word:
            print("🎉 Hurray! You've guessed the word correctly!")
            break
    else:
        print(f"💀 Game Over! The correct word was: '{chosen_word}'")

# Run the game
if __name__ == "__main__":
    hangman()
