# Define a function to find the sorted non-repeating intersection of two arrays
def find_intersection(arr1, arr2):
    intersection = []  # Initialize a list to store the intersection elements
    i, j = 0, 0  # Initialize pointers for the two arrays point to the first element

    # Iterate through the arrays while both pointers are within bounds
    while i < len(arr1) and j < len(arr2):
        # Compare elements at the current positions of both arrays
        if arr1[i] == arr2[j]:
            # If the elements match and the intersection list is empty or the last element is different,
            # add the element to the intersection list
            if not intersection or arr1[i] != intersection[-1]:
                intersection.append(arr1[i])
            i += 1  # Move the pointer in the first array
            j += 1  # Move the pointer in the second array
        elif arr1[i] < arr2[j]:
            i += 1  # Move the pointer in the first array
        else:
            j += 1  # Move the pointer in the second array

    return intersection  # Return the sorted non-repeating intersection


# Read input for the two arrays as comma-separated strings
arr1 = input().split(",")
arr2 = input().split(",")

# Find the sorted non-repeating intersection using the defined function
result = find_intersection(arr1, arr2)

# Print the result by joining the elements with commas after converting them to strings
print(",".join(map(str, result)))
