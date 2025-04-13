
#Mad Libs Game

print("Welcome to the Mad Libs Game!")
print("Please provide the following words:\n")

# the user for input
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")

# Create a mad lib using the user's input
mad_libs = f"Today, I saw a very {adjective} {noun} trying to {verb} in the park."
print(mad_libs) # and print it out