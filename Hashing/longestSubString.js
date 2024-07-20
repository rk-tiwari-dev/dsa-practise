//longestSubString.js
// Find the longest substring with k unique characters in a given string
// Time Complexity: O(n)
// Space Complexity: O(k)
// The longestSubString function takes a string and an integer k as input
// and returns the length of the longest substring with k unique characters.
// The function uses a sliding window approach to find the longest substring with k unique characters.
// The function maintains a hash map to store the frequency of each character in the current window.
// The function also maintains a count of the number of unique characters in the current window.
// The function iterates through the string and expands the window until the number of unique characters exceeds k.
// The function then contracts the window from the left until the number of unique characters is less than or equal to k.
// The function updates the maximum length of the substring seen so far.
// The function returns the maximum length of the substring with k unique characters.
// The function has a time complexity of O(n) and a space complexity of O(k).

function longestSubString(str, k) {
  let map = {};
  let left = 0;
  let maxLen = 0;

  for (let right = 0; right < str.length; right++) {
    let char = str[right];
    map[char] = (map[char] || 0) + 1;
    while (Object.keys(map).length > k) {
      let leftChar = str[left];
      map[leftChar]--;
      if (map[leftChar] === 0) {
        delete map[leftChar];
      }
      left++;
    }

    maxLen = Math.max(maxLen, right - left + 1);
  }

  return maxLen;
}
