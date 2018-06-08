# David's LeetCode Practice [![Build Status](https://travis-ci.org/daviddwlee84/LeetCode.svg?branch=master)](https://travis-ci.org/daviddwlee84/LeetCode)

[**LeetCode Algorithms Problems**](https://leetcode.com/problemset/algorithms/)

## Testing (based on [pytest](https://docs.pytest.org/en/latest/contents.html))

Test all the units (in the main directory):

`py.test -v`


## Python3 Progress

### Symbols

* Difficulty:
    * Harder: ▲
    * Same: -
    * Easier: ▼
* Important: *

Number | Difficulty | Problem | Date | Category | Method-TimeComplexity | Remark | TODO |
|-------------:|-------------|-------------| -------------|-------------|-------------| -------------|------|
|001|Easy    |[Two Sum](https://leetcode.com/problems/two-sum/description/)|2018/3/12|Array|[Naive-O(nlogn)](Python3/Array/TwoSum/Naive001.py)|[Note](Python3/Array/TwoSum//Note001.md)|HashTable-O(n)
|002|Medium  |[Add Two Numbers](https://leetcode.com/problems/add-two-numbers/description/)|2018/3/12|Linked List|[Naive-O(n)](Python3/LinkedList/AddTwoNumbers/Naive002.py)|[Note](Python3/LinkedList/AddTwoNumbers//Note002.md)|-
|006|Medium  |[ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/)|2018/3/22|Array|[Naive-O(n)](Python3/Array/ZigZagConversion/Naive006.py)|[Note](Python3/Array/ZigZagConversion/Note006.md)|-
|007|Easy    |[Reverse Integer](https://leetcode.com/problems/reverse-integer/description/)|2018/3/22|Array|[Naive-O(n)](Python3/Array/ReverseInteger/Naive007.py)|[Note](Python3/Array/ReverseInteger/Note007.md)|-
|009|Easy    |[Palindrome Number](https://leetcode.com/problems/palindrome-number/)|2018/3/22|Array|[Naive-O(n)](Python3/Array/PalindromeNumber/Naive009.py), [Without using string-O(n)](Python3/Array/PalindromeNumber/NotString009.py)|[Note](Python3/Array/PalindromeNumber/Note009.md)|-
|024|Medium  |[Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/description/)|2018/5/31|Linked List|[Naive-O(n)](Python3/LinkedList/SwapNodesInPairs/Naive024.py), [Recursive-O(n)](Python3/LinkedList/SwapNodesInPairs/Recursive024.py)|[Note](Python3/LinkedList/SwapNodesInPairs/Note024.md)|-
|046|Medium  |[Permutations](https://leetcode.com/problems/permutations/description/)|2018/5/31|Linked List|[Backtracking-O(n!)](Python3/Array/Permutations/Backtracking046.py), [Recursive-O(n!)](Python3/Array/Permutations/Recursive046.py), [DFS Based-O(n!)](Python3/Array/Permutations/DFS046.py)|[Note](Python3/Array/Permutations/Note046.md)|-
|094|Medium  |[Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/description/)|2018/5/29|Binary Tree|[Recursive-O(n)](Python3/BinaryTree/BinaryTreeInorderTraversal/Recursive94.py), [Iterative-O(n)](Python3/BinaryTree/BinaryTreeInorderTraversal/Iterative94.py)|[Note](Python3/BinaryTree/BinaryTreeInorderTraversal/Note94.md)|-
|102|Medium  |[Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)|2018/6/7|Binary Tree|[BFS-O(n)](Python3/BinaryTree/BinaryTreeLevelOrderTraversal/BFS.py)|[Note](Python3/BinaryTree/BinaryTreeLevelOrderTraversal/Note102.md)|-
|104|Easy    |[Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/)|2018/6/8|Binary Tree|[Top-Down-O(n)](Python3/BinaryTree/MaximumDepthofBinaryTree/TopDown.py), [Bottom-up-O(n)](Python3/BinaryTree/MaximumDepthofBinaryTree/BottomUp.py)|[Note](Python3/BinaryTree/MaximumDepthofBinaryTree/Note104.md)|
|106|Medium  |[Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/)|2018/6/8|Binary Tree|[Divide and Conquer-O(n)](Python3/BinaryTree/ConstructBinaryTreefromInorderandPostorderTraversal/DivideAndConquer.py)|[Note](Python3/BinaryTree/ConstructBinaryTreefromInorderandPostorderTraversal/Note106.md)|-
|144|Medium  |[Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/description/)|2018/5/29|Binary Tree|[Recursive-O(n)](Python3/BinaryTree/BinaryTreePreorderTraversal/Recursive144.py), [Iterative-O(n)](Python3/BinaryTree/BinaryTreePreorderTraversal/Iterative144.py)|[Note](Python3/BinaryTree/BinaryTreePreorderTraversal/Note144.md)|-
|145|Hard ▼ |[Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/description/)|2018/6/2|Binary Tree|[Recursive-O(n)](Python3/BinaryTree/BinaryTreePostorderTraversal/Recursive145.py), [Iterative-O(n)](Python3/BinaryTree/BinaryTreePostorderTraversal/Iterative145.py)|[Note](Python3/BinaryTree/BinaryTreePostorderTraversal/Note145.md)|-

## Resources

### Detail Solutions

* C++
    * [《LeetCode題解》](https://legacy.gitbook.com/book/siddontang/leetcode-solution/details)
* JavaScript
    * [《初學者練習 - LeetCode with Javascript》](https://legacy.gitbook.com/book/skyyen999/-leetcode-with-javascript/details)