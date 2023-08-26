# Define a function to reverse the order of characters in each word of a line
def reverse_words(line):
    # Split the line into individual words
    words = line.split()

    # Create a list of reversed words using list comprehension
    reversed_words = [word[::-1] for word in words]

    # Join the reversed words to form a line with reversed words
    return " ".join(reversed_words)


# Read the number of lines
n = int(input(""))

# Read all lines of input and store them in a list
lines = []
for _ in range(n):
    # Read a line of input from the user and append it to the 'lines' list
    line = input()
    lines.append(line)

# Process and output reversed lines
for line in lines:
    # Call the 'reverse_words' function to reverse words in the current line
    reversed_line = reverse_words(line)

    # Print the reversed line
    print(reversed_line)
