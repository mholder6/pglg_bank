'''
the bank module that loads and stores the bank info.
'''
import json

'''
Loads the bank information
'''
def load_bank():
    bank_file = open('bank.json')
    bank = json.load(bank_file)
    return bank


