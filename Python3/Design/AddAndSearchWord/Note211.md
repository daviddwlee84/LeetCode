# 211. Add and Search Word - Data structure design

## Description

Design a data structure that supports the following two operations:

```txt
void addWord(word)
bool search(word)
```

search(word) can search a literal word or a regular expression string containing only letters `a-z` or `.`. A `.` means it can represent any one letter.

**Example**:

```txt
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
```

**Note**:

You may assume that all words are consist of lowercase letters `a-z`.

## Solution

### Brute Force - Backtracking and Test for each possible char

### Tire - Backtracking but Only test for visited char

#### Recursive

```py
class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        node = self.root
        self.res = False
        self.dfs(node, word)
        return self.res

    def dfs(self, node, word):
        if not word:
            if node.isWord:
                self.res = True
            return
        if word[0] == ".":
            for n in node.children.values():
                self.dfs(n, word[1:])
        else:
            node = node.children.get(word[0])
            if not node:
                return
            self.dfs(node, word[1:])
```

#### Iterative with stack

```py
class WordNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:
    def __init__(self):
        self.root = WordNode()

    def addWord(self, word):
        node = self.root
        for w in word:
            if w in node.children:
                node = node.children[w]
            else:
                node.children[w] = WordNode()
                node = node.children[w]
        node.isEnd = True

    def search(self, word):
        stack = [(self.root,word)]
        while stack:
            node, w = stack.pop()
            if not w:
                if node.isEnd:
                    return True
            elif w[0]=='.':
                for n in node.children.values():
                    stack.append((n,w[1:]))
            else:
                if w[0] in node.children:
                    n = node.children[w[0]]
                    stack.append((n,w[1:]))
        return False
```

Using pointer instead of slicing

```py
class WordNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:
    WILDCARD = "."

    def __init__(self):
        self.root = WordNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = WordNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        stack = [(self.root, 0)]
        while stack:
            node, i = stack.pop()
            if i == len(word):
                if node.is_end:
                    return True
            elif word[i] == ".":
                for child_char in node.children:
                    stack.append((node.children[child_char], i + 1))
            elif word[i] in node.children:
                stack.append((node.children[word[i]], i + 1))
        return False
```

#### Use dict as Tire node

```py
class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for c in word:
            node = node.setdefault(c, {})
        node['$'] = True

    def search(self, word: str) -> bool:
        return self.searchNode(self.trie, word)

    def searchNode(self, node, word: str) -> bool:
        for i, c in enumerate(word):
            if c == '.':
                return any(self.searchNode(node[w], word[i+1:]) for w in node if w != '$')
            if c not in node: return False
            node = node[c]
        return '$' in node
```
