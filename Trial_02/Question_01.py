def calculate_divisibility_results(m):
    """Calculate divisibility results based on the given integer M.

    Args:
        M (int): The integer for which divisibility results should be calculated.

    Returns:
        str: A string containing the divisibility results.
    """
    result = ""
    found = False

    for num in range(1, m + 1):
        if num % 3 == 0 and num % 5 == 0:
            result += "OnaData "
            found = True
        elif num % 3 == 0:
            result += "Ona "
            found = True
        elif num % 5 == 0:
            result += "Data "
            found = True

    if not found:
        result += "N/A "

    return result.strip()


def main():
    """
    Main function to handle user input and processing the divisibility result.
    """
    try:
        n = int(input("Enter the number of lines: "))
        numbers = []

        for _ in range(n):
            m = int(input("Enter an integer value: "))
            result = calculate_divisibility_results(m)
            numbers.append(result)

        for result in numbers:
            print(result)
    except ValueError:
        print("Invalid input. Please enter valid integer values.")


if __name__ == "__main__":
    main()
