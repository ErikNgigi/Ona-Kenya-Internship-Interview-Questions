def is_smooth(arr):
    for i in range(1, len(arr)):
        if abs(arr[i] - arr[i - 1]) > 1:
            return False
    return True


def main():
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
