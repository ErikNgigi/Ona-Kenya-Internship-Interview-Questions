from typing import List


def find_intersection(arr1: List[int], arr2: List[int]) -> List[int]:
    """
    Find the sorted, non-repeating intersection of two arrays.

    Args:
        arr1 (List[int]): The first array.
        arr2 (List[int]): The second array.

    Returns:
        List[int]: A list containing the sorted, non-repeating intersection elements.
    """
    intersection = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            if not intersection or arr1[i] != intersection[-1]:
                intersection.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1

    return intersection


def main():
    try:
        arr1 = list(map(int, input("Enter elements for the first array (comma-separated): ").split(",")))
        arr2 = list(map(int, input("Enter elements for the second array (comma-separated): ").split(",")))

        result = find_intersection(arr1, arr2)

        if result:
            print("Intersection:", ",".join(map(str, result)))
        else:
            print("No intersection found.")
    except ValueError:
        print("Invalid input. Please enter integers separated by commas.")


if __name__ == "__main__":
    main()
