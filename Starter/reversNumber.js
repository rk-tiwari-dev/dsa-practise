function reverseNumber(n) {
  num = 0;
  while (n > 0) {
    num = num * 10 + (n % 10);
    n = Math.floor(n / 10);
  }
  return num;
}

console.log(reverseNumber(123)); //321
console.log(reverseNumber(12345)); //54321
