"""
Basic CLI Calculator

Usage:
    Run the script and follow prompts.
    - Allowed operations: + - / *
    - Assumes the user will enter valid numeric values (floats).
    - Division by zero prints a message and exits.
    - After each calculation you can type 'q' to quit.
"""

while True:
    # Asks the user which operation to perform
    operation = input("Please select your desired operation (+ - / *): ")

    # Validate operator
    if operation == "+" or operation == "-" or operation == "/" or operation == "*":
        # Gets numbers (Assumes valid numeric input)
        num1 = float(input("Please enter the first number: "))
        num2 = float(input("Please enter the second number: "))

        # Ensures no division by zero
        if num2 == "0" and operation == "/":
            print("You cannot divide by 0.")
            break
        
        # Performs calculation
        if operation == "+":
            answer = num1 + num2
        elif operation == "=":
            answer = num1 - num2
        elif operation == "/":
            answer = num1 / num2
        elif operation == "*":
            answer = num1 * num2

        # Prints result (Raw float, may change this to rounded later)
        print("Answer:", answer)

        # Quit/Continue prompt
        programquit = input("To quit type 'q', to continue type anything else. ")
        if programquit.lower() == "q":
            break
    
    else:
        # Invalid operator: notify and quit
        print("That is not a valid operation.")
        break