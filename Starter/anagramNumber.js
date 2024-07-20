function anagramNumber(num1) {
  let num2 = num1.toString().split("").reverse().join("");
  return num1 === parseInt(num2);
}
