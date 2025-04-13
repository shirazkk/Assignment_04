
import random 


def guess_the_number():
    print("Welcome to the Guess the Number game!")
    print("You have to guess number between 1 and 10.")
    print("You have 5 attempts to guess the number.")
    
    #random number
    number_to_guess = random.randint(1,10)
    attempt = 0
    max_attempts = 5

    while True:
        try:
            # Get User Input
            user_guess = int(input("Take a guess: "))
            attempt += 1
            print(f"Attempt {attempt} of {max_attempts}")
            if attempt > max_attempts:
                print("Sorry, you've used all your attempts. Better luck next time!")
                break

            if user_guess <1 or user_guess > 10:
                print("Please enter a number between 1 and 10.")

                continue
            elif user_guess < number_to_guess:
                print("Your guess is too low.")
            elif user_guess > number_to_guess:
                print("Your guess is too high.")
            else:
                print("Congratulations! You've guessed the number!")
                break
        except ValueError:
            print("That's not a valid number. Please try again.")

        

guess_the_number()
   
