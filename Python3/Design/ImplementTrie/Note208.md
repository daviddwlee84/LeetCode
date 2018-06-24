# 208. Implement Trie (Prefix Tree)

## Description

Implement a trie with insert, search, and startsWith methods.

**Example**:

```
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

### Others solution

```python
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

## Resources

[Cracking The Code Interview Author Tutorial](https://youtu.be/zIjfhVPRZCg)