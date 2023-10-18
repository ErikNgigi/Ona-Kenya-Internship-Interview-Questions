def is_smooth(arr):
    """
    Check if an array is 'smooth'.

    This function checks if the given list `arr` is 'smooth,' which means that the absolute difference between adjacent
    elements in the list is at most 1. If the array is smooth, it returns True; otherwise, it returns False.

    Args:
        arr (list): The input list to be checked for smoothness.

    Returns:
        bool: True if the array is smooth; False otherwise.
    """
    for i in range(1, len(arr)):
        if abs(arr[i] - arr[i - 1]) > 1:
            return False
    return True


def main():
    """
    Main function for checking the smoothness of an array.

    This function reads the length of the array and the array elements from the user and checks if the array is smooth.
    If the number of entered elements does not match the specified length, an error message is displayed.
    If the array is smooth, it prints 'YES'; otherwise, it prints 'NO.'

    The input elements should be separated by spaces.
    """
    try:
        n = int(input("Enter the length of the array: "))
        input_line = input("Enter the array elements separated by spaces: ")
        arr = list(map(int, input_line.split()))

        if len(arr) != n:
            print("Error: Number of elements entered does not match the specified length.")
        else:
            if is_smooth(arr):
                print("YES")
            else:
                print("NO")
    except ValueError:
        print("Error: Invalid input. Please enter valid integers.")


if __name__ == "__main__":
    main()
