#!/usr/bin/node
const args = process.argv.slice(2).map(Number);

if (args.length < 2) {
  console.log(0);
} else {
  const max = Math.max(...args);
  const secondMax = args.reduce((acc, cur) => {
    if (cur !== max && cur > acc) {
      return cur;
    }
    return acc;
  }, -Infinity);
  console.log(secondMax);
}
