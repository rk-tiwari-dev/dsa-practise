function kadaneAlgo(arr) {
  let maxSum = arr[0];
  let currentSum = arr[0];
  for (let i = 1; i < arr.length; i++) {
    currentSum = Math.max(arr[i], currentSum + arr[i]);
    console.log(currentSum, maxSum + " i is = " + arr[i]);
    maxSum = Math.max(maxSum, currentSum);
  }
  return maxSum;
}

const arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4];
console.log(kadaneAlgo(arr)); //6
// Time Complexity: O(n)
//space complexity: O(1)
// The Kadane's algorithm is a famous algorithm to solve the maximum subarray problem. It is a dynamic programming algorithm that finds the maximum subarray sum for a given array. The algorithm is efficient and has a time complexity of O(n). The algorithm works by iterating through the array and calculating the maximum subarray sum ending at each index. It then updates the maximum subarray sum seen so far.
// The algorithm returns the maximum subarray sum seen so far, which is the maximum subarray sum for the entire array.
// The algorithm works by keeping track of two variables:
//currentSum and maxSum. The currentSum variable stores the maximum subarray sum ending at the current index.
//The maxSum variable stores the maximum subarray sum seen so far.
// The algorithm iterates through the array and calculates the maximum subarray sum ending at each index. It then updates the maxSum variable
// with the maximum subarray sum seen so far.
//The algorithm returns the maxSum variable, which is the maximum subarray sum for the entire array.
