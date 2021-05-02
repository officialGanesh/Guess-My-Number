# import the required module
from random import randint

Secret_number_range = int(input("Enter the range of secret number --> "))

def playerGuess(Secre_number_range):
    secret_number = randint(1, Secret_number_range)
    player_guess = 0
    count = 0
    while player_guess != secret_number:
        player_guess = int(input("guess the number: "))
        if player_guess > secret_number:
            count += 1
            print("your guess is too high!")
        elif player_guess < secret_number:
            count += 1
            print("your guess is too low!")
    count += 1    
    print(f"you guessed the secretNumber ({secret_number}) in {count} guesses.")

    

playerGuess(Secret_number_range)