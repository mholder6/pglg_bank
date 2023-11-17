'''
The bank actions module that defines the information in
the bank, and how to handle the information in the bank
so it can benefit the bank users.
'''
import bank

accounts = bank.load_bank()

'''
Validates if the user exists in the system based on last name.
'''
def valid_user(last_name):
    for account in accounts['bank']['accounts']:
        if (account['lastName'] == last_name):
            return True
    return False

'''
Gets the first name of the user to be properly addressed.
'''
def get_user_firstname(user_lastname):
    for account in accounts['bank']['accounts']:
        if account['lastName'] == user_lastname:
            return account['firstName']
        
'''
Validates if the pin number of the specified user is correct
'''        
def validate_pin(user, pin):
    for account in accounts['bank']['accounts']:
        if account['lastName'] == user:
            return account['info']['pin'] == pin
        
'''
Gets the balance of the specified User
'''
def get_balance(user_last_name):
    for account in accounts['bank']['accounts']:        
        if account['lastName'] == user_last_name:
            return account['info']['balance']

'''
Withdraws the specified amount from the specified user account, 
and sets the new balance.
'''
def make_withdrawal(user, amount):
    balance = get_balance(user)

    if amount > balance:
        print("Sorry, you can't do that.")
    else:
        new_balance = balance - amount
        for account in accounts['bank']['accounts']:
            if account['lastName'] == user:
                account['info']['balance'] = new_balance
        print(get_user_firstname(user), ", your balance is now ", new_balance)

'''
Deposits the specified amount to the specified user account, 
and sets the new balance.
'''
def make_deposit(user, amount):
    balance = get_balance(user)
    new_balance = balance + amount

    for account in accounts['bank']['accounts']:
        if account['lastName'] == user:
            account['info']['balance'] = new_balance  

    print(get_user_firstname(user), ", your balance is now ", new_balance)