#!/usr/bin/node
function factorial (n) {
  const num = parseInt(n);
  if (isNaN(num) || num === 0) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
console.log(factorial(process.argv[2]));
