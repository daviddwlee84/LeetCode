# 208. Implement Trie (Prefix Tree)

## Description

Implement a trie with insert, search, and startsWith methods.

**Example**:

```txt
Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
```

**Note**:

* You may assume that all inputs are consist of lowercase letters a-z.
* All inputs are guaranteed to be non-empty strings.

## Solution

* Manipulate another data structure: Multiple-child tree
  * Each node store a character
  * Use hash table to store all the children of a node
  * Use a flag to determine whether it is the end of any word

* For each method just travel all the node contain the word's character and check if it fufill the condition

### Others' solution

* [Official Solution](https://leetcode.com/problems/implement-trie-prefix-tree/solution/)

Use pure dict without create trie node object

```py
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        n = self.root
        for c in word:
            n = n.setdefault(c, {})
        n['$'] = True

    def search(self, word, isprefix=False):
        n = self.root
        for c in word + ('' if isprefix else '$'):
            if not c in n:
                return False
            n = n[c]
        return True

    def startsWith(self, prefix):
        return self.search(prefix, isprefix=True)
```

```py
class Trie:
    def __init__(self):
        self.trie = {}   # using dictionary of dictionary for trie

    def insert(self, word: str) -> None:
        t = self.trie
        for char in word:
            if char not in t:
                t[char] = {}    # initialising new char as key with empty dictionary value
            t = t[char]         # move inside the char value (sub dictionaries)
        t['#'] = '#'            # ending word with # as key and value

    def search(self, word: str) -> bool:
        t = self.trie
        for char in word:
            if char not in t:   # curr character is not present
                return False
            t = t[char]         # narrow down to sub dcitionary
        if '#' in t:            # reached to the end of a word
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        t = self.trie
        for char in prefix:
            if char not in t:   # curr character is not present
                return False
            t = t[char]
        return True             # prefix present

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```

## Resources

* [Cracking The Code Interview Author Tutorial](https://youtu.be/zIjfhVPRZCg)
