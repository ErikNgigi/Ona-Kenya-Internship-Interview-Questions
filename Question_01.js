// Import the 'readline' module to handle input and output
const readline = require('readline');

// Create an interface for input and output using stdin and stdout
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Prompt the user to enter an integer N
rl.question('Enter an integer (N): ', (N) => {
  // Convert N to an integer
  N = parseInt(N);
  
  // Check if value of N is not a valid number.
  // Conditional check to determine if N is less than or equal to 0
  if (isNaN(N) || N <= 0) {
    console.log("Invalid input. N should be a positive integer.");
    rl.close();
    return;
  }

  const inputSets = [];

  // Function to read input for a single set
  function readInputSet(index) {
    // Prompt the user to enter a value for M of the current set
    rl.question(`Enter value for M-${index + 1}: `, (M) => {
      const num = parseInt(M);

      if (!isNaN(num)) {
        inputSets.push(num);

        if (inputSets.length === N) {
          // Print the conditions for each input value
          inputSets.forEach((input) => {
            let output = '';

            // Check if the input is a multiple of 3 and/or 5
            if (input % 3 === 0) {
              output += "Ona ";
            }
            if (input % 5 === 0) {
              output += "Data ";
            }
            if (input % 3 === 0 && input % 5 === 0) {
              output += "OnaData ";
            }
            if (output === '') {
              output = "N/A";
            }

            // Display the conditions for the input value
            console.log(`Conditions for input ${input}: ${output}`);
          });

          // Close the input interface
          rl.close();
        } else {
          // Ask for the next input set
          readInputSet(index + 1);
        }
      } else {
        console.log("Invalid input. Please enter an integer.");
        // Retry input for the same set
        readInputSet(index);
      }
    });
  }

  // Start reading input sets from index 0
  readInputSet(0);
});

