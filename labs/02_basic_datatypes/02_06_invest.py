'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''



investment = input("Please enter the investment amount.")
investment = float(investment)

percentage = input("Please enter the yearly ROI in percent.")
percentage = float(percentage)

contract_duration = input("Please enter the lifetime of the contract in years.")
contract_duration = float(contract_duration)

interestperyear = investment/100*percentage

dividend = interestperyear*contract_duration

print(dividend)