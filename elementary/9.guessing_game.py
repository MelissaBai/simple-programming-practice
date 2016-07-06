import random


def guessing_game(secret):
    for n in range(6):
        guessing = int(input("Please guess a number. "))
        if guessing == secret:
            print("You guessed it right!")
            print("You guessed " + str(n+1) + " times")
            return
        elif guessing < secret:
            print("Your number is too low. Please guess another number.")
        elif guessing > secret:
            print("Your number is too high. Please guess another number.")
    print("You have exceeded maximum guess.")

def main():
    while True:
        secret = random.randint(1, 20)
        guessing_game(secret)
        response = input('Do you want to play again? ')
        if response[0].lower() != 'y':
            break

main()
'''
1. Is there a way without repeating 'guessing = int(input("Please guess a number. "))'
2. How to make it so if user wants to play another game, regenerating secret number, it's also possible.
3. How to streamline the process.
'''
