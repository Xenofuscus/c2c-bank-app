# encoding: utf-8
# 1. Note the variable login_types, the list of account types.
login_types = ["admin", "user", "guest"]
# 2. Complete the function called gatekeeper that returns the following error message strings in the following scenarios:
# For “admin”:
# program says “You have the privileges.”
# For “user”:
# program says “You have limited privileges.”
# For “guest”:
# program says “You have no privileges.”
def gatekeeper(login):
  if login == login_types[0]:
    return "You have the privileges"
  if login == login_types[1]:
    return "You have limited privileges"
  if login == login_types[2]:
    return "You have no privileges"
  else:
    return "Access Denied :("

# 3. Call the gatekeeper function with a string and print what it returns.
print(gatekeeper("admin"))
# Test a nonsense login type.
print(gatekeeper("potato"))
# 4. How could this code be improved? Make it better. Think about what other scenarios you should cover in your if logic.
# ANS:
# I would add an else at the end, to ensure no one that is not at least a guest is allowed past the gatekeeper. Additionally,
# I would use the login_types list for comparison in case the admin decides to change the types. This way we will still be able
# to maintain the logic by treating the list indexes as "codes".

# 5. Complete the function called check_balance that takes one parameter, loan_balance.
def check_balance(loan_balance):
# 6. If loan_balance is zero or more, it says “you don’t owe any money”
# 7. If loan_balance is negative, it  says “you owe $X” where X is the amount
    if loan_balance >= 0:
      return "you don't owe any money"
    else:
      return "you owe $" + str(loan_balance * -1)

# 8. Call your function with a negative and positive number and print what it returns.
print(check_balance(300))
# Test a negitive balance.
print(check_balance(-12))
