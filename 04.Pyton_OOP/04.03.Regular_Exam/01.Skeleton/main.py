from project.bank_app import BankApp

bank = BankApp(3)

print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))
print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))

print()

print(bank.add_client('Student', 'Peter Simmons', '1234567891', 500))
print(bank.add_client('Adult', 'Samantha Peters', '1234567000', 1000))
print(bank.add_client('Student', 'Simon Mann', '1234567999', 700))
print(bank.add_client('Student', 'Tammy Smith', '1234567555', 700))

print()

# NB THERE MAY BE MISTAKE IN THIS METHOD
print(bank.grant_loan('StudentLoan', '1234567891'))
print(bank.grant_loan('MortgageLoan', '1234567000'))
print(bank.grant_loan('MortgageLoan', '1234567000'))
print(bank.grant_loan('StudentsdfghjkLoan', '1234567000'))

# print()
#
# # NB THERE MAY BE MISTAKE IN THIS METHOD
# print(bank.remove_client('1234567999'))
#
# print()
#
# print(bank.increase_loan_interest('StudentLoan'))
# print(bank.increase_loan_interest('MortgageLoan'))
#
# print()
#
# print(bank.increase_clients_interest(1.2))
# print(bank.increase_clients_interest(3.5))
#
# print()
#
# print(bank.get_statistics())

# StudentLoan was successfully added.
# MortgageLoan was successfully added.
# StudentLoan was successfully added.
# MortgageLoan was successfully added.

# Student was successfully added.
# Adult was successfully added.
# Student was successfully added.
# Not enough bank capacity.

# Successfully granted StudentLoan to Peter Simmons with ID 1234567891.
# Successfully granted MortgageLoan to Samantha Peters with ID 1234567000.
# Successfully granted MortgageLoan to Samantha Peters with ID 1234567000.

# Successfully removed Simon Mann with ID 1234567999.

# Successfully changed 1 loans.
# Successfully changed 0 loans.

# Number of clients affected: 0.
# Number of clients affected: 1.

# Active Clients: 2
# Total Income: 1500.00
# Granted Loans: 3, Total Sum: 102000.00
# Available Loans: 1, Total Sum: 2000.00
# Average Client Interest Rate: 3.50
