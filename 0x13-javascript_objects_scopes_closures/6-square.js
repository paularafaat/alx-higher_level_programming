#!/usr/bin/node
const BaseSquare = require('./5-square');

class Square extends BaseSquare {

  charPrint (c) {
    if (c !== 'C' || c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
