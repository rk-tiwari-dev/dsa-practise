// Group Anagrams together
// Time Complexity: O(n * m * log(m)) where n is the number of strings and m is the length of the string
// Space Complexity: O(n)
// The groupAnagrams function takes an array of strings as input and groups the anagrams together.
// The function uses a hash map to store the sorted version of each string and the corresponding anagrams.
// It then iterates through the array of strings and groups the anagrams together based on the sorted version.
// The function returns an array of arrays, where each inner array contains the anagrams grouped together.
// The function has a time complexity of O(n * m * log(m)) where n is the number of strings and m is the length of the string.
// The function has a space complexity of O(n).

function groupAnagrams(strs) {
  let map = {};
  for (let str of strs) {
    let sorted = str.split("").sort().join("");
    //console.log(sorted);
    if (map[sorted] === undefined) {
      map[sorted] = [str];
    } else {
      map[sorted].push(str);
    }
  }
  return Object.values(map);
}

console.log(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]));
// [["eat","tea","ate"],["tan","nat"],["bat"]]
console.log(groupAnagrams(["a"]));
// [["a"]]
console.log(groupAnagrams([""]));
// [[""]]
console.log(groupAnagrams([]));
// []
