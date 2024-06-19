#!/usr/bin/node
const args = process.argv.slice(2);
const length = process.argv.length;
if (length < 2) {
  console.log(0);
} else {
  const nums = args.map(arg => parseInt(arg));
  nums.sort((a, b) => b - a);
  console.log(nums[1]);
}
