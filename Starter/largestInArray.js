const arr = [1, 5, 3, 5, 20, 45, 34];
function largestInArray(arr) {
  let max = arr[0];
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > max) {
      max = arr[i];
    }
  }
  return max;
}

console.log(largestInArray(arr)); //45
