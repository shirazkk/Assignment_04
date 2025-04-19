import random


chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=[]{}|;:,.<>?"


length = int(input("Enter your password length "))

password = ""

for i in range(length):
    password+=random.choice(chars)
    

print("Your generated password is:", password)
