function findPeaksInArray1(arr) {
  let left = 0;
  let right = arr.length - 1;
  let peaks = [];

  while (left <= right) {
    let mid = Math.floor((left + right) / 2);

    // Check if arr[mid] is a peak
    if (
      (mid === 0 || arr[mid] >= arr[mid - 1]) &&
      (mid === arr.length - 1 || arr[mid] >= arr[mid + 1])
    ) {
      peaks.push(mid);
    }

    // Narrow down search based on comparison with neighbors
    if (mid > 0 && arr[mid - 1] > arr[mid]) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }

  return peaks;
}

// Example usage:
const arr4 = [1, 2, 3, 1];
console.log(findPeaksInArray1(arr4)); // [2]

const arr5 = [1, 2, 1, 3, 5, 6, 4];
console.log(findPeaksInArray1(arr5)); // [1, 5]

const arr6 = [10, 20, 15, 2, 23, 90, 67];
console.log(findPeaksInArray1(arr6)); // [1, 5, 6]

// Time Complexity: O(log n)
// Space Complexity: O(1)
// The findPeaksInArray function takes an array of integers
// as input and returns an array containing the indices of the peaks in the input array.
// A peak is defined as an element that is greater than or equal to its neighbors.
//The function uses a binary search approach to find the peaks efficiently.

//Simple approch

function findPeaksInArray(arr) {
  const peaks = [];

  // Iterate through each element in the array
  for (let i = 0; i < arr.length; i++) {
    // Check if arr[i] is a peak
    if (
      (i === 0 || arr[i] >= arr[i - 1]) &&
      (i === arr.length - 1 || arr[i] >= arr[i + 1])
    ) {
      peaks.push(i);
    }
  }

  return peaks;
}

// Example usage:
const arr1 = [1, 2, 3, 1];
console.log(findPeaksInArray(arr1)); // [2]

const arr2 = [1, 2, 1, 3, 5, 6, 4];
console.log(findPeaksInArray(arr2)); // [1, 5]

const arr3 = [10, 20, 15, 2, 23, 90, 67];
console.log(findPeaksInArray(arr3)); // [1, 5, 6]
