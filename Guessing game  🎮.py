
import random

secret_number = random.randint(1, 20)

print("I am thinking of a number between 1 and 20.")
print("You have 6 tries to guess it!")

for tries in range(6):
    guess = int(input("Take a guess: "))

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("🎉 You got it! The number was", secret_number)
        break
else:
    print("Out of tries! The number was", secret_number)
