import random

print("Number guessing game")

number= random.randint(1,9)

chances = 0

while chances < 5 :

    guess = int(input("Enter your guess: "))

    if guess ==number:
        print("Congratulation you won")
        break

    elif guess < number:
       print("Your guess was too low: Guessa number higher than",guess)

    else:

        print("Youe guess was too high: Guess a number lower than that", guess)


chances += 1

if not chances <5:
    print("YOU LOSE!!! The number is",number)

    

