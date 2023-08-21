def calculate(s):
    # Remove spaces from the input expression
    s = s.replace(" ", "")

    # Initialize lists to store numbers and operators
    numbers = []
    operators = []

    # Initialize variables for tracking substring indices
    start = 0
    stop = 0
    
    # Parse the input string to separate numbers and operators
    for i in s:
        if i in ('+', '-', '*', '/'):
            # Extract and store the number
            numbers.append(int(s[start:stop]))
            # Store the operator
            operators.append(i)
            # Update the start index for the next number
            start = stop + 1
        # Move the stop index to the next character
        stop += 1
    # Append the last number after the loop
    numbers.append(int(s[start:stop]))

    # Perform multiplication and division operations
    i = 0
    while i < len(operators):
        if operators[i] == "*":
            # Perform multiplication and update the numbers and operators lists
            numbers[i] *= numbers[i + 1]
            del numbers[i + 1]
            del operators[i]
        elif operators[i] == "/":
            # Perform division and update the numbers and operators lists
            numbers[i] //= numbers[i + 1]
            del numbers[i + 1]
            del operators[i]
        else:
            # Move to the next operator if not multiplication or division
            i += 1

    # Perform addition and subtraction operations
    i = 0
    while i < len(operators):
        if operators[i] == "+":
            # Perform addition and update the numbers and operators lists
            numbers[i] += numbers[i + 1]
            del numbers[i + 1]
            del operators[i]
        elif operators[i] == "-":
            # Perform subtraction and update the numbers and operators lists
            numbers[i] -= numbers[i + 1]
            del numbers[i + 1]
            del operators[i]
        else:
            # Move to the next operator if not addition or subtraction
            i += 1

    # Return the final result
    return numbers[0]
