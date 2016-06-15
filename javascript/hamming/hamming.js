"use strict"
function Hamming () {}

Hamming.prototype.compute = (string1, string2) => {
  if (string1.length !== string2.length) {
    throw new Error('DNA strands must be of equal length.')
  }
  let differences = 0
  for (let i = 0; i < string1.length; i++) {
    if (string1[i] !== string2[i]) {
      differences += 1
    }
  }
  return differences
}

module.exports = Hamming;
