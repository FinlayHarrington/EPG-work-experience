import random
print("welcome to the gamble game")
print("Here are the rules of the game:")
print("You will have as many tries as you want to guess a number between 1 and 100 correctly. If you lose you will lose one chip but if you win you will get thirty chips")
Participate = input("I will give you 100 chips to start you off. WOULD YOU LIKE TO PLAY? (Y/N)")
if Participate == "Y" or Participate == "y":
    print("Great! Let's play.")
    chips = 100
    play = True
    while play == True:
        for i in range(3):
            number = random.randint(1, 100)
            guess = int(input("Please enter your guess (1-100): "))
            if guess == number:
                chips += 30
                print("Congratulations! You guessed the number correctly. You now have", chips, "chips.")
                Play_agian = input("Do you want to play again? (Y/N)")
                if Play_agian == "Y" or Play_agian == "y":
                    play = True
                else:
                    play = False
            else:
                print("Sorry, that's not correct.")
                chips -= 1
                print("Please try agian. You have", chips, "chips left.")
else:
    print("Maybe next time!")
    