low = 1 
high = 100
guesses = 0

while low <= high:
    guess = (low+high) // 2
    guesses+=1

    print(f"My guess is {guess}.")
    feedback = input("Is it correct (c), too high (h), or too low (l)? ")

    if feedback == "c":
        print(f"Yeah i guesss correct in {guesses} tries")
        break
    elif feedback == "h":
        high = guess - 1
        print(f"Okay, I'll guess lower. The new range is {high} to {low}.")
    
    elif feedback == "l":
        low = guess -1
        print(f"Okay, I'll guess higher. The new range is {low} to {high}.")

    else:
        print("Invalid input. Please respond with 'c', 'h', or 'l'.")

    if low > high:
        print("It seems like there was a mistake. Let's start over.")
        break
