#!/usr/bin/node
const  Square = require('./6-square');
class Square extends Square {

  charPrint(c) {
    if (c === undefined) {
        c = 'X';
    }
    for (let i = 0; i < this.size; i++) {
        console.log(c.repeat(this.size));
    }
  }
}
module.exports = Square;
