# encoding: utf-8
# 1. Note the variable login_types, the list of account types.
login_types = ["admin", "user", "guest", "moderator"]
# 2. Complete the function called gatekeeper that returns the following error message strings in the following scenarios:
# For “admin”:
# program says “You have the privileges.”
# For “user”:
# program says “You have limited privileges.”
# For “guest”:
# program says “You have no privileges.”

# Return constants
FULL_PRIV = "You have the privileges"
LIM_PRIV = "You have limited privileges"
NO_PRIV = "You have no privileges"
ACC_DEN = "Access Denied"

def gatekeeper(login, account_age):
  if login == login_types[0] or login == login_types[3]:
    return FULL_PRIV
  if login == login_types[1] and account_age >= 7:
    return LIM_PRIV
  if login == login_types[2] or login == login_types[1]:
    return NO_PRIV
  else:
    return ACC_DEN

# 3. Call the gatekeeper function with a string and print what it returns.
def gatekeeper_test():
    # Test with admin login.
    require("admin, account_age 6", FULL_PRIV, gatekeeper("admin", 6))
    require("admin, account_age 7", FULL_PRIV, gatekeeper("admin", 7))
    require("admin, account_age 8", FULL_PRIV, gatekeeper("admin", 8))
    # Test with moderator login.
    require("moderator, account_age 6", FULL_PRIV, gatekeeper("moderator", 6))
    require("moderator, account_age 7", FULL_PRIV, gatekeeper("moderator", 7))
    require("moderator, account_age 8", FULL_PRIV, gatekeeper("moderator", 8))
    # Test with user login and with an account age >= 7.
    require("user, account_age 7", LIM_PRIV, gatekeeper("user", 7))
    require("admin, account_age 8", LIM_PRIV, gatekeeper("user", 8))
    # Test with user login and with an account age <= 7.
    require("user, account_age 6", NO_PRIV, gatekeeper("user", 6))
    # Test with guest login.
    require("guest, account_age 6", NO_PRIV, gatekeeper("guest", 6))
    require("guest, account_age 7", NO_PRIV, gatekeeper("guest", 7))
    require("guest, account_age 8", NO_PRIV, gatekeeper("guest", 8))
    # Test gibberish login.
    require("oaiw, account_age 6", ACC_DEN, gatekeeper("oaiw", 6))
    require("oaiw, account_age 7", ACC_DEN, gatekeeper("oaiw", 7))
    require("oaiw, account_age 8", ACC_DEN, gatekeeper("oaiw", 8))

# Test a nonsense login type.
print(gatekeeper("potato", 0))
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

# Testing stuff
def require(testName, expected, actual):
    if expected == actual:
        print(testName, " sucess")
    else
        print(testName, " failed:")
        print("\t expected: ", expected)
        print("\t received: ", actual)
