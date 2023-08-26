# Read the number of lines
N = int(input())

# Read M numbers and store them in a list
numbers = []
# loop iterates 'N' times, where 'N' is the number of lines specified by the user.
for _ in range(N):
    # Read an integer input from the user. This input represents the value 'M'.
    M = int(input())
    # Append the value 'M' to the 'numbers' list, which stores the input integers.
    numbers.append(M)

# Process and output the result for each number
for M in numbers:
    found = False  # Initialize a flag to track if any divisible number is found
    result = ""  # Initialize a string to store the result for the current number

    for num in range(1, M + 1):
        if num % 3 == 0 and num % 5 == 0:
            # If divisible by both 3 and 5, add "OnaData" to the result
            result += "OnaData "
            found = True
        elif num % 3 == 0:
            # If divisible by 3, add "Ona" to the result
            result += "Ona "
            found = True
        elif num % 5 == 0:
            # If divisible by 5, add "Data" to the result
            result += "Data "
            found = True

    if not found:
        # If no divisibility condition is met, add "N/A" to the result
        result += "N/A "

    # Print the result for the current number after removing trailing space
    print(result.strip())
