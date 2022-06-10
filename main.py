import random

possible_actions = ['R', 'P', 'S']
user_action = input("Pick an option (R, P or S): ")


while user_action not in possible_actions:
    print("Error: Input is not in options" )
    user_action = input("Pick again (R, P or S): ")
    
computer_action = random.choice(possible_actions)

while user_action == computer_action:
    statement = "Player ({}) : CPU ({})".format(user_action, computer_action)
    print(statement)
    print("It's a tie!")
    user_action = input("Pick again (R, P or S): ")
    computer_action = random.choice(possible_actions)
    
if user_action == "R":
    statement = "Player ({}) : CPU ({})".format(user_action, computer_action)
    print(statement)
    if computer_action == "S":
        print("You win!")
    else:
        print("You lose.")
elif user_action == "P":
    statement = "Player ({}) : CPU ({})".format(user_action, computer_action)
    print(statement)
    if computer_action == "R":
        print("You win!")
    else:
        print("You lose.")
elif user_action == "S":
    statement = "Player ({}) : CPU ({})".format(user_action, computer_action)
    print(statement)
    if computer_action == "P":
        print("You win!")
    else:
        print("You lose.")
