const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
let count = 0;

readline
  .on("line", function (line) {
    if (count === 0) {
      input.push(line.trim());
      count++;
    } else {
      input.push(line.trim());
      readline.close();
    }
  })
  .on("close", function () {
    const n = parseInt(input[0]);
    const f = parseInt(input[1]);
    console.log(solution(n, f));
    process.exit();
  });

const solution = (n, f) => {
  let answer;
  return answer;
};
