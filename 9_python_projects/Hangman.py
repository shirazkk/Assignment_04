import random 

words = [
    "apple", "banana", "grapes", "orange", "mango", "peach", "melon", "kiwi", "lemon", "cherry",
    "dog", "cat", "horse", "tiger", "lion", "zebra", "monkey", "panda", "giraffe", "elephant",
    "car", "truck", "train", "plane", "boat", "bicycle", "scooter", "van", "bus", "subway",
    "house", "chair", "table", "door", "window", "lamp", "bed", "sofa", "shelf", "mirror",
    "book", "pencil", "paper", "pen", "eraser", "notebook", "ruler", "crayon", "marker", "brush",
    "shirt", "pants", "shoes", "socks", "hat", "jacket", "scarf", "gloves", "belt", "coat",
    "sun", "moon", "star", "cloud", "rain", "snow", "wind", "storm", "fog", "sky",
    "cake", "bread", "cheese", "pizza", "burger", "noodle", "rice", "soup", "cookie", "candy",
    "ball", "doll", "robot", "block", "kite", "puzzle", "carpet", "clock", "radio", "camera",
    "milk", "juice", "water", "soda", "tea", "coffee", "sugar", "salt", "honey", "butter"
]


word = random.choice(words)

guess_letters = []
tries = 6

while tries > 0:
    display_word = ""
    for letter in word:
        if letter in guess_letters:
            display_word+=letter
        else:
            display_word += "_"
    print("Word:", display_word)

    if "_" not in display_word:
        print("🎉 You guessed it! You win!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guess_letters:
        print("⚠️ You already guessed that letter.")
    elif guess in word:
        guess_letters.append(guess)
        print("✅ Good guess!")
    else:
        guess_letters.append(guess)
        tries -=1
        print("❌ Wrong guess. Tries left:", tries)

if tries == 0:
    print("💀 You lost! The word was:", word)