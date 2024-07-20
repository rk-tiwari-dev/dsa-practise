const hash = new Map();
hash.set("apple", 1);
hash.set("banana", 2);
hash.set("cherry", 3);
hash.set("date", 4);
console.log(hash.get("banana")); // 2
hash.delete("banana");
console.log(hash.get("banana")); // undefined
console.log(hash.size); // 3
console.log(hash.has("banana")); // false
hash.clear();
console.log(hash.size); // 0
console.log(hash.has("apple")); // false
console.log(hash.has("banana")); // false
console.log(hash.has("cherry")); // false
for (const [key, value] of hash) {
  console.log(key, value);
}
