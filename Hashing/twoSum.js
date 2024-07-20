//
//problem states that we have to find the 'indices' of the two numbers such that they add up to a specific target.
//we can use a hash map to store the difference between the target and the current number.
//if the difference is already present in the hash map, we return the indices of the two numbers.
//otherwise, we store the current number in the hash map and continue.
//if no such pair is found, we return an empty array.
// Time Complexity: O(n)
// Space Complexity: O(n)
// The twoSum function takes an array of integers and a target sum as
// and returns an array containing the indices of the two
// numbers that add up to the target sum.
// The function uses a hash map to store the difference between the target sum and the current number.
// It then iterates through the array and checks if the difference is present in the hash map.
// If the difference is found, the function returns the indices of the two numbers.
// If no such pair is found, the function returns an empty array.

function twoSum(arr, target) {
  let map = {};
  for (let i = 0; i < arr.length; i++) {
    let diff = target - arr[i];
    if (map[diff] !== undefined) {
      return [map[diff], i];
    }
    map[arr[i]] = i;
  }
  return [];
}

console.log(twoSum([2, 7, 11, 15], 9)); //[0, 1]
console.log(twoSum([3, 2, 4], 6)); //[1, 2]
