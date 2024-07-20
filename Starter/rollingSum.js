const arr = [1, 5, 3, 5, 20, 45, 34];

function rollingSum(arr) {
  let sum = 0;
  let result = [];
  for (let i = 0; i < arr.length; i++) {
    sum += arr[i];
    result.push(sum);
  }
  return result;
}

console.log(rollingSum(arr)); //[1, 6, 9, 14, 34, 79, 113]
