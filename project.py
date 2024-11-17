#Display the art
from art import logo1
from art import vs
from game_data import data
import random
print(logo1)
#Format the account data into printable format
def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def checked_answer(user_guess, a_followers, b_followers):
    """Checked answer from user and followers real data"""
    if a_followers > b_followers:
            return user_guess == "a"
    else:
        return user_guess == "b"


score = 0
game_should_continue = True
account_b = random.choice(data)
#Make the game repeatable

while game_should_continue:

    #Generate a random account frm the game data
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Compare B: {format_data(account_b)}.")
    #Ask user for a guess
    guess = input("Who has more Followers? TYpe 'A' or 'B': ").lower()

    #Clear the Screen
    print("\n" * 10)
    print(logo1)

    #check if user is correct
    ## - Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count =  account_b["follower_count"]
    ## - use if statement to check if user is correct
    is_correct = checked_answer(guess, a_follower_count, b_follower_count )

    #Give user feedback on their guess
    # Score keeping
    if is_correct:
        score +=1
        print(f"Your are Right. Your score is {score}")
    else:
        print(f"Sorry that's Wrong!. Final Score is:  {score}")
        game_should_continue = False






#Making account at position B become the next account at position A.


