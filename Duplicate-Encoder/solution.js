function duplicateEncode(word) {
  let result = [];
  word = word.toLowerCase();
  for (char of word) {
    if (word.indexOf(char) !== word.lastIndexOf(char)) {
      result.push(")");
    } else {
      result.push("(");
    }
  }
  return result.join("")
}