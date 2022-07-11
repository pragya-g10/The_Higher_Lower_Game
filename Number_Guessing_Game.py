import random
from art import number_game_logo
easy_attempts=10
hard_attempts=5
def check_answer(guess,choice,turns):
   if guess > choice:
    print("too high")
    return turns-1
   elif guess < choice:
    print("Too Low ")
    return turns-1
   else:
    print(f" you got it ! answer is {choice}")

def difficulty():
    diff = input("choose a difficulty. Type 'easy' or 'hard':")

    if diff=="easy":
        return easy_attempts
    if diff=="hard":
        return hard_attempts
def game():
    print(number_game_logo )
    print("WELCOME to Number Guessing Game")
    print("I am thinking of a number between 1 and 100")
    choice=random.randint(1,100)
    print(f" correct answer is {choice}")
    turns=difficulty()
    guess=0
    while guess !=choice:
        print(f"You have {turns} attempts remaining to guess the number")
        guess=int(input("Guess a number: "))
        turns=check_answer(guess, choice, turns)
        if turns == 0:
            print("you have ran out of guesses, you lose. ")
            return
        elif guess !=choice:
            print("Guess again")
game()

# ...........................................................................................................
# for number in range(1, 101):
#   if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
#   elif number % 3 == 0:
#     print("Fizz")
#   elif number % 5 == 0:
#     print("Buzz")
#   else:
#     print(number)
#



