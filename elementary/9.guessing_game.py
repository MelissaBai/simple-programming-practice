import random


def guessing_game(secret):
    guessing = int(input("Please guess a number. "))
    n = 1
    while n <= 6:
        if guessing == secret:
            print ("You guessed it right!")
            n += 1
            print("You guessed " + str(n) + " times")
            break
        elif guessing < secret:
            n += 1
            print ("Your number is too low. Please guess another number.")
            guessing = int(input("Please guess a number. "))
        elif guessing > secret:
            n += 1
            print ("Your number is too high. Please guess another number.")
            guessing = int(input("Please guess a number. "))

    print ("You have exceeded maximum guess.")

def main():
    secret = random.randint(1, 20)
    guessing_game(secret)

main()
'''
1. Is there a way without repeating 'guessing = int(input("Please guess a number. "))'
2. How to make it so if user wants to play another game, regenerating secret number, it's also possible.
3. How to streamline the process.
'''
