import random

secret_number = random.randint(1, 10)
attempts = 0

print("🎮 Welcome to Number Guessing Game!")
while True:
    guess = int(input("Enter your guess (1-10): "))
    attempts += 1

    if guess == secret_number:
        print(f"🎉 Correct! You guessed it in {attempts} attempts.")
        break
    else:
        print("❌ Wrong guess. Try again!")
