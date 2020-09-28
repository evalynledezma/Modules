# # Python Bank ATM
# - use of methods
# - The user needs to be able to make a deposit
# - The user needs to be able to pull money out
# - The user needs to be able to pay a bill
# - The program needs to track the money in the bank
# - The user needs to be able to look up their balance
# - The program needs to keep running until the user decides to quit the program.

class Bank:
  def __init__(self, balance):
    self.balance = balance
  # TODO:  Fix bug for when user inputs a string of two hundred instead of 200
  def deposit(self):
    amount_to_deposit = input('How much do you want to deposit today? \n')
    self.balance += int(amount_to_deposit)
    print(f'Your new balance is:  {self.balance}')
  
  # TODO:  Should I let them go in the hole?
    # example: balance = 100 withdraw 120 would put them in the hole
  def withdrawal(self):
    amount_to_withdrawal = input('How much do you want to withdraw today? \n')
    self.balance -= int(amount_to_withdrawal)
    print(f'Your new balance is:  {self.balance}')
  def pay_bill(self):
    pass
  def check_balance(self):
    pass
user_one = Bank(100)
user_two = Bank(3000)
user_one.withdrawal()
def game():
  pass