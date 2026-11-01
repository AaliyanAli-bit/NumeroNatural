# Project: Natural Number Checker
# Topic: Conditional Statements & Input Validation

# Step 1: Prompt user for input
user_input = input("Enter a number to check: ")

# Step 2: Try converting the input to an integer
try:
    number = int(user_input)

    # Step 3: Check conditional statement for Natural Numbers (greater than 0)
    if number > 0:
        print(f"\n✅ {number} IS a Natural Number!")
    else:
        print(f"\n❌ {number} is NOT a Natural Number. (Natural numbers must be positive whole numbers greater than 0).")

except ValueError:
    # Handles cases where user enters decimals or text
    print(f"\n❌ '{user_input}' is NOT a Natural Number. (Please enter a whole integer without decimals).")