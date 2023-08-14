const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Function to count the number of words in a line
function countWords(line) {
  return line.trim().split(/\s+/).length;
}

rl.question('Enter the value of N: ', (N) => {
  N = parseInt(N); // Convert N to an integer
  const lines = [];
  let linesReceived = 0; // Keep track of the lines received

  // Read lines of input
  rl.on('line', (line) => {
    if (linesReceived < N) {
      const wordCount = countWords(line);

      if (wordCount <= 100) {
        lines.push(line);
        linesReceived++;

        // Print the received line
        console.log(`Words Input in Line ${linesReceived}: ${line}`);

        if (linesReceived === N) {
          rl.close();
        }
      } else {
        console.log("Number of words exceeded the limit. Closing application.");
        rl.close();
      }
    }
  });

  // After all input is received, process and display the reversed words
  rl.on('close', () => {
    lines.forEach((line) => {
      const words = line.split(' ');
      const reversedWords = words.map((word) => {
        return word.split('').reverse().join('');
      });
      console.log(reversedWords.join(' '));
    });
  });
});

