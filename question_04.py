# Define a function to check if an array is smooth
def int_is_smooth(arr):
    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        # Check if the absolute difference between adjacent elements is greater than 1
        if abs(arr[i] - arr[i - 1]) > 1:
            return False  # Return False if the smoothness condition is violated
    return True  # Return True if the array is smooth


# Read the length of the array
n = int(input())

# Read the array elements and store them in a list
arr = list(map(int, input().split()))

# Check if the array is smooth using the defined function
if int_is_smooth(arr):
    print("YES")  # If the array is smooth, print "YES"
else:
    print("NO")  # If the array is not smooth, print "NO"
