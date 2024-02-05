import random
a = random.randint(1, 20)
guess_count = 0

print("Hello! What is your name?")
user_name = input()
print(f"Well, {user_name}, I am thinking of a number between 1 and 20.\nTake a guess.")

while True:
    guess = int(input())
    if guess != a:
        guess_count += 1
        if guess > a:
            print("Your guess is too high.\nTake a guess.")
        else:
            print("Your guess is too low.\nTake a guess.")
    elif guess == a:
        print(f"Good job, {user_name}! You guessed my number in {guess_count} guesses!")
        break