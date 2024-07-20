const arr = [1, 5, 3, 5, 20, 45, 34];
function secondLargestInArray(arr) {
  let max = arr[0];
  let secondMax = arr[0]; //make both as fisrt element
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > max) {
      secondMax = max;
      max = arr[i];
    } else if (arr[i] > secondMax) {
      secondMax = arr[i];
    }
  }
  return secondMax;
}

console.log(secondLargestInArray(arr)); //34
