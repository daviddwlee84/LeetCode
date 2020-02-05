# David's LeetCode Practice [![Build Status](https://travis-ci.org/daviddwlee84/LeetCode.svg?branch=master)](https://travis-ci.org/daviddwlee84/LeetCode) [![codecov](https://codecov.io/gh/daviddwlee84/LeetCode/branch/master/graph/badge.svg)](https://codecov.io/gh/daviddwlee84/LeetCode)

## Testing

* local dependencies
  * `pytest`
  * `pytest-cov`
  * `coverage`

### Correctness (based on [pytest](https://docs.pytest.org/en/latest/contents.html))

Test all the units (in the main directory):

`py.test -v`

### Code Coverage

`pytest --cov-report term --cov Python3/`

> if successful you should see a new `.coverage` file

`coverage report`

* [Coverage.py — Coverage.py 4.3.4 documentation](https://coverage.readthedocs.io/en/coverage-4.3.4/index.html)
* [Code Coverage Done Right | Codecov](https://codecov.io/)
* [codecov/codecov-python: Python report uploader for Codecov](https://github.com/codecov/codecov-python)
* [codecov/example-python: Python coverage example](https://github.com/codecov/example-python)
* [Frequently Asked Questions - Where is the repository upload token found?](https://docs.codecov.io/docs/frequently-asked-questions#section-where-is-the-repository-upload-token-found-)
* [Excluding code from coverage.py — Coverage.py 4.3.4 documentation](https://coverage.readthedocs.io/en/coverage-4.3.4/excluding.html)

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

> Naive means the first thought of mine (usually a little better than Brute-Force, but may need to be optimized.)

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
|  013|Easy    |[Roman to Integer](https://leetcode.com/problems/roman-to-integer/)|2018/9/29|String|[Naive-O(n)](Python3/String/RomanToInteger/Naive013.py)|[Note](Python3/String/RomanToInteger/Note013.md)|-
|  014|Easy    |[Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)|2018/9/16|Array|[Naive-O(n*len)](Python3/Array/LongestCommonPrefix/Naive014.py)|[Note](Python3/Array/LongestCommonPrefix/Note014.md)|-
|  015|Medium ▲|[3Sum](https://leetcode.com/problems/3sum/)|2018/10/13|Array|[TwoPointer-O(n²)](Python3/Array/3Sum/TwoPointer015.py)|[Note](Python3/Array/3Sum/Note015.md)|Try other apporach
|  016|Medium  |[3Sum Closest](https://leetcode.com/problems/3sum-closest/)|2018/10/13|Array|[TwoPointer-O(n²)](Python3/Array/3SumClosest/TwoPointer016.py)|[Note](Python3/Array/3SumClosest/Note016.md)|-
|  017|Medium  |[Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)|2019/3/1|String|[Backtracking-O(n!)](Python3/String/LetterCombinationsOfAPhoneNumber/Backtracking017.py)|[Note](Python3/String/LetterCombinationsOfAPhoneNumber/Note017.md)|-
|👍 018|Medium ▲|[4Sum](https://leetcode.com/problems/4sum/)|2019/3/2|Array, HT|[GeneralizedTwoPointer-O(n³)](Python3/Array/4Sum/GeneralizedTwoPointer018.py)|[Note](Python3/Array/4Sum/Note018.md)|-
|   019|Medium  |[Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)|2019/3/3|Linked List|[HT-O(n)](Python3/LinkedList/RemoveNthNodeFromEndOfList/HT019.py)|[Note](Python3/LinkedList/RemoveNthNodeFromEndOfList/Note019.md)|Two Pointer (reduce space complexity)
|👍 020|Easy    |[Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)|2018/9/15|String, Stack|[Naive-O(n)](Python3/String/ValidParentheses/Naive020.py), [Stack-O(n)](Python3/String/ValidParentheses/Stack020.py), [HashTable-O(n)](Python3/String/ValidParentheses/Dict020.py)|[Note](Python3/String/ValidParentheses/Note020.md)|-
|  021|Easy    |[Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)|2018/6/27|Linked List|[Better-O(n)](Python3/LinkedList/MergeTwoSortedLists/Better021.py)|[Note](Python3/LinkedList/MergeTwoSortedLists/Note021.md)|-
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
|  038|Easy    |[Count and Say](https://leetcode.com/problems/count-and-say/)|2019/9/30|String|[Naive-O(n)](Python3/String/CountAndSay/Naive038.py)|[Note](Python3/String/CountAndSay/Note038.md)|-
|  039|Medium  |[Combination Sum](https://leetcode.com/problems/combination-sum/)|2019/3/7|Array|[Backtracking-O(n!)](Python3/Array/CombinationSum/Backtracking039.py)|[Note](Python3/Array/CombinationSum/Note039.md)|improve time complexity by not use sort
|👍 046|Medium *|[Permutations](https://leetcode.com/problems/permutations/)|2018/5/31|Array|[Backtracking-O(n!)](Python3/Array/Permutations/Backtracking046.py), [Recursive-O(n!)](Python3/Array/Permutations/Recursive046.py), [DFS Based-O(n!)](Python3/Array/Permutations/DFS046.py)|[Note](Python3/Array/Permutations/Note046.md)|-
|👍 048|Medium *|[Rotate Image](https://leetcode.com/problems/rotate-image/)|2019/12/2|Array|[Naive-O(n)](Python3/Array/RotateImage/Naive048.py)|[Note](Python3/Array/RotateImage/Note048.md)|-
|👍 049|Medium *|[Group Anagrams](https://leetcode.com/problems/group-anagrams/)|2019/12/3|String, HT|[Naive-O(nk)](Python3/String/GroupAnagrams/Naive049.py), [Sorting-O(nklogk)](Python3/String/GroupAnagrams/Sorting049.py), [Counter-O(nk)](Python3/String/GroupAnagrams/Counter049.py)|[Note](Python3/String/GroupAnagrams/Note049.md)|testcase
|  053|Easy ▲  |[Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)|2018/6/12|Array, DP, DC|[BruteForce-O(n³)](Python3/Array/MaximumSubarray/Naive053.py), [DP-O(n)](Python3/Array/MaximumSubarray/DP053.py), [DC-O(nlogn)](Python3/Array/MaximumSubarray/DC053.py)|[Note](Python3/Array/MaximumSubarray/Note053.md)|-
|  058|Easy    |[Length of Last Word](https://leetcode.com/problems/length-of-last-word/)|2019/9/30|String|Not even worth to do|-|-
|  066|Easy    |[Plus One](https://leetcode.com/problems/plus-one/)|2019/10/19|Array|[Naive-O(n)](Python3/Array/PlusOne/Naive066.py)|-|-
|  067|Easy    |[Add Binary](https://leetcode.com/problems/add-binary/)|2019/10/22|String|[Adder-O(n)](Python3/String/AddBinary/Naive067.py)|-|-
|  069|Easy    |[Sqrt(x)](https://leetcode.com/problems/sqrtx/)|2019/10/22|Search|[Naive-O(n)](Python3/Search/Sqrt_x/Naive069.py), [BinarySearch-O(logn)](Python3/Search/Sqrt_x/BinarySearch069.py)|-|-
|  070|Easy    |[Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)|2018/6/13|DP|[DP-O(n)](Python3/DynamicProgramming/ClimbingStairs/DP070.py), [Recursive-O(n)](Python3/DynamicProgramming/ClimbingStairs/Recursive070.py)|[Note](Python3/DynamicProgramming/ClimbingStairs/Note070.md)|-
|  071|Medium  |[Simplify Path](https://leetcode.com/problems/simplify-path/)|2019/12/17|String|[Stack-O(n)](Python3/String/SimplifyPath/Stack071.py)|[Note](Python3/String/SimplifyPath/Note071.md)|-
|👍 072|Hard    |[Edit Distance](https://leetcode.com/problems/edit-distance/)|2019/10/30|String|[DP-O(mn)](Python3/String/EditDistance/DP072.py), [Recursive-O(mⁿ)](Python3/String/EditDistance/Recursive072.py)|[Note](Python3/String/EditDistance/Note072.md)|-
|👍 078|Medium  |[Subsets](https://leetcode.com/problems/subsets/)|2018/6/27|BM|[Binary-O(2ⁿ)](Python3/BitManipulation/Subsets/Binary078.py), [DFSBased-O(2ⁿ)](Python3/BitManipulation/Subsets/DFS078.py), [Backtracking-O(2ⁿ)](Python3/BitManipulation/Subsets/Backtracking078.py)|[Note](Python3/BitManipulation/Subsets/Note078.md)|-
|  083|Easy    |[Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)|2019/10/22|Linked List|[Naive-O(n)](Python3/LinkedList/RemoveDuplicatesFromSortedList/Naive083.py)|-|-
|  088|Easy    |[Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)|2019/11/18|Array|[Naive-O(n)](Python3/Array/MergeSortedArray/Naive088.py)||-
|  093|Medium  |[Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/)|2019/12/16|Array|[Backtracking-O(nlogn)](Python3/Array/RestoreIPAddresses/Backtracking093.py)|[Note](Python3/Array/RestoreIPAddresses/Note93.md)|-
|  094|Medium  |[Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)|2018/5/29|Binary Tree|[Recursive-O(n)](Python3/BinaryTree/BinaryTreeInorderTraversal/Recursive94.py), [Iterative-O(n)](Python3/BinaryTree/BinaryTreeInorderTraversal/Iterative94.py)|[Note](Python3/BinaryTree/BinaryTreeInorderTraversal/Note94.md)|-
|  098|Medium ▼|[Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)|2018/6/25|BST|[Inorder-O(n)](Python3/BinaryTree/ValidateBinarySearchTree/InorderTraversal098.py), [DFS-O(n)](Python3/BinaryTree/ValidateBinarySearchTree/DFS098.py)|[Note](Python3/BinaryTree/ValidateBinarySearchTree/Note098.md)|-
|👍 100|Easy    |[Same Tree](https://leetcode.com/problems/same-tree/)|2019/11/20|Binary Tree|[Recursive-O(n)](Python3/BinaryTree/SameTree/Recursive100.py)|[Note](Python3/BinaryTree/SameTree/Note100.md)|-
|👍 101|Easy ▲  |[Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)|2018/6/8|Binary Tree|[Recursive-O(n)](Python3/BinaryTree/SymmetricTree/Recursive101.py), [Iterative-O(n)](Python3/BinaryTree/SymmetricTree/Iterative101.py)|[Note](Python3/BinaryTree/SymmetricTree/Note101.md)|-
|  102|Medium  |[Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)|2018/6/7|Binary Tree|[BFS-O(n)](Python3/BinaryTree/BinaryTreeLevelOrderTraversal/BFS102.py)|[Note](Python3/BinaryTree/BinaryTreeLevelOrderTraversal/Note102.md)|-
|👍  104|Easy   |[Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)|2018/6/8|Binary Tree|[Top-Down-O(n)](Python3/BinaryTree/MaximumDepthofBinaryTree/TopDown104.py), [Bottom-up-O(n)](Python3/BinaryTree/MaximumDepthofBinaryTree/BottomUp104.py), [Top-Down2-O(n)](Python3/BinaryTree/MaximumDepthofBinaryTree/TopDown104_2.py)|[Note](Python3/BinaryTree/MaximumDepthofBinaryTree/Note104.md)|-
|  105|Medium  |[Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)|2018/6/9|Binary Tree|[DC-O(n)](Python3/BinaryTree/ConstructBinaryTreefromPreorderandInorderTraversal/DivideAndConquer105.py)|[Note](Python3/BinaryTree/ConstructBinaryTreefromPreorderandInorderTraversal/Note105.md)|-
|  106|Medium  |[Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)|2018/6/8|Binary Tree|[DC-O(n)](Python3/BinaryTree/ConstructBinaryTreefromInorderandPostorderTraversal/DivideAndConquer106.py)|[Note](Python3/BinaryTree/ConstructBinaryTreefromInorderandPostorderTraversal/Note106.md)|-
|  107|Easy    |[Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)|2019/12/30|Binary Tree|[Naive-O(n)](Python3/BinaryTree/BinaryTreeLevelOrderTraversalII/Naive107.py)|-|-
|  108|Easy    |[Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/)|2019/11/13|BST|[Recursive-O(n)](Python3/BinaryTree/ConvertSortedArrayToBinarySearchTree/Recursive108.py)|[Note](Python3/BinaryTree/ConvertSortedArrayToBinarySearchTree/Note108.md)|Test case
|  109|Medium  |[Convert Sorted List to Binary Search Tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/)|2019/11/13|BST|[TwoPointerRecursive-O(nlogn)](Python3/BinaryTree/ConvertSortedListToBinarySearchTree/TwoPointerRecursive109.py)|[Note](Python3/BinaryTree/ConvertSortedListToBinarySearchTree/Note109.md)|Inorder Simulation, Test case
|👍 110|Easy ▲  |[Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/submissions/)|2019/12/30|Binary Tree|[Naive-O(n)](Python3/BinaryTree/BalancedBinaryTree/Naive110.py)|[Note](Python3/BinaryTree/BalancedBinaryTree/Note110.md)|improve time complexity a bit
|  111|Easy    |[Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)|2019/11/1|Binary Tree|[BFS-O(n)](Python3/BinaryTree/MinimumDepthOfBinaryTree/BFS111.py)||-
|👍 112|Easy    |[Path Sum](https://leetcode.com/problems/path-sum/)|2018/6/8|Binary Tree|[Naive-O(n)](Python3/BinaryTree/PathSum/Naive112.py)|[Note](Python3/BinaryTree/PathSum/Note112.md)|Can be imporved
|👍 113|Medium |[Path Sum II](https://leetcode.com/problems/path-sum-ii/)|2019/12/23|Binary Tree|[Naive-O(n)](Python3/BinaryTree/PathSumII/Naive113.py)|[Note](Python3/BinaryTree/PathSumII/Note113.md)|-
|👍 114|Medium |[Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)|2019/12/31|Binary Tree|[Naive-O(n)](Python3/BinaryTree/FlattenBinaryTreeToLinkedList/Naive114.py)|[Note](Python3/BinaryTree/FlattenBinaryTreeToLinkedList/Note114.md)|more elegant way
|  116|Medium  |[Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)|2019/12/24|Binary Tree|[Naive-O(n)](Python3/BinaryTree/PopulatingNextRightPointersInEachNode/Naive116.py), [DFS-O(n)](Python3/BinaryTree/PopulatingNextRightPointersInEachNode/DFS116.py)|[Note](Python3/BinaryTree/PopulatingNextRightPointersInEachNode/Note116.md)|Test
|  117|Medium *|[Populating Next Right Pointers in Each Node II](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/)|2019/12/24|Binary Tree|[DFS-O(n)](Python3/BinaryTree/PopulatingNextRightPointersInEachNodeII/DFS117.py)|[Note](Python3/BinaryTree/PopulatingNextRightPointersInEachNodeII/Note117.md)|Test
|  118|Easy    |[Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/)|2019/12/28|Array|[Naive-O(n)](Python3/Array/PascalsTriangle/Naive118.py)|[Note](Python3/Array/PascalsTriangle/Note118.md)|Faster approach (memory, recursive, iterative)
|  120|Medium *|[Triangle](https://leetcode.com/problems/triangle/)|2019/12/25|Array|[Naive-O(n)](Python3/Array/Triangle/Naive120.py)|[Note](Python3/Array/Triangle/Note120.md)|less space DP
|  121|Easy    |[Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)|2018/6/13|DP|[DP-O(n)](Python3/DynamicProgramming/BestTimetoBuyandSellStock/DP121.py)|[Note](Python3/DynamicProgramming/BestTimetoBuyandSellStock/Note121.md)|-
|  122|Easy    |[Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)|2018/6/14|Array|[Greedy-O(n)](Python3/Array/BestTimetoBuyandSellStockII/Greedy122.py), [Tricky-O(n)](Python3/Array/BestTimetoBuyandSellStockII/Tricky122.py)|[Note](Python3/Array/BestTimetoBuyandSellStockII/Note122.md)|-
|  125|Easy    |[Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)|2020/1/2|String|[Naive-O(n)](Python3/String/ValidPalindrome/Naive125.py)|-|-
|  127|Medium *|[Word Ladder](https://leetcode.com/problems/word-ladder/)|2019/12/25|String|[BFS-O(n)](Python3/String/WordLadder/BFS127.py)|[Note](Python3/String/WordLadder/Note127.md)|Bidirectional BFS
|👍 128|Hard ▼  |[Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)|2019/11/14|Array|[Naive-O(n²)](Python3/Array/LongestConsecutiveSequence/Naive128.py), [HT-O(n)](Python3/Array/LongestConsecutiveSequence/HT128.py)|[Note](Python3/Array/LongestConsecutiveSequence/Note128.md)|-
|  133|Medium  |[Clone Graph](https://leetcode.com/problems/clone-graph/)|2020/1/16|Graph|[Recursive-O(n)](Python3/Graph/CloneGraph/Recursive133.py)|-|Do it again
|👍 136|Easy    |[Single Number](https://leetcode.com/problems/single-number/)|2019/12/18|Array|[HT-O(n)](Python3/Array/SingleNumber/HT136.py)|[Note](Python3/Array/SingleNumber/Note136.md)|Other solutions
|👍 139|Medium  |[Word Break](https://leetcode.com/problems/word-break/)|2020/1/14|String|[Recursive-O(2ⁿ)](Python3/String/WordBreak/Recursive139.py), [DP-O(n²)](Python3/String/WordBreak/DP139.py)|[Note](Python3/String/WordBreak/Note139.md)|-
|  141|Medium *|[Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)|2019/12/31|Linked List|[Naive-O(n)](Python3/LinkedList/LinkedListCycle/Naive141.py), [TwoPointer-O(n)](Python3/LinkedList/LinkedListCycle/TwoPointer141.py)|[Note](Python3/LinkedList/LinkedListCycle/Note141.md)|testcase
|  144|Medium  |[Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)|2018/5/29|Binary Tree|[Recursive-O(n)](Python3/BinaryTree/BinaryTreePreorderTraversal/Recursive144.py), [Iterative-O(n)](Python3/BinaryTree/BinaryTreePreorderTraversal/Iterative144.py)|[Note](Python3/BinaryTree/BinaryTreePreorderTraversal/Note144.md)|-
|  145|Hard ▼  |[Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)|2018/6/2|Binary Tree|[Recursive-O(n)](Python3/BinaryTree/BinaryTreePostorderTraversal/Recursive145.py), [Iterative-O(n)](Python3/BinaryTree/BinaryTreePostorderTraversal/Iterative145.py)|[Note](Python3/BinaryTree/BinaryTreePostorderTraversal/Note145.md)|-
|  146|Hard ▼  |[LRU Cache](https://leetcode.com/problems/lru-cache/)|2018/6/25|Design|[Naive](Python3/Design/LRUCache/Naive146.py), [OrderedDict](Python3/Design/LRUCache/OrderedDict146.py)|[Note](Python3/Design/LRUCache/Note146.md)|DoubleLinkedList
|  147|Medium  |[Insertion Sort List](https://leetcode.com/problems/insertion-sort-list/)|2020/1/14|Linked List|[Naive-O(n²)](Python3/LinkedList/InsertionSortList/Naive147.py)|[Note](Python3/LinkedList/InsertionSortList/Note147.md)|Do it again with other style
|  151|Medium  |[Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/)|2019/10/22|String|[Pythonic-O(n)](Python3/String/ReverseWordsInAString/Pythonic151.py), [Trick-O(n)](Python3/String/ReverseWordsInAString/Trick151.py)|[Note](Python3/String/ReverseWordsInAString/Note151.md)|-
|  155|Easy    |[Min Stack](https://leetcode.com/problems/min-stack/)|2018/6/28|Design|[Naive](Python3/Design/MinStack/Naive155.py), [Improve](Python3/Design/MinStack/Improve155.py)|[Note](Python3/Design/MinStack/Note155.md)|Naive?!
|  167|Easy    |[Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)|2019/9/18|Array|[TwoPointer-O(n)](Python3/Array/TwoSumII/TwoPointer167.py)|[Note](Python3/Array/TwoSumII/Note167.md)|-
|  189|Easy    |[Rotate Array](https://leetcode.com/problems/rotate-array/)|2018/6/14|Array|[NaiveInPlace-O(k)](Python3/Array/RotateArray/NaiveInPlace189.py), [ExtraArray-O(n)](Python3/Array/RotateArray/UseArray189.py), [Simplest-O(n)](Python3/Array/RotateArray/Simplest189.py)|[Note](Python3/Array/RotateArray/Note189.md)|Cyclic Replacements / Reverse
|  198|Easy    |[House Robber](https://leetcode.com/problems/house-robber/)|2018/6/14|DP|[DP-O(n)](Python3/DynamicProgramming/HouseRobber/DP198.py)|[Note](Python3/DynamicProgramming/HouseRobber/Note198.md)|Can improve space complexity
|👍 200|Medium  |[Number of Islands](https://leetcode.com/problems/number-of-islands/)|2019/7/5|Search|[BFS-O(n²)](Python3/Search/NumberOfIslands/BFS200.py), [DFSO(n²)](Python3/Search/NumberOfIslands/DFS200.py)|[Note](Python3/Search/NumberOfIslands/Note200.md), Learn: Queue & Stack|try Union
|  206|Easy    |[Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)|2018/6/26|Linked List|[Iterative-O(n)](Python3/LinkedList/ReverseLinkedList/Iterative206.py), [Recursive-O(n)](Python3/LinkedList/ReverseLinkedList/Recursive206.py)|[Note](Python3/LinkedList/ReverseLinkedList/Note206.md)|-
|👍 208|Medium *|[Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)|2018/6/24|Design|[Trie](Python3/Design/ImplementTrie/Trie208.py)|[Note](Python3/Design/ImplementTrie/Note208.md)|-
|  215|Medium  |[Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)|2019/9/18|Array|[QuickSort-O(nlogn)](Python3/Array/KthLargestElementInAnArray/QuickSort215.py), [SelectionSortLike-O(n)](Python3/Array/KthLargestElementInAnArray/SelectionSortLike215.py)|[Note](Python3/Array/KthLargestElementInAnArray/Note215.md)|min-heap
|  225|Easy    |[Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)|2018/6/24|Design|[TwoQueue](Python3/Design/ImplementStackusingQueues/TwoQueue225.py)|[Note](Python3/Design/ImplementStackusingQueues/Note225.md)|-
|  232|Easy    |[Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)|2018/6/24|Design|[TwoStack](Python3/Design/ImplementQueueusingStacks/TwoStack232.py)|[Note](Python3/Design/ImplementQueueusingStacks/Note232.md)|-
|  236|Medium  |[Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)|2018/6/10|Binary Tree|[Naive-O(n)](Python3/BinaryTree/LowestCommonAncestorofaBinaryTree/Naive236.py)|[Note](Python3/BinaryTree/LowestCommonAncestorofaBinaryTree/Note236.md)|Maybe has another approach
|👍 257|Easy ▲  |[Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/)|2018/6/11|Binary Tree|[Iterative-O(n)](Python3/BinaryTree/BinaryTreePaths/Iterative257.py), [Recursive-O(n)](Python3/BinaryTree/BinaryTreePaths/Recursive257.py)|[Note](Python3/BinaryTree/BinaryTreePaths/Note257.md)|-
|👍 279|Medium  |[Perfect Squares](https://leetcode.com/problems/perfect-squares/)|2019/8/22|Search|[BFS-O(n)](Python3/Search/PerfectSquares/BFS279.py)|[Note](Python3/Search/PerfectSquares/Note279.md)|DP solution
|  297|Hard    |[Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)|2019/11/14|Binary Tree|[Naive-O(n)](Python3/BinaryTree/SerializeAndDeserializeBinaryTree/Naive297.py)|[Note](Python3/BinaryTree/SerializeAndDeserializeBinaryTree/Note297.md)|-
|👍 300|Medium  |[Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)|2019/11/11|Array|[BruteForce-O(2ⁿ)](Python3/Array/LongestIncreasingSubsequence/BruteForce300.py), [MemoryRecursive-O(n²)](Python3/Array/LongestIncreasingSubsequence/MemoryRecursive300.py), [DP-O(n²)](Python3/Array/LongestIncreasingSubsequence/DP300.py), [BinarySearch-O(nlogn)](Python3/Array/LongestIncreasingSubsequence/BinarySearch300.py)|[Note](Python3/Array/LongestIncreasingSubsequence/Note300.md)|-
|👍 347|Medium  |[Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements)|2019/9/27|Array|[HT-O(n)](Python3/Array/TopKFrequentElements/HTHeap347.py)|[Note](Python3/Array/TopKFrequentElements/Note347.md)|-
|👍 426|Medium  |[Convert Binary Search Tree to Sorted Doubly Linked List](https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list)|TODO|BST|Need subscription||-
|  460|Hard    |[LFU Cache](https://leetcode.com/problems/lfu-cache/)|2018/6/25|Design|[Naive](Python3/Design/LFUCache/Naive460.py)|[Note](Python3/Design/LFUCache/Note460.md)|OrderedDict, LinkedList
|  559|Easy    |[Maximum Depth of N-ary Tree](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/)|2019/11/14|Tree|[Naive-O(n)](Python3/BinaryTree/MaximumDepthOfNaryTree/Naive559.py), [DFS-O(n)](Python3/BinaryTree/MaximumDepthOfNaryTree/DFS559.py)|[Note](Python3/BinaryTree/MaximumDepthOfNaryTree/Note559.md)|Test
|👍 673|Medium  |[Number of Longest Increasing Subsequence](https://leetcode.com/problems/number-of-longest-increasing-subsequence/)|TODO|String|||
|👍 674|Easy    |[Longest Continuous Increasing Subsequence](https://leetcode.com/problems/longest-continuous-increasing-subsequence/)|TODO|String|||
|  687|Medium  |[Longest Univalue Path](https://leetcode.com/problems/longest-univalue-path/)|TODO|Binary Tree||[Note](Python3/BinaryTree/LongestUnivaluePath/Note687.md)|-
|👍 739|Medium  |[Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)|2019/12/26|Array|[Naive-O(n²)](Python3/Array/DailyTemperatures/Naive739.py), [Stack-O(n²)](Python3/Array/DailyTemperatures/Stack739.py)|[Note](Python3/Array/DailyTemperatures/Note739.md)|-
|👍 752|Medium  |[Open the Lock](https://leetcode.com/problems/open-the-lock/)|2019/7/5|Search|[BFS-O(n²)](Python3/Search/OpenTheLock/BFS752.py)|[Note](Python3/Search/OpenTheLock/Note752.md)|Improve time complexity
|  801|Medium  |[Minimum Swaps To Make Sequences Increasing](https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/)|TODO|Array||[Note](Python3/Array/MinimumSwapsToMakeSequencesIncreasing/Note801.md)|-
|👍 978|Medium  |[Longest Turbulent Subarray](https://leetcode.com/problems/longest-turbulent-subarray/)|TODO|String|||
|👍 1143|Medium  |[Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)|2019/10/22|String|[BruteForce-O(2^n)](Python3/String/LongestCommonSubsequence/BruteForce1143.py), [DP-O(mn)](Python3/String/LongestCommonSubsequence/DP1143.py)|[Note](Python3/String/LongestCommonSubsequence/Note1143.md)|DP

## Weekly Contest

### Weekly Contest 163

* [Weekly Contest 163](https://leetcode.com/contest/weekly-contest-163)
* [Ranking](https://leetcode.com/contest/weekly-contest-163/ranking)

|Number | Difficulty | Problem (Contest) | Date | Method                | Remark      | TODO |
|------:|------------|-------------------|------|-----------------------|-------------|------|
|   1260|Easy        |[Shift 2D Grid](https://leetcode.com/problems/shift-2d-grid/) ([contest](https://leetcode.com/contest/weekly-contest-163/problems/shift-2d-grid/)) |2019/11/17|[Naive](Contest/WeeklyContest163/1260-Shift2DGrid.py)|-|-

### Weekly Contest 165

* [Weekly Contest 165](https://leetcode.com/contest/weekly-contest-165)
* [Ranking](https://leetcode.com/contest/weekly-contest-165/ranking/)

|Number | Difficulty | Problem (Contest) | Date | Method                | Remark      | TODO |
|------:|------------|-------------------|------|-----------------------|-------------|------|
|   1275|Easy        |[Find Winner on a Tic Tac Toe Game](https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/) ([contest](https://leetcode.com/contest/weekly-contest-165/problems/find-winner-on-a-tic-tac-toe-game/)) |2019/12/1|[Naive](Contest/WeeklyContest165/1275-FindWinnerOnATicTacToeGame.py)|-|-
|   1276|Medium      |[Number of Burgers with No Waste of Ingredients](https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/) ([contest](https://leetcode.com/contest/weekly-contest-165/problems/number-of-burgers-with-no-waste-of-ingredients/)) |2019/12/1|[Naive](Contest/WeeklyContest165/1275-FindWinnerOnATicTacToeGame.py)|-|-

### Weekly Contest 167

* [Weekly Contest 167](https://leetcode.com/contest/weekly-contest-167/)
* [Ranking](https://leetcode.com/contest/weekly-contest-167/ranking/)

|Number | Difficulty | Problem (Contest) | Date | Method                | Remark      | TODO |
|------:|------------|-------------------|------|-----------------------|-------------|------|
|   1290|Easy        |[Convert Binary Number in a Linked List to Integer](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/) ([contest](https://leetcode.com/contest/weekly-contest-167/problems/convert-binary-number-in-a-linked-list-to-integer/)) |2019/12/15|[Naive](Contest/WeeklyContest167/1290-ConvertBinaryNumberInALinkedListToInteger.py)|-|-
|   1291|Medium      |[Sequential Digits](https://leetcode.com/problems/sequential-digits/) ([contest](https://leetcode.com/contest/weekly-contest-167/problems/sequential-digits/)) |2019/12/15|[Naive](Contest/WeeklyContest167/1291-SequentialDigits.py)|-|-

### Weekly Contest 169

* [Weekly Contest 169](https://leetcode.com/contest/weekly-contest-169/)
* [Ranking](https://leetcode.com/contest/weekly-contest-169/ranking/)

| Difficulty | Problem (Contest) | Date | Method                | Remark      | TODO |
|------------|-------------------|------|-----------------------|-------------|------|
|Easy        |[Find N Unique Integers Sum up to Zero](https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/) ([contest](https://leetcode.com/contest/weekly-contest-169/problems/find-n-unique-integers-sum-up-to-zero/))|2019/12/29|[Naive](Contest/WeeklyContest169/FindNUniqueIntegersSumUpToZero.py)|-|-
|Medium ▼    |[All Elements in Two Binary Search Trees](https://leetcode.com/problems/all-elements-in-two-binary-search-trees/) ([contest](https://leetcode.com/contest/weekly-contest-169/problems/all-elements-in-two-binary-search-trees/))|2019/12/29|[Naive](Contest/WeeklyContest169/AllElementsInTwoBinarySearchTrees.py)|-|-
|Medium      |[Jump Game III](https://leetcode.com/problems/jump-game-iii/) ([contest](https://leetcode.com/contest/weekly-contest-169/problems/jump-game-iii/))|2019/12/29|[Naive](Contest/WeeklyContest169/JumpGameIII.py)|-|-
|Hard        |[Verbal Arithmetic Puzzle](https://leetcode.com/problems/verbal-arithmetic-puzzle/) ([contest](https://leetcode.com/contest/weekly-contest-169/problems/verbal-arithmetic-puzzle/))|TODO|[Naive](Contest/WeeklyContest169/VerbalArithmeticPuzzle.py)|-|Backtracking + Pruning

### Weekly Contest 170

* [Weekly Contest 170](https://leetcode.com/contest/weekly-contest-170/)
* [Ranking](https://leetcode.com/contest/weekly-contest-170/ranking/)

| Difficulty | Problem (Contest) | Date | Method                | Remark      | TODO |
|------------|-------------------|------|-----------------------|-------------|------|
|Easy        |[Find N Unique Integers Sum up to Zero](https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/) ([contest](https://leetcode.com/contest/weekly-contest-170/problems/decrypt-string-from-alphabet-to-integer-mapping/))|2020/1/5|[Naive](Contest/WeeklyContest170/FindNUniqueIntegersSumUpToZero.py)|-|-
|Medium      |[All Elements in Two Binary Search Trees](https://leetcode.com/problems/xor-queries-of-a-subarray/) ([contest](https://leetcode.com/contest/weekly-contest-170/problems/xor-queries-of-a-subarray/))|2020/1/5|[Naive](Contest/WeeklyContest170/AllElementsInTwoBinarySearchTrees_Naive.py), [D&C w/ Memory](Contest/WeeklyContest170/AllElementsInTwoBinarySearchTrees_DCMem.py), [XOR property](Contest/WeeklyContest170/AllElementsInTwoBinarySearchTrees_XOR.py)|-|-
|Medium      |[Get Watched Videos by Your Friends](https://leetcode.com/problems/get-watched-videos-by-your-friends/) ([contest](https://leetcode.com/contest/weekly-contest-170/problems/get-watched-videos-by-your-friends/))|2020/1/5|[BFS](Contest/WeeklyContest170/GetWatchedVideosByYourFriends.py)|-|-
|Hard        |[Minimum Insertion Steps to Make a String Palindrome](https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/) ([contest](https://leetcode.com/contest/weekly-contest-170/problems/minimum-insertion-steps-to-make-a-string-palindrome/))|TODO|-|-|Find mid and compare LCS of head & tail

### Weekly Contest 171

* [Weekly Contest 171](https://leetcode.com/contest/weekly-contest-171/)
* [Ranking](https://leetcode.com/contest/weekly-contest-171/ranking/)

| Difficulty | Problem (Contest) | Date | Method                | Remark      | TODO |
|------------|-------------------|------|-----------------------|-------------|------|
|Easy        |[Convert Integer to the Sum of Two No-Zero Integers](https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/) ([contest](https://leetcode.com/contest/weekly-contest-171/problems/convert-integer-to-the-sum-of-two-no-zero-integers/))|TODO|[Naive](Contest/WeeklyContest171/ConvertIntegerToTheSumOfTwoNoZeroIntegers.py)|-|-
|Medium      |[Minimum Flips to Make a OR b Equal to c](https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/) ([contest](https://leetcode.com/contest/weekly-contest-171/problems/minimum-flips-to-make-a-or-b-equal-to-c/))|2020/1/12|[Naive](Contest/WeeklyContest171/MinimumFlipsToMakeAOrBEqualToC.py)|-|-
|Medium      |[Number of Operations to Make Network Connected](https://leetcode.com/problems/number-of-operations-to-make-network-connected/) ([contest](https://leetcode.com/contest/weekly-contest-171/problems/number-of-operations-to-make-network-connected/))|TODO|-|-|-
|Hard        |[Minimum Distance to Type a Word Using Two Fingers](https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/) ([contest](https://leetcode.com/contest/weekly-contest-171/problems/minimum-distance-to-type-a-word-using-two-fingers/))|TODO|-|-|3D array DP `dp[ith char][left finger][right finger]`

## LeetCode Learn Progress

> [LeetCode Explore Learn](https://leetcode.com/explore/learn/)

Introduction to Algorithm

* [Recursion I](https://leetcode.com/explore/learn/card/recursion-i/)

Introduction to Data Structure

* [Binary Tree](https://leetcode.com/explore/learn/card/data-structure-tree/)
* [Queue & Stack](https://leetcode.com/explore/learn/card/queue-stack/) - [note](Notes/DataStructure/QueueStack.md)
* [Binary Search Tree](https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/)
* [Trie](https://leetcode.com/explore/learn/card/trie)

Design        |  Date    |   Category   |  Implementaiton  |  Remark  | TODO |
--------------|----------|--------------|------------------|----------|------|
Circular Queue|2019/7/4  |Data Structure|[C++](Learn/Cpp/Queue/CircularQueue.cpp)|[Note](Notes/DataStructure/QueueStack.md#Circular-Queue), [Design Circular Queue](https://leetcode.com/problems/design-circular-queue/)|-
Min Stack     |2019/12/26|Data Structure|[C++](Learn/Cpp/Stack/MinStack.cpp)|[Min Stack](https://leetcode.com/problems/min-stack/)|-

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

Data Structure

* [Queue and Stack](Notes/DataStructure/QueueStack.md)
* [Binary Tree](Notes/DataStructure/BinaryTree.md)

Algorithm

* [Dynamic Programming](Notes/Algorithm/DynamicProgramming.md)

## Resources

* [LeetFree](https://www.leetfree.com/)
* [Codeforces](http://codeforces.com/)
* [Newcoder](https://www.nowcoder.com/)
  * [劍指Offer](https://www.nowcoder.com/ta/coding-interviews)

> Paid
>
> * [AlgoExpert](https://www.algoexpert.io)
> * [Grokking **Dynamic Programming Patterns** for Coding Interviews](https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews)
>   1. 0/1 Knapsack
>      * Equal Subset Sum Partition
>      * Subset Sum
>      * Minimum Subset Sum Difference
>      * Count of Subset Sum
>      * Target Sum
>   2. Unbounded Knapsack
>      * Unbounded Knapsack
>      * Rod Cutting
>      * Coin Change
>      * Minimum Coin Change
>      * Maximum Ribbon Cut
>   3. Fibonacci Numbers
>      * Fibonacci numbers
>      * Staircase
>      * Number factors
>      * Minimum jumps to reach the end
>      * Minimum jumps with fee
>      * House thief
>   4. Palindromic Subsequence
>      * Longest Palindromic Subsequence
>      * Longest Palindromic Substring
>      * Count of Palindromic Substrings
>      * Minimum Deletions in a String to make it a Palindrome
>      * Palindromic Partitioning
>   5. Longest Common Substring
>      * Longest Common Substring
>      * Longest Common Subsequence
>      * Minimum Deletions & Insertions to Transform a String into another
>      * Longest Increasing Subsequence
>      * Maximum Sum Increasing Subsequence
>      * Shortest Common Super-sequence
>      * Minimum Deletions to Make a Sequence Sorted
>      * Longest Repeating Subsequence
>      * Subsequence Pattern Matching
>      * Longest Bitonic Subsequence
>      * Longest Alternating Subsequence
>      * Edit Distance
>      * Strings Interleaving

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
  * [azl397985856/leetcode: LeetCode Solutions: A Record of My Problem Solving Journey.](https://github.com/azl397985856/leetcode)
* Go
  * [LeetCode-in-Go](https://github.com/aQuaYi/LeetCode-in-Go)
* Mixed
  * [qiyuangong/leetcode: Python & JAVA Solutions for Leetcode](https://github.com/qiyuangong/leetcode)
  * [haoel/leetcode: LeetCode Problems' Solutions](https://github.com/haoel/leetcode)

### Experience

* [Google | L5 | MTV | Oct 2019 [Offer] - LeetCode Discuss](https://leetcode.com/discuss/interview-experience/424540/google-l5-mtv-oct-2019-offer)

### Others

Usually online judgement TLE limitation is 1 second. => we can estimate the time complexity as the power of ten.

* Type hints (Python 3.5 feature)
  * [Python document - typing](https://docs.python.org/3/library/typing.html)
  * [Stackoverflow - What are Type hints in Python 3.5](https://stackoverflow.com/questions/32557920/what-are-type-hints-in-python-3-5)
  * [Stackoverflow - How to annotate types of multiple return values?](https://stackoverflow.com/questions/40181344/how-to-annotate-types-of-multiple-return-values)
* Python Operations Time Complexity
  * [Complexity of Python Operations](https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt)
  * [TimeComplexity - Python Wiki](https://wiki.python.org/moin/TimeComplexity)
* Python Tricks
  * For memorized recursive
    * [Python Tutorial: Memoization and Decorators](https://www.python-course.eu/python3_memoization.php)
    * [Build a "function with a memory" in Python - Samuel Taylor](https://www.samueltaylor.org/articles/function-with-memory.html)
* Tkinter (`_tkinter.TclError: no display name and no $DISPLAY environment variable`, `_tkinter.TclError: couldn't connect to display ":0"`)
  1. Install tkinter `sudo apt-get install python3-tk`
  2. Install [Xming X Server for Windows](https://sourceforge.net/projects/xming/)
  3. `export DISPLAY=:0;`
