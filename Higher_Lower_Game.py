import random
from ART1 import logo
from ART1 import vs
from data import data

def format_data(account):
    """ Takes the account data and return  printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from  {account_country}"
def check_answer(guess, followers1, followers2):
    """Take the user guess and follower counts and return if they got it right ."""
    if followers1 > followers2:
        return guess=="a"
    else:
        return guess=="b"
#Displaying art
print(logo)
score=0
should_continue=True
account2=random.choice(data)
# Make the game repeatable
while should_continue:

#Generating random account from data
    account1=account2
    account2=random.choice(data)

    while account1==account2:
        account2=random.choice(data)

    print(f"Compare A: {format_data(account1)}.")
    print(vs)
    print(f"Against B: {format_data(account2)}.")

    #Ask user for a guess
    guess=input("Who has more followers? Type 'A'or 'B' ").lower()

    # Check if the user is correct
    # Get follower count of each account.
    followers1_count=account1["follower_count"]
    followers2_count=account2["follower_count"]
    is_correct=check_answer(guess,followers1_count,followers2_count)

    # Give user some feedback according to their guesses.
    # Score Keeping
    if is_correct:
        score+=1
        print(f"you're  right! Current score: {score}.")
    else:
        should_continue=False
        print(f"Sorry, that's wrong. Final Score: {score}.")









