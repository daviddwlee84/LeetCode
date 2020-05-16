# [Trie (Prefix Tree)](https://leetcode.com/explore/learn/card/trie)

* [Implement Trie (Prefix Tree) - LeetCode](https://leetcode.com/problems/implement-trie-prefix-tree/solution/) - [Note](../../Python3/Design/ImplementTrie/Note208.md)

## Overview

### Introduction

`Trie`, also called `prefix tree`, is a special form of a `Nary tree`.

In this card, we will go deep into the implementation of Trie and talk about how to use this data structure to solve problems.

After completing this card, you should be able to:

1. Understand the concept of Trie;
2. Do insertion and search operations in a Trie;
3. Understand how Trie helps in practical application;
4. Solve practical problems using Trie.

### Application

Trie (we pronounce "try") or prefix tree is a tree data structure, which is used for retrieval of a key in a dataset of strings. There are various applications of this very efficient data structure such as:

1. Autocomplete
2. Spell checker
3. IP routing (Longest prefix matching)
4. T9 (Text on 9 keys, was used on phones to input text) predictive text
5. Solving word games

### Why Trie for search a word?

There are several other data structures, like balanced trees and hash tables, which give us the possibility to search for a word in a dataset of strings. Then why do we need trie? Although hash table has O(1) time complexity for looking for a key, it is not efficient in the following operations :

* Finding all keys with a common prefix.
* Enumerating a dataset of strings in lexicographical order.

Another reason why trie outperforms hash table, is that as hash table increases in size, there are lots of hash collisions and the search time complexity could deteriorate to O(n), where nn is the number of keys inserted. Trie could use less space compared to Hash Table when storing many keys with the same prefix. In this case using trie has only O(m) time complexity, where m is the key length. Searching for a key in a balanced tree costs O(mlogn) time complexity.

## Introduction To Trie

### What is Trie?

A Trie is a special form of a Nary tree. Typically, a trie is used to store strings. *Each Trie node represents a string (a prefix)*. Each node might have several children nodes while the paths to different children nodes represent different characters. And the strings the child nodes represent will be the origin string represented by the node itself plus the character on the path.

Here is an example of a trie:

![example](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/07/screen-shot-2018-01-31-at-163403.png)

In the example, the value we mark in each node is the string the node represents. For instance, we start from the root node and choose the second path 'b', then choose the first child 'a', and choose child 'd', finally we arrived at the node "bad". The value of the node is exactly formed by the letters in the path from the root to the node sequentially.

It is worth noting that the root node is associated with the empty string.

One important property of Trie is that all the descendants of a node have a common prefix of the string associated with that node. That's why Trie is also called prefix tree.

Let's look at the example again. For example, the strings represented by nodes in the subtree rooted at node "b" have a common prefix "b". And vice versa. The strings which have the common prefix "b" are all in the subtree rooted at node "b" while the strings with different prefixes will come to different branches.

Trie is widely used in various applications, such as autocomplete, spell checker, etc. We will introduce the practical applications in later chapters.

### How to represent a Trie?

#### Trie node structure

Trie is a rooted tree. Its nodes have the following fields:

* Maximum of R links to its children, where each link corresponds to one of R character values from dataset alphabet. In this article we assume that R is 26, the number of lowercase latin letters.
* Boolean field which specifies whether the node corresponds to the end of the key, or is just a key prefix.

![trie node structure](https://leetcode.com/media/original_images/208_Node.png)

#### First Solution - Array

The first solution is to use an array to store children nodes.

For instance, if we store strings which only contains letter a to z, we can declare an array whose size is 26 in each node to store its children nodes. And for a specific character c, we can use c - 'a' as the index to find the corresponding child node in the array.

```cpp
// change this value to adapt to different cases
#define N 26

struct TrieNode {
    TrieNode* children[N];
    // you might need some extra values according to different cases
};

/** Usage:
 *  Initialization: TrieNode root = new TrieNode();
 *  Return a specific child node with char c: (root->children)[c - 'a']
 */
```

It is really fast to visit a child node. It is comparatively easy to visit a specific child since we can easily transfer a character to an index in most cases. But not all children nodes are needed. So there might be some *waste of space*.

#### Second Solution - Map

The second solution is to use a hashmap to store children nodes.

We can declare a hashmap in each node. The key of the hashmap are characters and the value is the corresponding child node.

```cpp
struct TrieNode {
    unordered_map<char, TrieNode*> children;
    // you might need some extra values according to different cases
};

/** Usage:
 *  Initialization: TrieNode root = new TrieNode();
 *  Return a specific child node with char c: (root->children)[c]
 */
```

It is even easier to visit a specific child directly by the corresponding character. But it *might be a little slower than using an array*. However, it *saves some space* since we only store the children nodes we need. It is also *more flexible* because we are not limited by a fixed length and fixed range.

#### More

We mentioned how to represent the children nodes in Trie node. Besides, we might need some other values.

For example, as we know, each Trie node represents a string but not all the strings represented by Trie nodes are meaningful. *If we only want to store words in a Trie, we might declare a boolean in each node as a flag to indicate if the string represented by this node is a word or not*.

## Basic Operations

### Insertion in Trie

When we insert a target value into a BST, in each node, we need to decide which child node to go according to the relationship between the value of the node and the target value. Similarly, *when we insert a target value into a Trie, we will also decide which path to go depending on the target value we insert.*

To be more specific, if we insert a string S into Trie, we start with the root node. We will choose a child or add a new child node depending on S[0], the first character in S. Then we go down to the second node and we will make a choice according to S[1]. Then we go down to the third node, so on and so for. Finally, we traverse all characters in S sequentially and reach the end. The end node will be the node which represents the string S.

Let's summarize the strategy using pseudo-code:

```txt
1. Initialize: cur = root
2. for each char c in target string S:
3.      if cur does not have a child c:
4.          cur.children[c] = new Trie node
5.      cur = cur.children[c]
6. cur is the node which represents the string S
```

Usually, you will need to build the trie by yourself. Building a trie is actually to call the insertion function several times. But remember to initialize a root node before you insert the strings.

---

We insert a key by searching into the trie. We start from the root and search a link, which corresponds to the first key character. There are two cases :

* A link exists. Then we move down the tree following the link to the next child level. The algorithm continues with searching for the next key character.
* A link does not exist. Then we create a new node and link it with the parent's link matching the current key character. We repeat this step until we encounter the last character of the key, then we mark the current node as an end node and the algorithm finishes.

Complexity Analysis

* Time complexity : O(m), where m is the key length.

In each iteration of the algorithm, we either examine or create a node in the trie till we reach the end of the key. This takes only m operations.

* Space complexity : O(m).

In the worst case newly inserted key doesn't share a prefix with the the keys already inserted in the trie. We have to add m new nodes, which takes us O(m) space.

### Search in Trie

As we mentioned in the introduction to Trie, all the descendants of a node have a common prefix of the string associated with that node. Therefore, it should be easy to search if there are any words in the trie that starts with the given prefix.

Similarly, we can go down the tree depending on the given prefix. Once we can not find the child node we want, search fails. Otherwise, search succeeds. To be more specific, we provide several examples:

Let's summarize the strategy using pseudo-code:

```txt
1. Initialize: cur = root
2. for each char c in target string S:
3.      if cur does not have a child c:
4.          search fails
5.      cur = cur.children[c]
6. search successes
```

---

The approach is very similar to the one we used for searching a key in a trie. We traverse the trie from the root, till there are no characters left in key prefix or it is impossible to continue the path in the trie with the current key character. The only difference with the mentioned above search for a key algorithm is that when we come to an end of the key prefix, we always return true. We don't need to consider the isEnd mark of the current trie node, because we are searching for a prefix of a key, not for a whole key.

Complexity Analysis

* Time complexity : O(m)O(m)
* Space complexity : O(1)O(1)

#### Search Word

You might also want to know how to search for a specific word rather than a prefix. We can treat this word as a prefix and search in the same way we mentioned above.

1. If search fails which means that no words start with the target word, the target word is definitely not in the Trie.
2. If search succeeds, we need to check if the target word is only a prefix of words in Trie or it is exactly a word. To solve this problem, you might want to modify the node structure a little bit.

> Hint: A boolean flag in each node might work.

---

Each key is represented in the trie as a path from the root to the internal node or leaf. We start from the root with the first key character. We examine the current node for a link corresponding to the key character. There are two cases:

* A link exist. We move to the next node in the path following this link, and proceed searching for the next key character.
* A link does not exist. If there are no available key characters and current node is marked as isEnd we return true. Otherwise there are possible two cases in each of them we return false :
  * There are key characters left, but it is impossible to follow the key path in the trie, and the key is missing.
  * No key characters left, but current node is not marked as isEnd. Therefore the search key is only a prefix of another key in the trie.

Complexity Analysis

* Time complexity : O(m) In each step of the algorithm we search for the next key character. In the worst case the algorithm performs mm operations.
* Space complexity : O(1)

## Resources

* [How to create a trie in Python - Stack Overflow](https://stackoverflow.com/questions/11015320/how-to-create-a-trie-in-python)

### Tutorial

* [Cracking The Code Interview Author Tutorial](https://youtu.be/zIjfhVPRZCg)
