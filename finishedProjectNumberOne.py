import random
currentScore = 5
# my last steps are to make sure if they input anything but yes or no they get error checked.
# another thing is that if the number is outside the range my program informs them.

while True:
    proceed = input("Welcome to my guessing game! Would you like to play? (YES/NO)")
    if proceed.lower() == 'yes':
        print(f"Let us begin! Hope you have fun!\nCurrent score to beat is {currentScore} attempts!")
        break
    elif proceed.lower() == 'no':
        exit("Thank you for checking out our guessing game!\nGoodbye!")

def start_game(x):
    scrtNumber = random.randrange(1, x+1)
    guessNum = 0
    attempts = 0
    guessNum = int(input(f"Enter your number guess between 1 and {x} here: "))    
    while guessNum != scrtNumber:
        if guessNum < scrtNumber:
            print("Your guess is too low!")
            guessNum = int(input(f"\nGuess a number between 1 and {x}: "))
            attempts += 1
            continue
        elif guessNum > x:
            print("Please print a number under the specified range!")
            guessNum = int(input(f"\nGuess a number between 1 and {x}: "))
            continue
        elif guessNum < 1:
            print("Please print a number under the specified range!")
            guessNum = int(input(f"\nGuess a number between 1 and {x}: "))
            continue
        elif guessNum > scrtNumber:
            print("Your guess is too high!")
            guessNum = int(input(f"\nGuess a number between 1 and {x}: "))
            attempts += 1
            continue

    print("Congrats! You have guessed the correct number!\nYour guess count is {}!".format(attempts))


while True:
    #x = input(("You will pick a number that will be between 1 and your chosen number: "))
    try:
        
        x = input(("You will pick a number that will be between 1 and your chosen number: "))
        start_game(int(x))
        break
        #x = input(("You will pick a number that will be between 1 and your chosen number: "))
    except ValueError:
        print("Your answer must be an integer greater than 1.")
        continue


while True:
    restart = input("Would you like to play again? (YES/NO)")
    if restart.lower() == "no":
        print("Thank you for playing!")
        break
    elif restart.lower() == "yes":
        while True:
    #x = input(("You will pick a number that will be between 1 and your chosen number: "))
            try:                
                x = input(("You will pick a number that will be between 1 and your chosen number: "))
                start_game(int(x))
                break
            #x = input(("You will pick a number that will be between 1 and your chosen number: "))
            except ValueError:
                print("Your answer must be an integer greater than 1.")
                continue
            
# so far the try exception block is working well
# however, if I press enter for the yes or no, it let's me pick a number

# current problem with the game is that when it is finished it goes back to pick a number