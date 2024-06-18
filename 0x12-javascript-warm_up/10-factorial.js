#!/usr/bin/node
function factorial (n) {
  n = parseInt(n);
  if (isNaN(n) || n === 0) {
    return 1;
  } else {
    const result = n * factorial(n - 1);
    console.log(result);
  }
}
