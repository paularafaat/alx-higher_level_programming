#!/usr/bin/node
function factorial (n) {
  let result;
  if (isNaN(parseInt(n)) || n === 0) {
    result = 1;
  } else {
    result = n * factorial(n - 1);
  }
  console.log(result);
}
factorial(process.argv[2]);
