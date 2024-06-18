#!/usr/bin/node

function add(a, b) {
    a = parseInt(a);
    b = parseInt(b);
    if (isNaN(a) || isNaN(b)) {
      console.log("NaN");
    } else {
      const sum = a + b;
      console.log(sum);
    }
  }
  