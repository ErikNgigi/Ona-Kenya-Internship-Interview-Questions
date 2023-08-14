// Import the 'readline' module to handle input and output
const readline = require('readline');

// Create an interface for input and output using stdin and stdout
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Function to check if an array is smooth
function isSmooth(arr) {
  // Loop through the array starting from index 1
  for (let i = 1; i < arr.length; i++) {
    // Check if the absolute difference between adjacent elements is greater than 1
    if (Math.abs(arr[i] - arr[i - 1]) > 1) {
      // If the condition is met, the array is not smooth
      return false;
    }
  }
  // If the loop completes without returning, the array is smooth
  return true;
}

// Read the number of elements in the array
rl.question('Enter the number of elements (N): ', (N) => {
  // Convert N to an integer
  N = parseInt(N);

  // Check if N is not within the specified range
  if (N < 1 || N > 10) {
    // Close the input interface and exit the program
    rl.close();
    return;
  }

  // Read the array elements from the user
  rl.question(`Enter ${N} array elements separated by spaces (between 1 and 100): `, (input) => {
    // Split the input string into an array of strings, then convert each string to a number
    const elements = input.split(' ').map(Number);

    // Check if the number of elements or their values are invalid
    if (elements.length !== N || elements.some(num => num < 1 || num > 100)) {
      // Close the input interface and exit the program
      rl.close();
      return;
    }

    // Check if the array is smooth using the isSmooth function
    if (isSmooth(elements)) {
      // If the array is smooth, print "YES"
      console.log("YES");
    } else {
      // If the array is not smooth, print "NO"
      console.log("NO");
    }

    // Close the input interface
    rl.close();
  });
});

