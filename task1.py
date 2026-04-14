import random

words = {
    "python": "Programming language",
    "apple": "A fruit",
    "tiger": "A wild animal",
    "ocean": "Large water body",
    "space": "Beyond Earth"
}

def display_word(word, guessed):
    return " ".join([letter if letter in guessed else "_" for letter in word])

def hangman():
    word = random.choice(list(words.keys()))
    hint = words[word]
    
    guessed_letters = []
    attempts = 6
    score = 0
    
    print("\nWelcome to Hangman Game")
    print("Hint:", hint)

    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print("Attempts left:", attempts)
        print("Guessed letters:", guessed_letters)

        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("Already guessed")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct")
            score += 10
        else:
            print("Wrong")
            attempts -= 1
            score -= 5

        if all(letter in guessed_letters for letter in word):
            print("\nYou won")
            print("Word was:", word)
            print("Score:", score)
            return

    print("\nGame Over")
    print("The word was:", word)
    print("Final Score:", score)


while True:
    hangman()
    again = input("\nPlay again? (yes/no): ").lower()
    if again != "yes":
        print("Thank you for playing")
        break
