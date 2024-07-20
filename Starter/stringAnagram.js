function stringAnagram(str) {
  let anagrams = [];
  if (str.length === 1) {
    anagrams.push(str);
    return anagrams;
  }
  for (let i = 0; i < str.length; i++) {
    const prefix = str[i];
    const rest = str.substring(0, i) + str.substring(i + 1);
    const words = stringAnagram(rest);
    for (let j = 0; j < words.length; j++) {
      anagrams.push(prefix + words[j]);
    }
  }
  return anagrams;
}
