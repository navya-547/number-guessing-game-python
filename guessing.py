import random

print("===== NUMBER GUESSING GAME =====")

while True:
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess > secret_number:
            print("Too High!")

        elif guess < secret_number:
            print("Too Low!")

        else:
            print(f"Correct! You guessed in {attempts} attempts.")
            break

    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break