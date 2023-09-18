def reverse_words(line: str) -> str:
    """
    Reverse the order of characters in each word of a line.

    Args:
        line (str): The input line.

    Returns:
        str: The line with reversed words.
    """
    words = line.split()
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)


def main():
    try:
        n = int(input("Enter the number of lines: "))
        lines = []

        for _ in range(n):
            line = input("Enter a line: ")
            reversed_line = reverse_words(line)
            lines.append(reversed_line)

        for reversed_line in lines:
            print(reversed_line)
    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of lines.")


if __name__ == "__main__":
    main()
