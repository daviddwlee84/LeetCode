# David's LeetCode Practice [![Build Status](https://travis-ci.org/daviddwlee84/LeetCode.svg?branch=master)](https://travis-ci.org/daviddwlee84/LeetCode)

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
* Good: 👍

### Abbreviation

* Algorithm
    * DP - Dynamic Programming
    * DC - Divide and Conquer
* Data Structure
    * HT - Hash Table
    * BST - Binary Search Tree
* Others
    * BM - Bit Manipulation

### Remark

* Catagory
    * `Catagory1, Catagory2, ...`
    * Usually record in Data Structure. (The Algorithm strategy will be noted in the Method field)
    * Code will be put in the main catagory folder (i.e. the first one).
    * Some catagory may be the Related Topic tags marked by LeetCode.
    * TODO: Most of the categories need to be updated. (The date before 2018/9/22)

|Number | Difficulty | Problem | Date | Category | Method-TimeComplexity | Remark | TODO |
|-------------:|-------------|-------------|-------------|-------------|-------------|-------------|------|
|👍 001|Easy    |[Two Sum](https://leetcode.com/problems/two-sum/)|2018/3/12|Array, HT|[Naive-O(nlogn)](Python3/Array/TwoSum/Naive001.py), [HT-O(n)](Python3/Array/TwoSum/HashTable001.py), [Sorted HT-O(n)](Python3/Array/TwoSum/SortedHashTable001.py)|[Note](Python3/Array/TwoSum//Note001.md)|-
|  002|Medium  |[Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)|2018/3/12|Linked List|[Naive-O(n)](Python3/LinkedList/AddTwoNumbers/Naive002.py)|[Note](Python3/LinkedList/AddTwoNumbers/Note002.md)|Make a shorter version
|👍 003|Medium *|[Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)|2018/9/24|String, HT|[Sliding Window](Python3/String/LongestSubstringWithoutRepeatingCharacters/SlidingWindow003.py), [Sliding Window Optimized](Python3/String/LongestSubstringWithoutRepeatingCharacters/SlidingWindowOptimized003.py)|[Note](Python3/String/LongestSubstringWithoutRepeatingCharacters/Note003.md)|-
|👍 005|Medium *|[Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)|2019/2/28|String, DP|[Naive-O(n³)](Python3/String/LongestPalindromicSubstring/Naive005.py), [DP-O(n²)](Python3/String/LongestPalindromicSubstring/DP005.py), [Expand Around Center-O(n²)](Python3/String/LongestPalindromicSubstring/ExpandAroundCenter005.py)|[Note](Python3/String/LongestPalindromicSubstring/Note005.md)|-
|  006|Medium  |[ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/)|2018/3/22|Array|[Naive-O(n)](Python3/Array/ZigZagConversion/Naive006.py)|[Note](Python3/Array/ZigZagConversion/Note006.md)|-
|  007|Easy    |[Reverse Integer](https://leetcode.com/problems/reverse-integer/)|2018/3/22|Array|[Naive-O(n)](Python3/Array/ReverseInteger/Naive007.py)|[Note](Python3/Array/ReverseInteger/Note007.md)|-
|  008|Medium  |[String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)|2018/9/30|String|[Naive-O(n)](Python3/String/StringToInteger/Naive008.py)|[Note](Python3/String/StringToInteger/Note008.md)|-
|  009|Easy    |[Palindrome Number](https://leetcode.com/problems/palindrome-number/)|2018/3/22|Array|[Naive-O(n)](Python3/Array/PalindromeNumber/Naive009.py), [Without using string-O(n)](Python3/Array/PalindromeNumber/NotString009.py)|[Note](Python3/Array/PalindromeNumber/Note009.md)|-
|  010|Hard *  |[Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)|2018/10/13|String|[DC-O((m+n)*2ⁿ)](Python3/String/RegularExpressionMatching/DC010.py), [Top-Down DP-O(mn)](Python3/String/RegularExpressionMatching/TopDownDP010.py), [Bottom-Up DP-O(mn)](Python3/String/RegularExpressionMatching/BottomUpDP010.py)|[Note](Python3/String/RegularExpressionMatching/Note010.md)|-
|  011|Medium  |[Container With Most Water](https://leetcode.com/problems/container-with-most-water/)|2018/9/22|Array|[Naive-O(n²)](Python3/Array/ContainerWithMostWater/Naive011.py), [TwoPointer-O(n)](Python3/Array/ContainerWithMostWater/TwoPointer011.py)|[Note](Python3/Array/ContainerWithMostWater/Note011.md)|-
|  012|Medium  |[Integer to Roman](https://leetcode.com/problems/integer-to-roman/)|TODO|String|[Naive-O(n)](Python3/String/IntegerToRoman/Naive012.py)|[Note](Python3/String/IntegerToRoman/Note012.md)|-
|  013|Eazy    |[Roman to Integer](https://leetcode.com/problems/roman-to-integer/)|2018/9/29|String|[Naive-O(n)](Python3/String/RomanToInteger/Naive013.py)|[Note](Python3/String/RomanToInteger/Note013.md)|-
|  014|Eazy    |[Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)|2018/9/16|Array|[Naive-O(n*len)](Python3/Array/LongestCommonPrefix/Naive014.py)|[Note](Python3/Array/LongestCommonPrefix/Note014.md)|-
|  015|Medium ▲|[3Sum](https://leetcode.com/problems/3sum/)|2018/10/13|Array|[TwoPointer-O(n²)](Python3/Array/3Sum/TwoPointer015.py)|[Note](Python3/Array/3Sum/Note015.md)|Try other apporach
|  016|Medium  |[3Sum Closest](https://leetcode.com/problems/3sum-closest/)|2018/10/13|Array|[TwoPointer-O(n²)](Python3/Array/3SumClosest/TwoPointer016.py)|[Note](Python3/Array/3SumClosest/Note016.md)|-
|  017|Medium  |[Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)|2019/3/1|String|[Backtracking-O(n!)](Python3/String/LetterCombinationsOfAPhoneNumber/Backtracking017.py)|[Note](Python3/String/LetterCombinationsOfAPhoneNumber/Note017.md)|-
|👍 018|Medium ▲|[4Sum](https://leetcode.com/problems/4sum/)|2019/3/2|Array, HT|[GeneralizedTwoPointer-O(n³)](Python3/Array/4Sum/GeneralizedTwoPointer018.py)|[Note](Python3/Array/4Sum/Note018.md)|-
|   019|Medium  |[Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)|2019/3/3|Linked List|[HT-O(n)](Python3/LinkedList/RemoveNthNodeFromEndOfList/HT019.py)|[Note](Python3/LinkedList/RemoveNthNodeFromEndOfList/Note019.md)|Two Pointer (reduce space complexity)
|👍 020|Eazy    |[Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)|2018/9/15|String, Stack|[Naive-O(n)](Python3/String/ValidParentheses/Naive020.py), [HashTable-O(n)](Python3/String/ValidParentheses/Dict020.py)|[Note](Python3/String/ValidParentheses/Note020.md)|-
|  021|Eazy    |[Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)|2018/6/27|Linked List|[Better-O(n)](Python3/LinkedList/MergeTwoSortedLists/Better021.py)|[Note](Python3/LinkedList/MergeTwoSortedLists/Note021.md)|-
|  023|Hard    |[Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)|2018/6/26|Linked List|[Naive-O(kn)](Python3/LinkedList/MergeKSortedLists/Naive023.py), [DC-O(nlogk)](Python3/LinkedList/MergeKSortedLists/DC023.py)|[Note](Python3/LinkedList/MergeKSortedLists/Note023.md)|Compare K each time, Heap, attrgetter
|  022|Medium  |[Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)|2019/3/6|String|[Backtracking-O(n!)](Python3/String/GenerateParentheses/Backtracking022.py)|[Note](Python3/String/GenerateParentheses/Note022.md)|-
|  024|Medium  |[Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)|2018/5/31|Linked List|[Naive-O(n)](Python3/LinkedList/SwapNodesInPairs/Naive024.py), [Recursive-O(n)](Python3/LinkedList/SwapNodesInPairs/Recursive024.py)|[Note](Python3/LinkedList/SwapNodesInPairs/Note024.md)|-
|  026|Easy    |[Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)|2018/6/14|Array|[Naive-O(n)](Python3/Array/RemoveDuplicatesfromSortedArray/Naive026.py), [Better-O(n)](Python3/Array/RemoveDuplicatesfromSortedArray/Better026.py)|[Note](Python3/Array/RemoveDuplicatesfromSortedArray/Note026.md)|-
|  027|Easy    |[Remove Element](https://leetcode.com/problems/remove-element/)|2019/7/2|Array|[Naive-O(n)](Python3/Array/RemoveElement/Naive027.py), [Naive2-O(n)](Python3/Array/RemoveElement/Naive2027.py)|[Note](Python3/Array/RemoveElement/Note027.md)|-
|  028|Easy    |[Implement strStr()](https://leetcode.com/problems/implement-strstr/)|2019/7/2|String|[Naive-O(n)](Python3/String/Implement_strStr/Naive028.py)|[Note](Python3/String/Implement_strStr/Note028.md)|-
|  031|Medium ▲|[Next Permutation](https://leetcode.com/problems/next-permutation/)|2019/3/4|Array|[SinglePass-O(n)](Python3/Array/NextPermutation/SinglePass031.py)|[Note](Python3/Array/NextPermutation/Note031.md)|Permutation with duplicates
|  033|Medium  |[Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)|2019/3/5|Array|[BinarySearch-O(log(n))](Python3/Array/SearchInRotatedSortedArray/BinarySearch033.py)|[Note](Python3/Array/SearchInRotatedSortedArray/Note033.md)|-
|👍 035|Easy    |[Search Insert Position](https://leetcode.com/problems/search-insert-position/)|2019/7/3|Array|[BinarySearch-O(log(n))](Python3/Array/SearchInsertPosition/BinarySearch035.py)|[Note](Python3/Array/SearchInsertPosition/Note035.md)|-
|  036|Medium ▼|[Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)|2018/6/21|Array|[HT-O(n)](Python3/Array/ValidSudoku/HashTable036.py)|[Note](Python3/Array/ValidSudoku/Note036.md)|-
|  037|Hard    |[Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)|TODO|Array||[Note](Python3/Array/SudokuSolver/Note037.md)|-
|  039|Medium  |[Combination Sum](https://leetcode.com/problems/combination-sum/)|2019/3/7|Array|[Backtracking-O(n!)](Python3/Array/CombinationSum/Backtracking039.py)|[Note](Python3/Array/CombinationSum/Note039.md)|improve time complexity by not use sort
|👍 046|Medium *|[Permutations](https://leetcode.com/problems/permutations/)|2018/5/31|Array|[Backtracking-O(n!)](Python3/Array/Permutations/Backtracking046.py), [Recursive-O(n!)](Python3/Array/Permutations/Recursive046.py), [DFS Based-O(n!)](Python3/Array/Permutations/DFS046.py)|[Note](Python3/Array/Permutations/Note046.md)|-
|  053|Easy ▲  |[Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)|2018/6/12|Array, DP, DC|[BruteForce-O(n³)](Python3/Array/MaximumSubarray/Naive053.py), [DP-O(n)](Python3/Array/MaximumSubarray/DP053.py), [DC-O(nlogn)](Python3/Array/MaximumSubarray/DC053.py)|[Note](Python3/Array/MaximumSubarray/Note053.md)|-
|  070|Easy    |[Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)|2018/6/13|DP|[DP-O(n)](Python3/DynamicProgramming/ClimbingStairs/DP070.py), [Recursive-O(n)](Python3/DynamicProgramming/ClimbingStairs/Recursive070.py)|[Note](Python3/DynamicProgramming/ClimbingStairs/Note070.md)|-
|👍 078|Medium  |[Subsets](https://leetcode.com/problems/subsets/)|2018/6/27|BM|[Binary-O(2ⁿ)](Python3/BitManipulation/Subsets/Binary078.py), [DFSBased-O(2ⁿ)](Python3/BitManipulation/Subsets/DFS078.py), [Backtracking-O(2ⁿ)](Python3/BitManipulation/Subsets/Backtracking078.py)|[Note](Python3/BitManipulation/Subsets/Note078.md)|-
|  094|Medium  |[Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)|2018/5/29|Binary Tree|[Recursive-O(n)](Python3/BinaryTree/BinaryTreeInorderTraversal/Recursive94.py), [Iterative-O(n)](Python3/BinaryTree/BinaryTreeInorderTraversal/Iterative94.py)|[Note](Python3/BinaryTree/BinaryTreeInorderTraversal/Note94.md)|-
|  098|Medium ▼|[Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)|2018/6/25|BST|[Inorder-O(n)](Python3/BinaryTree/ValidateBinarySearchTree/InorderTraversal098.py), [DFS-O(n)](Python3/BinaryTree/ValidateBinarySearchTree/DFS098.py)|[Note](Python3/BinaryTree/ValidateBinarySearchTree/Note098.md)|-
|👍 101|Easy ▲  |[Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)|2018/6/8|Binary Tree|[Recursive-O(n)](Python3/BinaryTree/SymmetricTree/Recursive101.py), [Iterative-O(n)](Python3/BinaryTree/SymmetricTree/Iterative101.py)|[Note](Python3/BinaryTree/SymmetricTree/Note101.md)|-
|  102|Medium  |[Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)|2018/6/7|Binary Tree|[BFS-O(n)](Python3/BinaryTree/BinaryTreeLevelOrderTraversal/BFS102.py)|[Note](Python3/BinaryTree/BinaryTreeLevelOrderTraversal/Note102.md)|-
|  104|Easy    |[Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)|2018/6/8|Binary Tree|[Top-Down-O(n)](Python3/BinaryTree/MaximumDepthofBinaryTree/TopDown104.py), [Bottom-up-O(n)](Python3/BinaryTree/MaximumDepthofBinaryTree/BottomUp104.py), [Top-Down2-O(n)](Python3/BinaryTree/MaximumDepthofBinaryTree/TopDown104_2.py)|[Note](Python3/BinaryTree/MaximumDepthofBinaryTree/Note104.md)|-
|  105|Medium  |[Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)|2018/6/9|Binary Tree|[DC-O(n)](Python3/BinaryTree/ConstructBinaryTreefromPreorderandInorderTraversal/DivideAndConquer105.py)|[Note](Python3/BinaryTree/ConstructBinaryTreefromPreorderandInorderTraversal/Note105.md)|-
|  106|Medium  |[Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)|2018/6/8|Binary Tree|[DC-O(n)](Python3/BinaryTree/ConstructBinaryTreefromInorderandPostorderTraversal/DivideAndConquer106.py)|[Note](Python3/BinaryTree/ConstructBinaryTreefromInorderandPostorderTraversal/Note106.md)|-
|👍 112|Easy    |[Path Sum](https://leetcode.com/problems/path-sum/)|2018/6/8|Binary Tree|[Naive-O(n)](Python3/BinaryTree/PathSum/Naive112.py)|[Note](Python3/BinaryTree/PathSum/Note112.md)|Can be imporved
|  116|Medium  |[Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)|TODO|Tree|[DFS-O(n)](Python3/BinaryTree/PopulatingNextRightPointersInEachNode/DFS116.py)|[Note](Python3/BinaryTree/PopulatingNextRightPointersInEachNode/Note116.md)|-
|  121|Easy    |[Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)|2018/6/13|DP|[DP-O(n)](Python3/DynamicProgramming/BestTimetoBuyandSellStock/DP121.py)|[Note](Python3/DynamicProgramming/BestTimetoBuyandSellStock/Note121.md)|-
|  122|Easy    |[Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)|2018/6/14|Array|[Greedy-O(n)](Python3/Array/BestTimetoBuyandSellStockII/Greedy122.py), [Tricky-O(n)](Python3/Array/BestTimetoBuyandSellStockII/Tricky122.py)|[Note](Python3/Array/BestTimetoBuyandSellStockII/Note122.md)|-
|  144|Medium  |[Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)|2018/5/29|Binary Tree|[Recursive-O(n)](Python3/BinaryTree/BinaryTreePreorderTraversal/Recursive144.py), [Iterative-O(n)](Python3/BinaryTree/BinaryTreePreorderTraversal/Iterative144.py)|[Note](Python3/BinaryTree/BinaryTreePreorderTraversal/Note144.md)|-
|  145|Hard ▼  |[Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)|2018/6/2|Binary Tree|[Recursive-O(n)](Python3/BinaryTree/BinaryTreePostorderTraversal/Recursive145.py), [Iterative-O(n)](Python3/BinaryTree/BinaryTreePostorderTraversal/Iterative145.py)|[Note](Python3/BinaryTree/BinaryTreePostorderTraversal/Note145.md)|-
|  146|Hard ▼  |[LRU Cache](https://leetcode.com/problems/lru-cache/)|2018/6/25|Design|[Naive](Python3/Design/LRUCache/Naive146.py), [OrderedDict](Python3/Design/LRUCache/OrderedDict146.py)|[Note](Python3/Design/LRUCache/Note146.md)|DoubleLinkedList
|  155|Easy    |[Min Stack](https://leetcode.com/problems/min-stack/)|2018/6/28|Design|[Naive](Python3/Design/MinStack/Naive155.py), [Improve](Python3/Design/MinStack/Improve155.py)|[Note](Python3/Design/MinStack/Note155.md)|-
|  189|Easy    |[Rotate Array](https://leetcode.com/problems/rotate-array/)|2018/6/14|Array|[NaiveInPlace-O(k)](Python3/Array/RotateArray/NaiveInPlace189.py), [ExtraArray-O(n)](Python3/Array/RotateArray/UseArray189.py), [Simplest-O(n)](Python3/Array/RotateArray/Simplest189.py)|[Note](Python3/Array/RotateArray/Note189.md)|Cyclic Replacements / Reverse
|  198|Easy    |[House Robber](https://leetcode.com/problems/house-robber/)|2018/6/14|DP|[DP-O(n)](Python3/DynamicProgramming/HouseRobber/DP198.py)|[Note](Python3/DynamicProgramming/HouseRobber/Note198.md)|Can improve space complexity
|👍 200|Medium  |[Number of Islands](https://leetcode.com/problems/number-of-islands/)|2019/7/5|Search|[BFS-O(n²)](Python3/Search/NumberOfIslands/BFS200.py)|[Note](Python3/Search/NumberOfIslands/Note200.md)|try Union, DFS
|  206|Easy    |[Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)|2018/6/26|Linked List|[Iterative-O(n)](Python3/LinkedList/ReverseLinkedList/Iterative206.py), [Recursive-O(n)](Python3/LinkedList/ReverseLinkedList/Recursive206.py)|[Note](Python3/LinkedList/ReverseLinkedList/Note206.md)|-
|👍 208|Medium *|[Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)|2018/6/24|Design|[Trie](Python3/Design/ImplementTrie/Trie208.py)|[Note](Python3/Design/ImplementTrie/Note208.md)|-
|  225|Easy    |[Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)|2018/6/24|Design|[TwoQueue](Python3/Design/ImplementStackusingQueues/TwoQueue225.py)|[Note](Python3/Design/ImplementStackusingQueues/Note225.md)|-
|  232|Easy    |[Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)|2018/6/24|Design|[TwoStack](Python3/Design/ImplementQueueusingStacks/TwoStack232.py)|[Note](Python3/Design/ImplementQueueusingStacks/Note232.md)|-
|  236|Medium  |[Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)|2018/6/10|Binary Tree|[Naive-O(n)](Python3/BinaryTree/LowestCommonAncestorofaBinaryTree/Naive236.py)|[Note](Python3/BinaryTree/LowestCommonAncestorofaBinaryTree/Note236.md)|Maybe has another approach
|👍 257|Easy ▲  |[Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/)|2018/6/11|Binary Tree|[Iterative-O(n)](Python3/BinaryTree/BinaryTreePaths/Iterative257.py), [Recursive-O(n)](Python3/BinaryTree/BinaryTreePaths/Recursive257.py)|[Note](Python3/BinaryTree/BinaryTreePaths/Note257.md)|-
|  297|Hard    |[Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)|TODO|Binary Tree||[Note](Python3/BinaryTree/SerializeandDeserializeBinaryTree/Note297.md)|-
|  460|Hard    |[LFU Cache](https://leetcode.com/problems/lfu-cache/)|2018/6/25|Design|[Naive](Python3/Design/LFUCache/Naive460.py)|[Note](Python3/Design/LFUCache/Note460.md)|OrderedDict, LinkedList
|  687|Medium  |[Longest Univalue Path](https://leetcode.com/problems/longest-univalue-path/)|TODO|Binary Tree||[Note](Python3/BinaryTree/LongestUnivaluePath/Note687.md)|-
|👍 752|Medium  |[Open the Lock](https://leetcode.com/problems/open-the-lock/)|2019/7/5|Search|[BFS-O(n²)](Python3/Search/OpenTheLock/BFS752.py)|[Note](Python3/Search/OpenTheLock/Note752.md)|Improve time complexity
|  801|Medium  |[Minimum Swaps To Make Sequences Increasing](https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/)|TODO|Array||[Note](Python3/Array/MinimumSwapsToMakeSequencesIncreasing/Note801.md)|-

## LeetCode Learn Progress

> [LeetCode Explore Learn](https://leetcode.com/explore/learn/)

Introduction to Algorithm

* [Recursion I](https://leetcode.com/explore/learn/card/recursion-i/)

Introduction to Data Structure

* [Binary Tree](https://leetcode.com/explore/learn/card/data-structure-tree/)
* [Queue & Stack](https://leetcode.com/explore/learn/card/queue-stack/) - [note](Notes/QueueStack.md)
* [Binary Search Tree](https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/)
* [Trie](https://leetcode.com/explore/learn/card/trie)

Design        |  Date   |   Category   |  Implementaiton  |  Remark  | TODO |
--------------|---------|--------------|------------------|----------|------|
Circular Queue|2019/7/4 |Data Structure|[C++](Learn/Cpp/Queue/CircularQueue.cpp)|[Note](Notes/QueueStack.md#Circular-Queue)|-

## DIY Progress

### Data Structure

|Difficulty | Problem | Date | Category | Method-TimeComplexity | Remark | TODO |
|-------------|-------------|-------------|-------------|-------------|-------------|------|
|Easy    |Linked List|2018/3/12|Linked List|[Singly-Linked List](Python3/LinkedList/ListNodeModule.py)|-|Double-Linked List
|Medium *|Binary Heap (Min/Max Heap)|2018/6/28|Design|[Binary Heap](Python3/Design/BinaryHeap/BinaryHeap.py)|[Note](Python3/Design/BinaryHeap/BinaryHeap.md)|-

### Classic Algorithm Problem

|Difficulty | Problem | Date | Category | Method-TimeComplexity | Remark | TODO |
|-------------|-------------|-------------|-------------|-------------|-------------|------|
|Easy    |Linked List|2018/3/12|Linked List|[Singly-Linked List](Python3/LinkedList/ListNodeModule.py)|-|Double-Linked List
|Medium *|Binary Heap (Min/Max Heap)|2018/6/28|Design|[Binary Heap](Python3/Design/BinaryHeap/BinaryHeap.py)|[Note](Python3/Design/BinaryHeap/BinaryHeap.md)|-

## Notes

* [Binary Tree](python3/BinaryTree/BinaryTree.md)
* [Dynamic Programming](python3/DynamicProgramming/DynamicProgramming.md)

## Resources

* [LeetFree](https://www.leetfree.com/)
* [Codeforces](http://codeforces.com/)

### LeetCode Links

* [**LeetCode Algorithms Problems**](https://leetcode.com/problemset/algorithms/)

#### Top Interview Questions

* [Top Interview Questions - Easy Collection](https://leetcode.com/explore/interview/card/top-interview-questions-easy/)
* [Top Interview Questions - Medium Collection](https://leetcode.com/explore/interview/card/top-interview-questions-medium/)
* [Top Interview Questions - Hard Collection](https://leetcode.com/explore/interview/card/top-interview-questions-hard/)

### Detail Solutions

* C++
    * [《LeetCode題解》](https://legacy.gitbook.com/book/siddontang/leetcode-solution/details)
* JavaScript
    * [《初學者練習 - LeetCode with Javascript》](https://legacy.gitbook.com/book/skyyen999/-leetcode-with-javascript/details)

### Others

* Type hints (Python 3.5 feature)
  * [Python document - typing](https://docs.python.org/3/library/typing.html)
  * [Stackoverflow - What are Type hints in Python 3.5](https://stackoverflow.com/questions/32557920/what-are-type-hints-in-python-3-5)
  * [Stackoverflow - How to annotate types of multiple return values?](https://stackoverflow.com/questions/40181344/how-to-annotate-types-of-multiple-return-values)
