#!/usr/bin/node
function factorial (n) {
  const num = parseInt(n);
  let result;
  if (isNaN(num) || num === 0) {
    result = 1;
  } else {
    result = num * factorial(num - 1);
  }
  console.log(result);
}
factorial(process.argv[2]);
