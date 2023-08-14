const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let inputCount = 0;
const arrays = [];

// Print a prompt to guide the user where to input the arrays
console.log("Enter the first array of elements separated by commas:");
// Listen for input on the first line
rl.on('line', (line) => {
  arrays.push(line.split(','));
  inputCount++;

  if (inputCount === 2) {
    rl.close();
  } else {
    // Print a prompt to guide the user where to input the second array
    console.log("Enter the second array of elements separated by commas:");
  }
});

// After all input is received, process and display the non-repeating intersection
rl.on('close', () => {
  const firstArray = arrays[0];
  const secondArray = arrays[1];
  const intersection = [];

  let i = 0;
  let j = 0;

  while (i < firstArray.length && j < secondArray.length) {
    if (firstArray[i] === secondArray[j]) {
      if (intersection.length === 0 || intersection[intersection.length - 1] !== firstArray[i]) {
        intersection.push(firstArray[i]);
      }
      i++;
      j++;
    } else if (firstArray[i] < secondArray[j]) {
      i++;
    } else {
      j++;
    }
  }

  console.log("Repeating Section each of the Arrays:");
  console.log(intersection.join(','));
});

