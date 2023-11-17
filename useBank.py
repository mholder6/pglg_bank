'''
the use bank module that prompts the user on what actions
they would like to use, and updates the user on their bank
information.
'''
import bank
import bankActions

'''
Main method that 'communicates' directly with the user
'''
def main():
    user = get_user_lastname()
    if confirm_user(user):
        get_user_password(user)

    while True:
        user_action = get_user_action(user)
        handle_user_action(user, user_action)

        continue_choice = input("Do you want to perform another action? (yes/no): ").lower()
        if continue_choice != 'yes':
            print("Thank you! See you next time!")
            break
    
'''
Gets and returns the inputted last name of the user
'''
def get_user_lastname():
    creds = input("Hi! Welcome to the bank. Please enter your last name.")
    return creds

'''
Validates if the user exists in the system. If not,
the system will shut down.
'''
def confirm_user(last_name):
    if bankActions.valid_user(last_name):
        return True
    print("That user doesn't exist. System shutting down.")
    exit()
    return False

'''
Gets the 4 digit security pin the user inputs, and keeps
prompting user until pin is correct or until the maximum
number of attempts have been reached.
'''
def get_user_password(user):
    user_attempts = 0
    while user_attempts < 3:
        password = makeInputInt("Hi " + bankActions.get_user_firstname(user) + "!" + " Please enter your 4 digit security code. (ShawFoundingYear)")

        if bankActions.validate_pin(user, password):
            print("Welcome " + bankActions.get_user_firstname(user) + "! You are successfully logged in.")
            break
        else:
            user_attempts += 1
            print("Oops! That's not it. Try again!")

    if user_attempts >= 3:
        print("Max attempts reached. System shutting down")
        exit()
    
'''
Informs the specified user of their current Balance,
and asks the user if they would like to make a Deposit (D),
a Withdrawal(W), or if they are done and would like to Exit (E)
the bank.
'''
def get_user_action(user_last_name):
    firstname = bankActions.get_user_firstname(user_last_name)
    balance = bankActions.get_balance(user_last_name)
    print(firstname + ", your balance is currently ", balance)
    user_action = input("\nIf you would like to make a Withdrawal, please enter (W).\nFor a Deposit, enter (D).")
    while not valid_user_action(user_action):
       user_action = input("That was not a valid action. Please enter W, or D.")
    return user_action


'''
Handles the user's selected action.  
'''
def handle_user_action(user, user_action):
    amount = makeInputInt("Please enter the amount:")

    if user_action == "W":
        bankActions.make_withdrawal(user, amount)
    elif user_action == "D":
        bankActions.make_deposit(user, amount)
    

'''
Validates if the user entered a valid action
'''
def valid_user_action(action):
    if action == "W":
        return True
    elif action == "D":
        return True
    elif action == "E":
        return True
    return False
        
'''
Ensures that the user inputs a valid integer.
'''
def makeInputInt(number):
  maxAttempts = 0
  while True:
    try:
       userInput = int(input(number))       
    except ValueError:
       print("Not an integer! Try again.")
       maxAttempts = maxAttempts + 1
       if (maxAttempts >= 4):
           print("Max attempts reached. System shutting down")
           exit()
       continue
    else:
       return userInput 
       break 

if __name__=="__main__": 
    main() 