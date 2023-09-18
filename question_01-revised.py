def calculate_divisibility_results(m):
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
