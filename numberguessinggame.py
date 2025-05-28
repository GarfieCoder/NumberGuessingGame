import random



print("Welcome to the Number Guessing Game!")


def select_difficulty():
    while True:
        difficulty = input("Choose a difficulty level (easy, medium, hard): ").lower()
        if difficulty in ['easy', 'medium', 'hard']:
            return difficulty
        else:
            print("Invalid choice. Please select 'easy', 'medium', or 'hard'.")

def main():
    numGuesses = 0
    difficulty = select_difficulty()
    
    if difficulty == 'easy':
        number_to_guess = random.randint(1, 100)
        attempts = 7
    elif difficulty == 'medium':
        number_to_guess = random.randint(1, 100)
        attempts = 5
    else:  # hard
        number_to_guess = random.randint(1, 100)
        attempts = 3

    print(f"You have {attempts} attempts to guess the number between 1 and 100.")

    for attempt in range(attempts):
        guess = int(input(f"Attempt {attempt + 1}: Enter your guess: "))
        
        if guess < number_to_guess:
            print("Too low!")
            numGuesses += 1
        elif guess > number_to_guess:
            print("Too high!")
            numGuesses += 1
        else:
            print(f"Congratulations! You've guessed the number! It took you {numGuesses + 1} attempts.")
            break

    else:
        print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")

main()
