import random 

def play():
    choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    user = input("what can you choose? r' for rock 'p' for paper 's' for scissors ").lower()
    computer = random.choice(list(choices.keys()))

    if user not in choices:
         print("Invalid choice! Please enter 'r', 'p', or 's'.")
         return

    print(f"You chose: {choices[user]}")
    print(f"Computer chose: {choices[computer]}")

    if user == computer:
        print("Match Tie")
    elif (user == "r" and computer == "s") or \
         (user == 's' and computer == 'p') or \
         (user == 'p' and computer == 'r'):
         print("You Win!")
    else:
        print("Computer wins!")
    

play()