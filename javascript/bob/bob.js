//
// This is only a SKELETON file for the "Bob" exercise. It's been provided as a
// convenience to get you started writing code faster.
//

var Bob = function() {};

Bob.prototype.hey = function(input) {
  uppercase = input.match(/[A-Z]/g)
  allUppercase = input === input.toUpperCase()
  questionMark = input[input.length - 1] === "?"
  spaces = input.match(/\ /g)
  if (uppercase && allUppercase) {
    return 'Whoa, chill out!'
  } else if (questionMark) {
    return "Sure."
  } else if (!input || (spaces && spaces.length === input.length)) {
    return "Fine. Be that way!"
  }
  return "Whatever."
};

module.exports = Bob;
