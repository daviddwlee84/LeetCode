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

> Python 3.8

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
  * PQ - Priority Queue (usually Heap)
* Others
  * BM - Bit Manipulation

> Naive means the first thought of mine (usually a little better than Brute-Force, but may need to be optimized.)

### LeetCode Patterns

* [Leetcode Patterns – Medium](https://medium.com/leetcode-patterns)
  * Leetcode Pattern 0 - Iterative traversals on Trees
  * Leetcode Pattern 1 - DFS + BFS
  * Leetcode Pattern 2 - Sliding Windows for Strings
  * Leetcode Pattern 3 - Backtracking
  * Leetcode Pattern 4 - Meta Stuff

### Remark

* Catagory
  * `Catagory1, Catagory2, ...`
  * Usually record in (input data) Data Structure. (The Algorithm (and additional/special Data Structrue) strategy will be noted in the Method field)
  * Code will be put in the main catagory folder (i.e. the first one).
  * Some catagory may be the Related Topic tags marked by LeetCode.
  * (Add Pattern 0~4 in brackets)
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
|  010|Hard *  |[Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)|2018/10/13|String|[DC-O((m+n) x 2ⁿ)](Python3/String/RegularExpressionMatching/DC010.py), [Top-Down DP-O(mn)](Python3/String/RegularExpressionMatching/TopDownDP010.py), [Bottom-Up DP-O(mn)](Python3/String/RegularExpressionMatching/BottomUpDP010.py)|[Note](Python3/String/RegularExpressionMatching/Note010.md)|-
|  011|Medium  |[Container With Most Water](https://leetcode.com/problems/container-with-most-water/)|2018/9/22|Array|[Naive-O(n²)](Python3/Array/ContainerWithMostWater/Naive011.py), [TwoPointer-O(n)](Python3/Array/ContainerWithMostWater/TwoPointer011.py)|[Note](Python3/Array/ContainerWithMostWater/Note011.md)|-
|  012|Medium  |[Integer to Roman](https://leetcode.com/problems/integer-to-roman/)|TODO|String|[Naive-O(n)](Python3/String/IntegerToRoman/Naive012.py)|[Note](Python3/String/IntegerToRoman/Note012.md)|-
|  013|Easy    |[Roman to Integer](https://leetcode.com/problems/roman-to-integer/)|2018/9/29|String|[Naive-O(n)](Python3/String/RomanToInteger/Naive013.py)|[Note](Python3/String/RomanToInteger/Note013.md)|-
|  014|Easy    |[Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)|2018/9/16|Array|[Naive-O(n*len)](Python3/Array/LongestCommonPrefix/Naive014.py)|[Note](Python3/Array/LongestCommonPrefix/Note014.md)|-
|👍 015|Medium ▲|[3Sum](https://leetcode.com/problems/3sum/)|2018/10/13|Array|[TwoPointer-O(n²)](Python3/Array/3Sum/TwoPointer015.py), [Naive-O(n²)](Python3/Array/3Sum/Naive015.py), [TwoPointer2-O(n²)](Python3/Array/3Sum/TwoPointer2_015.py), [BinarySearch-O(n²)](Python3/Array/3Sum/BinarySearch015.py)|[Note](Python3/Array/3Sum/Note015.md)|do it again
|  016|Medium  |[3Sum Closest](https://leetcode.com/problems/3sum-closest/)|2018/10/13|Array|[TwoPointer-O(n²)](Python3/Array/3SumClosest/TwoPointer016.py)|[Note](Python3/Array/3SumClosest/Note016.md)|-
|  017|Medium  |[Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)|2019/3/1|String|[Backtracking-O(n!)](Python3/String/LetterCombinationsOfAPhoneNumber/Backtracking017.py)|[Note](Python3/String/LetterCombinationsOfAPhoneNumber/Note017.md)|-
|👍 018|Medium ▲|[4Sum](https://leetcode.com/problems/4sum/)|2019/3/2|Array, HT|[GeneralizedTwoPointer-O(n³)](Python3/Array/4Sum/GeneralizedTwoPointer018.py)|[Note](Python3/Array/4Sum/Note018.md)|-
|   019|Medium  |[Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)|2019/3/3|Linked List|[HT-O(n)](Python3/LinkedList/RemoveNthNodeFromEndOfList/HT019.py)|[Note](Python3/LinkedList/RemoveNthNodeFromEndOfList/Note019.md)|Two Pointer (reduce space complexity)
|👍 020|Easy    |[Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)|2018/9/15|String, Stack|[Naive-O(n)](Python3/String/ValidParentheses/Naive020.py), [Stack-O(n)](Python3/String/ValidParentheses/Stack020.py), [HashTable-O(n)](Python3/String/ValidParentheses/Dict020.py)|[Note](Python3/String/ValidParentheses/Note020.md), Learn: Queue & Stack|-
|  021|Easy    |[Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)|2018/6/27|Linked List|[Better-O(n)](Python3/LinkedList/MergeTwoSortedLists/Better021.py)|[Note](Python3/LinkedList/MergeTwoSortedLists/Note021.md)|-
|  023|Hard    |[Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)|2018/6/26|Linked List|[Naive-O(kn)](Python3/LinkedList/MergeKSortedLists/Naive023.py), [DC-O(nlogk)](Python3/LinkedList/MergeKSortedLists/DC023.py)|[Note](Python3/LinkedList/MergeKSortedLists/Note023.md)|Compare K each time, Heap, attrgetter
|  022|Medium  |[Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)|2019/3/6|String|[Backtracking-O(n!)](Python3/String/GenerateParentheses/Backtracking022.py)|[Note](Python3/String/GenerateParentheses/Note022.md)|-
|  024|Medium  |[Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)|2018/5/31|Linked List|[Naive-O(n)](Python3/LinkedList/SwapNodesInPairs/Naive024.py), [Recursive-O(n)](Python3/LinkedList/SwapNodesInPairs/Recursive024.py)|[Note](Python3/LinkedList/SwapNodesInPairs/Note024.md)|-
|  026|Easy    |[Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)|2018/6/14|Array|[Naive-O(n)](Python3/Array/RemoveDuplicatesfromSortedArray/Naive026.py), [Better-O(n)](Python3/Array/RemoveDuplicatesfromSortedArray/Better026.py)|[Note](Python3/Array/RemoveDuplicatesfromSortedArray/Note026.md)|-
|  027|Easy    |[Remove Element](https://leetcode.com/problems/remove-element/)|2019/7/2|Array|[Naive-O(n)](Python3/Array/RemoveElement/Naive027.py), [Naive2-O(n)](Python3/Array/RemoveElement/Naive2027.py)|[Note](Python3/Array/RemoveElement/Note027.md)|-
|  028|Easy    |[Implement strStr()](https://leetcode.com/problems/implement-strstr/)|2019/7/2|String|[Naive-O(n)](Python3/String/Implement_strStr/Naive028.py)|[Note](Python3/String/Implement_strStr/Note028.md)|-
|  031|Medium ▲|[Next Permutation](https://leetcode.com/problems/next-permutation/)|2019/3/4|Array|[SinglePass-O(n)](Python3/Array/NextPermutation/SinglePass031.py)|[Note](Python3/Array/NextPermutation/Note031.md)|Permutation with duplicates
|👍 033|Medium *|[Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)|2019/3/5|Array|[BinarySearch-O(log(n))](Python3/Array/SearchInRotatedSortedArray/BinarySearch033.py), [BinarySearch2-O(log(n))](Python3/Array/SearchInRotatedSortedArray/BinarySearch2_033.py)|[Note](Python3/Array/SearchInRotatedSortedArray/Note033.md)|-
|👍 035|Easy    |[Search Insert Position](https://leetcode.com/problems/search-insert-position/)|2019/7/3|Array|[BinarySearch-O(log(n))](Python3/Array/SearchInsertPosition/BinarySearch035.py), [Naive-O(logn)](Python3/Array/SearchInsertPosition/Naive035.py)|[Note](Python3/Array/SearchInsertPosition/Note035.md)|-
|  036|Medium ▼|[Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)|2018/6/21|Array|[HT-O(n)](Python3/Array/ValidSudoku/HashTable036.py)|[Note](Python3/Array/ValidSudoku/Note036.md)|-
|  037|Hard    |[Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)|TODO|Array||[Note](Python3/Array/SudokuSolver/Note037.md)|-
|  038|Easy    |[Count and Say](https://leetcode.com/problems/count-and-say/)|2019/9/30|String|[Naive-O(n)](Python3/String/CountAndSay/Naive038.py)|[Note](Python3/String/CountAndSay/Note038.md)|-
|  039|Medium  |[Combination Sum](https://leetcode.com/problems/combination-sum/)|2019/3/7|Array|[Backtracking-O(n!)](Python3/Array/CombinationSum/Backtracking039.py)|[Note](Python3/Array/CombinationSum/Note039.md)|improve time complexity by not use sort
|👍 046|Medium *|[Permutations](https://leetcode.com/problems/permutations/)|2018/5/31|Array|[Backtracking-O(n!)](Python3/Array/Permutations/Backtracking046.py), [Recursive-O(n!)](Python3/Array/Permutations/Recursive046.py), [DFS Based-O(n!)](Python3/Array/Permutations/DFS046.py)|[Note](Python3/Array/Permutations/Note046.md)|-
|👍 048|Medium *|[Rotate Image](https://leetcode.com/problems/rotate-image/)|2019/12/2|Array|[Naive-O(n)](Python3/Array/RotateImage/Naive048.py)|[Note](Python3/Array/RotateImage/Note048.md)|-
|👍 049|Medium *|[Group Anagrams](https://leetcode.com/problems/group-anagrams/)|2019/12/3|String, HT|[Naive-O(nk)](Python3/String/GroupAnagrams/Naive049.py), [Sorting-O(nklogk)](Python3/String/GroupAnagrams/Sorting049.py), [Counter-O(nk)](Python3/String/GroupAnagrams/Counter049.py)|[Note](Python3/String/GroupAnagrams/Note049.md)|testcase
|👍 050|Medium *|[Pow(x, n)](https://leetcode.com/problems/powx-n/)|2020/7/16|Math|[Naive-O(n)](Python3/Math/PowXN/Naive050.py), [Recursive-O(logn)](Python3/Math/PowXN/Recursive050.py), [Recursive 2-O(logn)](Python3/Math/PowXN/Recursive2_050.py), [Bit Manipulation-O(logn)](Python3/Math/PowXN/BitManipulation050.py)||-
|👍 053|Easy ▲  |[Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)|2018/6/12|Array, DP, DC|[BruteForce-O(n³)](Python3/Array/MaximumSubarray/Naive053.py), [DP-O(n)](Python3/Array/MaximumSubarray/DP053.py), [DC-O(nlogn)](Python3/Array/MaximumSubarray/DC053.py)|[Note](Python3/Array/MaximumSubarray/Note053.md)|Do it again
|👍 055|Medium *|[Jump Game](https://leetcode.com/problems/jump-game/)|2020/4/26|Array|[Backtracking-O(2^n)](Python3/Array/JumpGame/Backtracking055.py), [DPTopDown-O(n^2)](Python3/Array/JumpGame/DPTopDown055.py), [DPBottomUp-O(n^2)](Python3/Array/JumpGame/DPBottomUp055.py), [Greedy-O(n)](Python3/Array/JumpGame/Greedy055.py)|[Note](Python3/Array/JumpGame/Note055.md), Good DP walk through|-
|  056|Medium *|[Merge Intervals](https://leetcode.com/problems/merge-intervals/)|2020/2/21|Array|[Sorting-O(nlogn)](Python3/Array/MergeIntervals/Sorting056.py)|[Note](Python3/Array/MergeIntervals/Note056.md)|Improve performance
|  058|Easy    |[Length of Last Word](https://leetcode.com/problems/length-of-last-word/)|2019/9/30|String|Not even worth to do|-|-
|👍 060|Medium *|[Permutation Sequence](https://leetcode.com/problems/permutation-sequence/)|2020/6/20|String|[Naive-O(n!)](Python3/String/PermutationSequence/Naive060.py), [Backtracking-O(n!)](Python3/String/PermutationSequence/Backtracking060.py), [Math-O(n)](Python3/String/PermutationSequence/Math060.py)||do it again (math one)
|👍 062|Medium  |[Unique Paths](https://leetcode.com/problems/unique-paths/)|2020/6/29|Array|[Naive-O(m+n)](Python3/Array/UniquePaths/Naive062.py), [DP-O(mn)](Python3/Array/UniquePaths/DP062.py)||-
|👍 064|Medium *|[Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)|2020/4/19|Array|[Naive-O(mn)](Python3/Array/MinimumPathSum/Naive064.py), [NoAdditionalSpace-O(mn)](Python3/Array/MinimumPathSum/NoAdditionalSpace064.py)||testcase
|  066|Easy    |[Plus One](https://leetcode.com/problems/plus-one/)|2019/10/19|Array|[Naive-O(n)](Python3/Array/PlusOne/Naive066.py), [FullAdder](Python3/Array/PlusOne/FullAdder066.py)|-|-
|  067|Easy    |[Add Binary](https://leetcode.com/problems/add-binary/)|2019/10/22|String|[Adder-O(n)](Python3/String/AddBinary/Naive067.py)|-|-
|  069|Easy    |[Sqrt(x)](https://leetcode.com/problems/sqrtx/)|2019/10/22|Search|[Naive-O(n)](Python3/Search/Sqrt_x/Naive069.py), [BinarySearch-O(logn)](Python3/Search/Sqrt_x/BinarySearch069.py), [BinarySearch2-O(logn)](Python3/Search/Sqrt_x/BinarySearch2_069.py), [BinarySearch3-O(logn)](Python3/Search/Sqrt_x/BinarySearch3_069.py)|-|-
|  070|Easy    |[Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)|2018/6/13|DP|[DP-O(n)](Python3/DynamicProgramming/ClimbingStairs/DP070.py), [Recursive-O(n)](Python3/DynamicProgramming/ClimbingStairs/Recursive070.py)|[Note](Python3/DynamicProgramming/ClimbingStairs/Note070.md)|TODO: move this to Array
|  071|Medium  |[Simplify Path](https://leetcode.com/problems/simplify-path/)|2019/12/17|String|[Stack-O(n)](Python3/String/SimplifyPath/Stack071.py)|[Note](Python3/String/SimplifyPath/Note071.md)|-
|👍 072|Hard    |[Edit Distance](https://leetcode.com/problems/edit-distance/)|2019/10/30|String|[DP-O(mn)](Python3/String/EditDistance/DP072.py), [Recursive-O(mⁿ)](Python3/String/EditDistance/Recursive072.py)|[Note](Python3/String/EditDistance/Note072.md)|-
|👍 075|Medium  |[Sort Colors](https://leetcode.com/problems/sort-colors/)|2020/6/11|Array|[CountingSort-O(n)](Python3/Array/SortColors/CountingSort075.py), [DutchNationalFlagProblem-O(n)](Python3/Array/SortColors/DutchNationalFlagProblem075.py)|[Note](Python3/Array/SortColors/Note075.md)|testcase, do this again
|👍 078|Medium  |[Subsets](https://leetcode.com/problems/subsets/)|2018/6/27|BM|[Binary-O(2ⁿ)](Python3/BitManipulation/Subsets/Binary078.py), [DFSBased-O(2ⁿ)](Python3/BitManipulation/Subsets/DFS078.py), [Backtracking-O(2ⁿ)](Python3/BitManipulation/Subsets/Backtracking078.py), [Naive-O(2ⁿ)](Python3/BitManipulation/Subsets/Naive078.py)|[Note](Python3/BitManipulation/Subsets/Note078.md)|-
|👍 079|Medium *|[Word Search](https://leetcode.com/problems/word-search/)|2020/6/30|Array|[Naive-O(nlogn)](Python3/Array/WordSearch/Naive079.py), [DFS-O(mn4^s)](Python3/Array/WordSearch/DFS079.py), [DFS 2-O(mn4^s)](Python3/Array/WordSearch/DFS2_079.py)||do it again
|  083|Easy    |[Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)|2019/10/22|Linked List|[Naive-O(n)](Python3/LinkedList/RemoveDuplicatesFromSortedList/Naive083.py)|-|-
|  085|Hard    |[Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/)|TODO|Array||[Note](Python3/Array/MaximalRectangle/Note085.md)|-
|  088|Easy    |[Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)|2019/11/18|Array|[Naive-O(n)](Python3/Array/MergeSortedArray/Naive088.py)||-
|  093|Medium  |[Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/)|2019/12/16|Array|[Backtracking-O(nlogn)](Python3/Array/RestoreIPAddresses/Backtracking093.py)|[Note](Python3/Array/RestoreIPAddresses/Note93.md)|-
|  094|Medium  |[Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)|2018/5/29|Binary Tree|[Recursive-O(n)](Python3/BinaryTree/BinaryTreeInorderTraversal/Recursive94.py), [Iterative-O(n)](Python3/BinaryTree/BinaryTreeInorderTraversal/Iterative94.py)|[Note](Python3/BinaryTree/BinaryTreeInorderTraversal/Note94.md)|-
|👍 096|Medium *|[Unique Binary Search Tree](https://leetcode.com/problems/unique-binary-search-trees/)|2020/6/24|Binary Tree|[Naive-O(n)](Python3/BinaryTree/UniqueBinarySearchTree/Naive096.py)||testcase, do it again
|  098|Medium ▼|[Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)|2018/6/25|BST|[Inorder-O(n)](Python3/BinaryTree/ValidateBinarySearchTree/InorderTraversal098.py), [DFS-O(n)](Python3/BinaryTree/ValidateBinarySearchTree/DFS098.py)|[Note](Python3/BinaryTree/ValidateBinarySearchTree/Note098.md)|-
|👍 100|Easy    |[Same Tree](https://leetcode.com/problems/same-tree/)|2019/11/20|Binary Tree|[Recursive-O(n)](Python3/BinaryTree/SameTree/Recursive100.py), [Naive-O(n)](Python3/BinaryTree/SameTree/Naive100.py)|[Note](Python3/BinaryTree/SameTree/Note100.md)|-
|👍 101|Easy ▲  |[Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)|2018/6/8|Binary Tree|[Recursive-O(n)](Python3/BinaryTree/SymmetricTree/Recursive101.py), [Iterative-O(n)](Python3/BinaryTree/SymmetricTree/Iterative101.py)|[Note](Python3/BinaryTree/SymmetricTree/Note101.md)|-
|  102|Medium  |[Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)|2018/6/7|Binary Tree|[BFS-O(n)](Python3/BinaryTree/BinaryTreeLevelOrderTraversal/BFS102.py)|[Note](Python3/BinaryTree/BinaryTreeLevelOrderTraversal/Note102.md)|-
|👍  104|Easy   |[Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)|2018/6/8|Binary Tree|[Top-Down-O(n)](Python3/BinaryTree/MaximumDepthofBinaryTree/TopDown104.py), [Bottom-up-O(n)](Python3/BinaryTree/MaximumDepthofBinaryTree/BottomUp104.py), [Top-Down2-O(n)](Python3/BinaryTree/MaximumDepthofBinaryTree/TopDown104_2.py)|[Note](Python3/BinaryTree/MaximumDepthofBinaryTree/Note104.md)|-
|  105|Medium  |[Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)|2018/6/9|Binary Tree|[DC-O(n)](Python3/BinaryTree/ConstructBinaryTreefromPreorderandInorderTraversal/DivideAndConquer105.py)|[Note](Python3/BinaryTree/ConstructBinaryTreefromPreorderandInorderTraversal/Note105.md)|-
|  106|Medium  |[Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)|2018/6/8|Binary Tree|[DC-O(n)](Python3/BinaryTree/ConstructBinaryTreefromInorderandPostorderTraversal/DivideAndConquer106.py)|[Note](Python3/BinaryTree/ConstructBinaryTreefromInorderandPostorderTraversal/Note106.md)|-
|  107|Easy    |[Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)|2019/12/30|Binary Tree|[Naive-O(n)](Python3/BinaryTree/BinaryTreeLevelOrderTraversalII/Naive107.py), [Naive 2-O(n)](Python3/BinaryTree/BinaryTreeLevelOrderTraversalII/Naive2_107.py)|-|-
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
|👍 122|Easy    |[Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)|2018/6/14|Array|[Greedy-O(n)](Python3/Array/BestTimetoBuyandSellStockII/Greedy122.py), [Tricky-O(n)](Python3/Array/BestTimetoBuyandSellStockII/Tricky122.py), [Max-O(n)](Python3/Array/BestTimetoBuyandSellStockII/Max122.py)|[Note](Python3/Array/BestTimetoBuyandSellStockII/Note122.md)|-
|👍 124|Hard    |[Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)|2020/4/29|BinaryTree|[Recursive-O(nlogn)](Python3/BinaryTree/BinaryTreeMaximumPathSum/Recursive124.py)|-|testcase, do this again
|  125|Easy    |[Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)|2020/1/2|String|[Naive-O(n)](Python3/String/ValidPalindrome/Naive125.py)|-|-
|  127|Medium *|[Word Ladder](https://leetcode.com/problems/word-ladder/)|2019/12/25|String|[BFS-O(n)](Python3/String/WordLadder/BFS127.py)|[Note](Python3/String/WordLadder/Note127.md)|Bidirectional BFS
|👍 128|Hard ▼  |[Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)|2019/11/14|Array|[Naive-O(n²)](Python3/Array/LongestConsecutiveSequence/Naive128.py), [HT-O(n)](Python3/Array/LongestConsecutiveSequence/HT128.py)|[Note](Python3/Array/LongestConsecutiveSequence/Note128.md)|-
|👍 129|Medium *|[Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/)|2020/6/26|Binary Tree|[Naive-O(nlogn)](Python3/BinaryTree/SumRootToLeafNumbers/Naive129.py), [DFS-O(n)](Python3/BinaryTree/SumRootToLeafNumbers/DFS129.py)||-
|👍 130|Medium  |[Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)|2020/3/25|Array|[Naive-O(mn)](Python3/Array/SurroundedRegions/Naive130.py), [Boarders-O(mn)](Python3/Array/SurroundedRegions/Boarders130.py)|[Note](Python3/Array/SurroundedRegions/Note130.md)|
|  133|Medium  |[Clone Graph](https://leetcode.com/problems/clone-graph/)|2020/1/16|Graph|[Recursive-O(n)](Python3/Graph/CloneGraph/Recursive133.py), [DFS-O(n)](Python3/Graph/CloneGraph/DFS133.py)|[Note](Python3/Graph/CloneGraph/Note133.md), Learn: Queue & Stack|Do it again
|👍 136|Easy    |[Single Number](https://leetcode.com/problems/single-number/)|2019/12/18|Array|[HT-O(n)](Python3/Array/SingleNumber/HT136.py), [Set-O(n)](Python3/Array/SingleNumber/Set136.py), [BM-O(n)](Python3/Array/SingleNumber/BM136.py)|[Note](Python3/Array/SingleNumber/Note136.md)|-
|👍 137|Medium *|[Single Number II](https://leetcode.com/problems/single-number-ii/)|2020/6/22|Array|[Naive-O(n)](Python3/Array/SingleNumberII/Naive137.py), [BitManipulation-O(n)](Python3/Array/SingleNumberII/BitManipulation137.py), [BitManipulation 2-O(n)](Python3/Array/SingleNumberII/BitManipulation2_137.py), [Math-O(n)](Python3/Array/SingleNumberII/Math137.py)||testcase
|👍 138|Medium *|[Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)|2020/3/18|Array|[ProductList-O(n)](Python3/Array/ProductOfArrayExceptSelf/ProductList138.py), [ProductList2-O(n)](Python3/Array/ProductOfArrayExceptSelf/ProductList2_138.py), [SingleProductList-O(n)](Python3/Array/ProductOfArrayExceptSelf/SingleProductList138.py)|[Note](Python3/Array/ProductOfArrayExceptSelf/Note138.md)|testcase
|👍 139|Medium  |[Word Break](https://leetcode.com/problems/word-break/)|2020/1/14|String|[Recursive-O(2ⁿ)](Python3/String/WordBreak/Recursive139.py), [DP-O(n²)](Python3/String/WordBreak/DP139.py)|[Note](Python3/String/WordBreak/Note139.md)|-
|  141|Easy *  |[Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)|2019/12/31|Linked List|[Naive-O(n)](Python3/LinkedList/LinkedListCycle/Naive141.py), [TwoPointer-O(n)](Python3/LinkedList/LinkedListCycle/TwoPointer141.py)|[Note](Python3/LinkedList/LinkedListCycle/Note141.md), Microsoft|testcase
|👍 142|Medium *|[Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)|2020/6/25|Linked List|[TwoPointer-O(n)](Python3/LinkedList/LinkedListCycleII/TwoPointer142.py)||do it again
|  143|Medium  |[Reorder List](https://leetcode.com/problems/reorder-list/)|2020/3/25|Linked List|[Naive-O(n)](Python3/LinkedList/ReorderList/Naive143.py), [Improved-O(n)](Python3/LinkedList/ReorderList/Improved143.py)||testcase
|  144|Medium  |[Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)|2018/5/29|Binary Tree|[Recursive-O(n)](Python3/BinaryTree/BinaryTreePreorderTraversal/Recursive144.py), [Iterative-O(n)](Python3/BinaryTree/BinaryTreePreorderTraversal/Iterative144.py)|[Note](Python3/BinaryTree/BinaryTreePreorderTraversal/Note144.md)|-
|  145|Hard ▼  |[Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)|2018/6/2|Binary Tree|[Recursive-O(n)](Python3/BinaryTree/BinaryTreePostorderTraversal/Recursive145.py), [Iterative-O(n)](Python3/BinaryTree/BinaryTreePostorderTraversal/Iterative145.py)|[Note](Python3/BinaryTree/BinaryTreePostorderTraversal/Note145.md)|-
|👍 146|Hard * ▼|[LRU Cache](https://leetcode.com/problems/lru-cache/)|2018/6/25|Design|[Naive](Python3/Design/LRUCache/Naive146.py), [OrderedDict](Python3/Design/LRUCache/OrderedDict146.py), [DoubleLinkedList](Python3/Design/LRUCache/DoubleLinkedList146.py)|[Note](Python3/Design/LRUCache/Note146.md)|
|  147|Medium  |[Insertion Sort List](https://leetcode.com/problems/insertion-sort-list/)|2020/1/14|Linked List|[Naive-O(n²)](Python3/LinkedList/InsertionSortList/Naive147.py)|[Note](Python3/LinkedList/InsertionSortList/Note147.md)|Do it again with other style
|👍 148|Medium *|[Sort List](https://leetcode.com/problems/sort-list/)|2020/5/11|Linked List|[MergeSort-O(nlogn)](Python3/LinkedList/SortList/MergeSort148.py)||Do it again, testcase
|👍 150|Medium |[Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)|2020/2/10|Array|[Stack-O(n)](Python3/Array/EvaluateReversePolishNotation/Stack150.py)|[Note](Python3/Array/EvaluateReversePolishNotation/Note150.md), Learn: Queue & Stack|-
|  151|Medium *|[Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/)|2019/10/22|String|[Pythonic-O(n)](Python3/String/ReverseWordsInAString/Pythonic151.py), [Trick-O(n)](Python3/String/ReverseWordsInAString/Trick151.py), [Naive-O(n)](Python3/String/ReverseWordsInAString/Naive151.py), [C Style-O(n)](Python3/String/ReverseWordsInAString/CStyle151.py)|[Note](Python3/String/ReverseWordsInAString/Note151.md), Microsoft Intern Interview|-
|  155|Easy    |[Min Stack](https://leetcode.com/problems/min-stack/)|2018/6/28|Design|[Naive](Python3/Design/MinStack/Naive155.py), [Improve](Python3/Design/MinStack/Improve155.py)|[Note](Python3/Design/MinStack/Note155.md), Learn: Queue & Stack|Naive?!
|  167|Easy    |[Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)|2019/9/18|Array|[TwoPointer-O(n)](Python3/Array/TwoSumII/TwoPointer167.py)|[Note](Python3/Array/TwoSumII/Note167.md)|-
|  169|Easy    |[Majority Element](https://leetcode.com/problems/majority-element/)|2020/5/6|Array|[Naive-O(n)](Python3/Array/MajorityElement/Naive169.py), [Counter-O(n)](Python3/Array/MajorityElement/Counter169.py), [Sorting-O(nlogn)](Python3/Array/MajorityElement/Sorting169.py), [Boyer-Moore Voting-O(n)](Python3/Array/MajorityElement/Voting169.py)||-
|👍 174|Hard *  |[Dungeon Game](https://leetcode.com/problems/dungeon-game/)|2020/6/21|Array|[DP-O(mn)](Python3/Array/DungeonGame/DP174.py)||do it again, TODO: bottom-up dp with binary search
|  189|Easy    |[Rotate Array](https://leetcode.com/problems/rotate-array/)|2018/6/14|Array|[NaiveInPlace-O(k)](Python3/Array/RotateArray/NaiveInPlace189.py), [ExtraArray-O(n)](Python3/Array/RotateArray/UseArray189.py), [Simplest-O(n)](Python3/Array/RotateArray/Simplest189.py)|[Note](Python3/Array/RotateArray/Note189.md)|Cyclic Replacements / Reverse
|  190|Easy    |[Reverse Bits](https://leetcode.com/problems/rotate-array/)|2020/7/12|Bit Manipulation|[Naive-O(n)](Python3/BitManipulation/ReverseBits/Naive190.py), [String-O(n)](Python3/BitManipulation/ReverseBits/String190.py)||testcase
|  198|Easy    |[House Robber](https://leetcode.com/problems/house-robber/)|2018/6/14|DP|[DP-O(n)](Python3/DynamicProgramming/HouseRobber/DP198.py)|[Note](Python3/DynamicProgramming/HouseRobber/Note198.md)|Can improve space complexity
|👍 200|Medium |[Number of Islands](https://leetcode.com/problems/number-of-islands/)|2019/7/5|Search|[BFS-O(n²)](Python3/Search/NumberOfIslands/BFS200.py), [DFS-O(n²)](Python3/Search/NumberOfIslands/DFS200.py)|[Note](Python3/Search/NumberOfIslands/Note200.md), Learn: Queue & Stack|try Union, do this again
|👍 201|Medium |[Bitwise AND of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/)|2020/4/23|BitManipulation|[Naive-O(n)](Python3/BitManipulation/BitwiseANDOfNumbersRange/Naive201.py), [Improve-O(n)](Python3/BitManipulation/BitwiseANDOfNumbersRange/Improve201.py)||
|  202|Easy    |[Happy Number](https://leetcode.com/problems/happy-number/)|2020/4/2|Math|[Naive-O(n)](Python3/Math/HappyNumber/Naive202.py)||testcase
|  203|Easy    |[Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/)|2020/3/18|Linked List|[Naive-O(n)](Python3/LinkedList/RemoveLinkedListElements/Naive203.py)||testcase, single pointer
|  206|Easy    |[Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)|2018/6/26|Linked List|[Iterative-O(n)](Python3/LinkedList/ReverseLinkedList/Iterative206.py), [Recursive-O(n)](Python3/LinkedList/ReverseLinkedList/Recursive206.py)|[Note](Python3/LinkedList/ReverseLinkedList/Note206.md)|-
|👍 207|Medium *|[Course Schedule](https://leetcode.com/problems/course-schedule/)|TODO|Array|-|-|topological sort
|👍 208|Medium *|[Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)|2018/6/24|Design|[Naive](Python3/Design/ImplementTrie/Naive208.py), [Trie (using Hashmap)](Python3/Design/ImplementTrie/Trie208.py), [Trie (using Array)](Python3/Design/ImplementTrie/Trie_array208.py)|[Note](Python3/Design/ImplementTrie/Note208.md)|testcase
|👍 210|Medium *|[Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)|TODO|Array|-|-|topological sort
|👍 211|Medium *|[Add and Search Word - Data structure design](https://leetcode.com/problems/add-and-search-word-data-structure-design/)|2020/6/30|Design|[Naive-O(n)](Python3/Design/AddAndSearchWord/Naive211.py), [RegEx-O(n)](Python3/Design/AddAndSearchWord/RegEx211.py), [Tire-O(n)](Python3/Design/AddAndSearchWord/Tire211.py)|[Note](Python3/Design/AddAndSearchWord/Note211.md), [Tire 2-O(n)](Python3/Design/AddAndSearchWord/Tire2_211.py)|do it again
|👍 212|Hard *  |[Word Search II](https://leetcode.com/problems/word-search-ii/)|2020/6/30|Array|[Tire-O(n)](Python3/Array/WordSearchII/Naive212.py)|-|do it again, testcase
|  215|Medium  |[Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)|2019/9/18|Array|[QuickSort-O(nlogn)](Python3/Array/KthLargestElementInAnArray/QuickSort215.py), [SelectionSortLike-O(n)](Python3/Array/KthLargestElementInAnArray/SelectionSortLike215.py)|[Note](Python3/Array/KthLargestElementInAnArray/Note215.md)|min-heap
|👍 221|Medium *|[Maximal Square](https://leetcode.com/problems/maximal-square/)|2020/4/27|Array|[Naive-O(k x (mn)^2)](Python3/Array/MaximalSquare/Naive221.py), [BruteForce-O((mn)^2)](Python3/Array/MaximalSquare/BruteForce221.py), [DP-O(mn)](Python3/Array/MaximalSquare/DP221.py), [Better DP-O(mn)](Python3/Array/MaximalSquare/DP_2_221.py)|[Note](Python3/Array/MaximalSquare/Note221.md)|-
|👍 221|Medium *|[Count Complete Tree Nodes](https://leetcode.com/problems/count-complete-tree-nodes/)|2020/6/23|Binary Tree|[Naive-O(n)](Python3/BinaryTree/CountCompleteTreeNodes/Naive221.py), [BinarySearch-O(n)](Python3/BinaryTree/CountCompleteTreeNodes/BinarySearch221.py)||testcase
|  225|Easy    |[Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)|2018/6/24|Design|[Two Queue](Python3/Design/ImplementStackusingQueues/TwoQueue225.py)|[Note](Python3/Design/ImplementStackusingQueues/Note225.md), Learn: Queue & Stack|-
|👍 226|Easy *  |[Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)|2020/6/1|Binary Tree|[Naive](Python3/BinaryTree/InvertBinaryTree/Naive226.py)|[Note](Python3/BinaryTree/InvertBinaryTree/Note226.md)|-
|👍 230|Medium *|[Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)|2020/5/20|Binary Tree|[Naive-O(n)](Python3/BinaryTree/KthSmallestElementInABST/Naive230.py), [Iterative-O(n)](Python3/BinaryTree/KthSmallestElementInABST/Iterative230.py)|[Note](Python3/BinaryTree/KthSmallestElementInABST/Note230.md)|testcase
|  231|Easy *  |[Power of Two](https://leetcode.com/problems/power-of-two/)|2020/6/8|Math|[Naive-O(n)](Python3/Math/PowerOfTwo/Naive231.py), [String-O(n)](Python3/Math/PowerOfTwo/String231.py), [BitManipulation-O(n)](Python3/Math/PowerOfTwo/BitManipulation231.py)||do it again
|  232|Easy    |[Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)|2018/6/24|Design|[Two Stack](Python3/Design/ImplementQueueusingStacks/TwoStack232.py)|[Note](Python3/Design/ImplementQueueusingStacks/Note232.md), Learn: Queue & Stack|-
|  236|Medium  |[Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)|2018/6/10|Binary Tree|[Naive-O(n)](Python3/BinaryTree/LowestCommonAncestorofaBinaryTree/Naive236.py)|[Note](Python3/BinaryTree/LowestCommonAncestorofaBinaryTree/Note236.md)|Maybe has another approach
|  237|Easy    |[Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/)|2020/3/18|Linked List|[Naive-O(1)](Python3/LinkedList/DeleteNodeInALinkedList/Naive237.py)|(not worth to do)|testcase..
|  252|Easy *|[Meeting Rooms](https://leetfree.com/problems/meeting-rooms.html) (premium)|2020/2/20|Array|[Sorting-O(nlogn)](Python3/Array/MeetingRooms/Sorting252.py)|[Note](Python3/Array/MeetingRooms/Note252.md), Facebook|-
|👍 253|Medium *|[Meeting Rooms II](https://leetfree.com/problems/meeting-rooms-ii.html) (premium)|2020/3/14|Array|[Sorting-O(nlogn)](Python3/Array/MeetingRoomsII/Sorting253.py)|[Note](Python3/Array/MeetingRoomsII/Note253.md), Facebook|-
|👍 257|Easy ▲  |[Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/)|2018/6/11|Binary Tree|[Iterative-O(n)](Python3/BinaryTree/BinaryTreePaths/Iterative257.py), [Recursive-O(n)](Python3/BinaryTree/BinaryTreePaths/Recursive257.py)|[Note](Python3/BinaryTree/BinaryTreePaths/Note257.md), Learn: Queue & Stack|-
|   258|Easy    |[Add Digits](https://leetcode.com/problems/add-digits/)|2020/3/18|Array|[Naive-O(n)](Python3/Array/AddDigits/Naive258.py), [NoLoop-O(1)](Python3/Array/AddDigits/NoLoop258.py)|[Note](Python3/Array/AddDigits/Note258.md), Microsoft, not good|testcase
|👍 260|Medium *|[Single Number III](https://leetcode.com/problems/single-number-iii/)|2020/6/22|Array|[Naive-O(n)](Python3/Array/SingleNumberIII/Naive260.py), [BitManipulation-O(n)](Python3/Array/SingleNumberIII/BitManipulation260.py)||testcase
|   263|Easy    |[Ugly Number](https://leetcode.com/problems/ugly-number/)|2020/7/4|Array|[Naive-O(n)](Python3/Math/UglyNumber/Naive263.py)||
|👍 264|Medium *|[Ugly Number II](https://leetcode.com/problems/ugly-number-ii/)|2020/7/4|Array|[PriorityQueue-O(n)](Python3/Math/UglyNumberII/PriorityQueue264.py), [DP-O(n)](Python3/Math/UglyNumberII/DP264.py)|[Note](Python3/Math/UglyNumberII/Note264.md), Microsoft Intern Interview|do it again
|   278|Easy    |[First Bad Version](https://leetcode.com/problems/first-bad-version/)|2020/5/1|Iteractive|[Naive-O(logn)](Python3/Array/FirstBadVersion/Naive278.py)||testcase
|   274|Medium  |[H-Index](https://leetcode.com/problems/h-index/)|2020/6/18|Array|[CumulativeSum-O(n)](Python3/Array/H-Index/CumulativeSum274.py)|sorting-based solution see 275|testcase, do it again
|   275|Medium  |[H-Index II](https://leetcode.com/problems/h-index-ii/)|2020/6/18|Array|[Linear-O(n)](Python3/Array/H-IndexII/Linear275.py), [BinarySearch-O(n)](Python3/Array/H-IndexII/BinarySearch275.py)||testcase, do it again
|👍 287|Medium  |[Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)|2020/6/25|Array|[Naive-O(n^2)](Python3/Array/FindTheDuplicateNumber/Naive287.py), [TwoPointer-O(n)](Python3/Array/FindTheDuplicateNumber/TwoPointer287.py)||do it again, testcase
|👍 279|Medium *|[Perfect Squares](https://leetcode.com/problems/perfect-squares/)|2019/8/22|Search|[BFS-O(n)](Python3/Search/PerfectSquares/BFS279.py), [Recursive-O(n!)](Python3/Search/PerfectSquares/Recursive279.py), [Top-Down DP-O(n)](Python3/Search/PerfectSquares/TopDownDP279.py), [Linear Check-O(n * sqrt(n))](Python3/Search/PerfectSquares/LinearCheck279.py), [Bottom-Up DP-O(n)](Python3/Search/PerfectSquares/BottomUpDP279.py), [Math-O(sqrt(n))](Python3/Search/PerfectSquares/Math279.py)|[Note](Python3/Search/PerfectSquares/Note279.md)|do it again
|   283|Easy    |[Move Zeroes](https://leetcode.com/problems/move-zeroes/)|2020/4/4|Array|[Naive-O(n)](Python3/Array/MoveZeroes/Naive283.py), [TwoPointer-O(n)](Python3/Array/MoveZeroes/TwoPointer283.py)|-|testcase
|  297|Hard    |[Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)|2019/11/14|Binary Tree|[Naive-O(n)](Python3/BinaryTree/SerializeAndDeserializeBinaryTree/Naive297.py)|[Note](Python3/BinaryTree/SerializeAndDeserializeBinaryTree/Note297.md)|-
|👍 300|Medium  |[Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)|2019/11/11|Array|[BruteForce-O(2ⁿ)](Python3/Array/LongestIncreasingSubsequence/BruteForce300.py), [MemoryRecursive-O(n²)](Python3/Array/LongestIncreasingSubsequence/MemoryRecursive300.py), [DP-O(n²)](Python3/Array/LongestIncreasingSubsequence/DP300.py), [BinarySearch-O(nlogn)](Python3/Array/LongestIncreasingSubsequence/BinarySearch300.py)|[Note](Python3/Array/LongestIncreasingSubsequence/Note300.md)|-
|👍 328|Medium  |[Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/)|2020/5/16|Linked List|[Naive-O(n)](Python3/LinkedList/OddEvenLinkedList/Naive328.py)||testcase
|👍 332|Medium *|[Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/)|2020/6/28|Array|[Naive-O(n)](Python3/Array/ReconstructItinerary/Naive332.py), [EulerianPath-O(ElogE)](Python3/Array/ReconstructItinerary/EulerianPath332.py), [DFS-O(nlogn)](Python3/Array/ReconstructItinerary/DFS332.py)||do it again
|   344|Easy    |[Reverse String](https://leetcode.com/problems/reverse-string/)|2020/6/4|String|[Naive-O(n)](Python3/String/ReverseString/Naive344.py), [Recursive-O(n)](Python3/String/ReverseString/Recursive344.py)|[Note](Python3/String/ReverseString/Note344.md)|testcase
|👍 347|Medium *|[Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements)|2019/9/27|Array|[Naive-O(nlogn)](Python3/Array/TopKFrequentElements/Naive347.py), [HT Heap-O(nlogk)](Python3/Array/TopKFrequentElements/HTHeap347.py), [HT Heap 2-O(nlogk)](Python3/Array/TopKFrequentElements/HTHeap2_347.py), [Quickselect-avg O(n)](Python3/Array/TopKFrequentElements/Quickselect347.py), [Bucket Sort-O(n)](Python3/Array/TopKFrequentElements/BucketSort347.py), [HT-O(n)](Python3/Array/TopKFrequentElements/HT347.py)|[Note](Python3/Array/TopKFrequentElements/Note347.md)|-
|   367|Easy    |[Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/)|2020/5/9|Math|[Naive-O(n)](Python3/Math/ValidPerfectSquare/Naive367.py), [BinarySearch-O(n)](Python3/Math/ValidPerfectSquare/BinarySearch367.py)|-|testcase
|👍 368|Medium  |[Largest Divisible Subset](https://leetcode.com/problems/largest-divisible-subset/)|2020/6/13|Array|[Naive-O(n!)](Python3/Array/LargestDivisibleSubset/Naive368.py), [DP-O(n²)](Python3/Array/LargestDivisibleSubset/DP368.py)|[Note](Python3/Array/LargestDivisibleSubset/Note368.md)|do it again (DP)
|👍 373|Medium  |[Find K Pairs with Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/)|2020/5/3|Array|[Priority Queue-O(klogk)](Python3/Array/FindKPairsWithSmallestSums/PriorityQueue373.py), [Heap Merge Sort](Python3/Array/FindKPairsWithSmallestSums/HeapMergeSort373.py)|related to 1439 (competition)|testcase, do it again
|👍 378|Medium  |[Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)|TODO|Array|||-
|   380|Medium  |[Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/)|2020/6/12|Design|[Naive-O(1)](Python3/Design/InsertDeleteGetRandomO(1).py)||testcase, use HT + array
|   383|Easy    |[Ransom Note](https://leetcode.com/problems/ransom-note/)|2020/5/4|String|[Naive-O(n)](Python3/String/RansomNote/Naive383.py)|-|testcase
|   387|Easy    |[First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/)|2020/5/5|String|[Naive-O(n)](Python3/String/FirstUniqueCharacterInAString/Naive387.py)|-|testcase
|👍 402|Medium  |[Remove K Digits](https://leetcode.com/problems/remove-k-digits/)|2020/5/13|String|[Naive-O(n)](Python3/String/RemoveKDigits/Greedy402.py)||do this again
|👍 406|Medium *|[Queue Reconstruction by Height](https://leetcode.com/problems/queue-reconstruction-by-height/)|2020/6/6|Array|[Sorting-O(n^2)](Python3/Array/QueueReconstructionByHeight/Sorting402.py), [InsertFromLowest-O(nlogn)](Python3/Array/QueueReconstructionByHeight/InsertFromLowest402.py), [InsertFromHighest-O(nlogn)](Python3/Array/QueueReconstructionByHeight/InsertFromHighest402.py), [Insert-O(n)](Python3/Array/QueueReconstructionByHeight/Insert402.py)|[Note](Python3/Array/QueueReconstructionByHeight/Note402.md)|do it again, testcase
|   419|Medium  |[Battleships in a Board](https://leetcode.com/problems/battleships-in-a-board/)|TODO|Array|||
|👍 426|Medium  |[Convert Binary Search Tree to Sorted Doubly Linked List](https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list)|TODO|BST|Need subscription||-
|👍 430|Medium *|[Flatten a Multilevel Doubly Linked List](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/)|2020/7/10|Linked List|[Naive-O(n)](Python3/LinkedList/FlattenAMultilevelDoublyLinkedList/Naive430.py), [Stack-O(n)](Python3/LinkedList/FlattenAMultilevelDoublyLinkedList/Stack430.py)||do it again, testcase
|👍 438|Medium  |[Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)|2020/5/17|String|[Naive-O(n)](Python3/String/FindAllAnagramsInAString/Naive438.py)||-
|👍 441|Easy    |[Arranging Coins](https://leetcode.com/problems/arranging-coins/)|2020/7/1|Math|[Naive-O(n)](Python3/Math/ArrangingCoins/Naive441.py), [Binary Search-O(logn)](Python3/Math/ArrangingCoins/BinarySearch441.py), [Math-O(1)](Python3/Math/ArrangingCoins/Math441.py)||-
|👍 451|Medium  |[Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/)|2020/5/22|String|[Naive-O(n)](Python3/String/SortCharactersByFrequency/Naive451.py), [PQ-O(n)](Python3/String/SortCharactersByFrequency/PQ451.py)||testcase
|  460|Hard    |[LFU Cache](https://leetcode.com/problems/lfu-cache/)|2018/6/25|Design|[Naive](Python3/Design/LFUCache/Naive460.py)|[Note](Python3/Design/LFUCache/Note460.md)|OrderedDict, LinkedList
|  461|Easy    |[Hamming Distance](https://leetcode.com/problems/hamming-distance/)|2020/7/5|Bit Manipulation|[Naive-O(n)](Python3/BitManipulation/HammingDistance/Naive461.py)||testcase
|👍 463|Easy    |[Island Perimeter](https://leetcode.com/problems/island-perimeter/)|2020/7/7|Array|[Naive-O(n)](Python3/Array/IslandPerimeter/Naive463.py), [Neighbour-O(n)](Python3/Array/IslandPerimeter/Neighbour463.py), [CountEdge-O(n)](Python3/Array/IslandPerimeter/CountEdge463.py), [StringEdge-O(n)](Python3/Array/IslandPerimeter/StringEdge463.py)||testcase
|👍 468|Medium  |[Validate IP Address](https://leetcode.com/problems/validate-ip-address/)|2020/6/16|String|[Naive-O(n)](Python3/String/ValidateIPAddress/Naive468.py)|Microsoft Intern Interview|todo: pure regex, pure rule
|👍 477|Medium  |[Total Hamming Distance](https://leetcode.com/problems/total-hamming-distance/)|TODO|Bit Manipulation|||[string approach](https://leetcode.com/problems/total-hamming-distance/discuss/96229/python-via-strings)
|👍 494|Medium |[Target Sum](https://leetcode.com/problems/target-sum/)|2020/2/10|Array|[Naive-O(n²)](Python3/Array/TargetSum/Naive494.py), [RecursiveWithMemory-O(l*n)](Python3/Array/TargetSum/RecursiveWithMemory494.py), [2D DP-O(l*n)](Python3/Array/TargetSum/DP_2D_494.py), [1D DP-O(l*n)](Python3/Array/TargetSum/DP_1D_494.py)|[Note](Python3/Array/TargetSum/Note494.md), Learn: Queue & Stack|more optimization on DP
|👍 518|Medium *|[Coin Change 2](https://leetcode.com/problems/coin-change-2/)|2020/6/7|Array|[Naive-O(n^t)](Python3/Array/CoinChange2/Naive518.py), [DP-O(nt)](Python3/Array/CoinChange2/DP518.py)|[Note](Python3/Array/CoinChange2/Note518.md)|do it again (bottom up 1D DP)
|👍 525|Medium *|[Contiguous Array](https://leetcode.com/problems/contiguous-array/)|2020/4/13|Array|[Naive-O(n²)](Python3/Array/ContiguousArray/Naive525.py), [HT-O(n)](Python3/Array/ContiguousArray/HT525.py), [ExtraArray-O(n)](Python3/Array/ContiguousArray/ExtraArray525.py), [HT2-O(n)](Python3/Array/ContiguousArray/HT2_525.py)||do it again
|  528|Medium  |[Random Pick with Weight](https://leetcode.com/problems/random-pick-with-weight/)|2020/6/5|Design|[Naive-O(n)](Python3/Design/RandomPickWithWeight/Naive528.py)||testcase
|👍 540|Medium  |[Single Element in a Sorted Array](https://leetcode.com/problems/single-element-in-a-sorted-array/)|2020/5/12|Array|[Naive-O(n)](Python3/Array/SingleElementInASortedArray/Naive540.py), [BinarySearchXOR-O(logn)](Python3/Array/SingleElementInASortedArray/BinarySearchXOR540.py)||testcase
|👍 543|Easy    |[Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)|2020/4/11|Binary Tree|[DFS-O(n)](Python3/BinaryTree/DiameterOfBinaryTree/DFS543.py)||testcase
|  559|Easy    |[Maximum Depth of N-ary Tree](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/)|2019/11/14|Tree|[Naive-O(n)](Python3/BinaryTree/MaximumDepthOfNaryTree/Naive559.py), [DFS-O(n)](Python3/BinaryTree/MaximumDepthOfNaryTree/DFS559.py)|[Note](Python3/BinaryTree/MaximumDepthOfNaryTree/Note559.md)|Test
|👍 560|Medium  |[Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)|2020/4/22|Array|[BruteForce-O(n^3)](Python3/Array/SubarraySumEqualsK/BruteForce560.py), [CumulativeSum-O(n²)](Python3/Array/SubarraySumEqualsK/CumulativeSum560.py), [WithoutSpace-O(n²)](Python3/Array/SubarraySumEqualsK/WithoutSpace560.py), [HT-O(n)](Python3/Array/SubarraySumEqualsK/HT560.py)|[Note](Python3//Array/SubarraySumEqualsK/Note560.md)|
|👍 567|Medium  |[Permutation in String](https://leetcode.com/problems/permutation-in-string/)|2020/5/18|String|[Naive-O(n)](Python3/String/PermutationInString/Naive567.py)||testcase
|👍 630|Hard *  |[Course Schedule III](https://leetcode.com/problems/course-schedule-iii/)|TODO|Array|-|-|topological sort
|👍 662|Medium *|[Maximum Width of Binary Tree](https://leetcode.com/problems/maximum-width-of-binary-tree/)|2020/7/9|Binary Tree|[Naive-O(n)](Python3/BinaryTree/MaximumWidthOfBinaryTree/Naive662.py)|[Note](Python3/BinaryTree/MaximumWidthOfBinaryTree/Note662.md)|do it again (more elegant way), testcase
|👍 673|Medium  |[Number of Longest Increasing Subsequence](https://leetcode.com/problems/number-of-longest-increasing-subsequence/)|TODO|String|||
|👍 674|Easy    |[Longest Continuous Increasing Subsequence](https://leetcode.com/problems/longest-continuous-increasing-subsequence/)|TODO|String|||
|👍 678|Medium *|[Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/)|2020/4/17|String|[Naive-O(n*3^n)](Python3/String/ValidParenthesisString/Naive678.py), [DP-O(n)](Python3/String/ValidParenthesisString/DP678.py), [Greedy-O(n)](Python3/String/ValidParenthesisString/Greedy678.py)|[Note](Python3/String/ValidParenthesisString/Note678.md)|do this again
|  687|Medium  |[Longest Univalue Path](https://leetcode.com/problems/longest-univalue-path/)|TODO|Binary Tree||[Note](Python3/BinaryTree/LongestUnivaluePath/Note687.md)|-
|  700|Easy    |[Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/)|2020/6/15|Binary Tree|[Naive-O(logn)](Python3/BinaryTree/SearchInABinarySearchTree/Naive700.py)||testcase
|  703|Easy    |[Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)|2020/5/8|Design|[Naive-O(n)](Python3/Design/KthLargestElementInAStream/Naive703.py), [Heap-O(n)](Python3/Design/KthLargestElementInAStream/Heap703.py)|[Note](Python3/Design/KthLargestElementInAStream/Note703.md)|testcase
|  704|Easy    |[Binary Search](https://leetcode.com/problems/binary-search)|2020/5/9|Array|[Iterative(<)-O(logn)](Python3/Array/BinarySearch/Iterative704.py), [Recursive(<=)-O(logn)](Python3/Array/BinarySearch/Recursive704.py)||Test
|  733|Easy    |[Flood Fill](https://leetcode.com/problems/flood-fill/)|2020/5/11|Array|[Naive-O(n)](Python3/Array/FloodFill/Naive733.py), [DFS-O(n)](Python3/Array/FloodFill/DFS733.py), [IterativeDFS-O(n)](Python3/Array/FloodFill/IterativeDFS733.py)||Test
|👍 739|Medium  |[Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)|2019/12/26|Array|[Naive-O(n²)](Python3/Array/DailyTemperatures/Naive739.py), [Naive2-O(n²)](Python3/Array/DailyTemperatures/Naive2_739.py), [Stack-O(n²)](Python3/Array/DailyTemperatures/Stack739.py)|[Note](Python3/Array/DailyTemperatures/Note739.md), Learn: Queue & Stack|-
|👍 752|Medium  |[Open the Lock](https://leetcode.com/problems/open-the-lock/)|2019/7/5|Search|[BFS-O(n²)](Python3/Search/OpenTheLock/BFS752.py)|[Note](Python3/Search/OpenTheLock/Note752.md), Learn: Queue & Stack|Improve time complexity
|  771|Easy    |[Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/)|2020/5/2|String|[Naive-O(n)](Python3/String/JewelsAndStones/Naive771.py), [Naive2-O(n)](Python3/String/JewelsAndStones/Naive2_771.py)||testcase
|👍 787|Medium *|[Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)|2020/6/14|Graph|[Naive-O(V + E)](Python3/Graph/CheapestFlightsWithinKStops/Naive787.py), [BFS-O(V + E)](Python3/Graph/CheapestFlightsWithinKStops/BFS787.py), [DP-O(n²)](Python3/Graph/CheapestFlightsWithinKStops/DP787.py)|[Note](Python3/Graph/CheapestFlightsWithinKStops/Note787.md)|testcase, do it again
|  801|Medium  |[Minimum Swaps To Make Sequences Increasing](https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/)|TODO|Array||[Note](Python3/Array/MinimumSwapsToMakeSequencesIncreasing/Note801.md)|-
|  844|Easy    |[Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/)|2020/4/9|String|[Naive-O(n)](Python3/String/BackspaceStringCompare/Naive844.py), [TwoPointer-O(n)](Python3/String/BackspaceStringCompare/TwoPointer844.py)||testcase
|👍 857|Hard *  |[Minimum Cost to Hire K Workers](https://leetcode.com/problems/minimum-cost-to-hire-k-workers/)|2020/3/17|Array|[Greedy-O(n²logn)](Python3/Array/MinimumCostToHireKWorkers/Greedy857.py), [Greedy w/ PQ-O(nlogn)](Python3/Array/MinimumCostToHireKWorkers/GreedyPQ857.py)|[Note](Python3/Array/MinimumCostToHireKWorkers/Note857.md)|-
|👍 862|Hard *  |[Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/)|TODO|Array||[Note](Python3/Array/ShortestSubarrayWithSumAtLeastK/Note862.md)|Deque
|  876|Easy    |[Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)|2020/4/8|Linked List|[Naive-O(n)](Python3/LinkedList/MiddleOfTheLinkedList/Naive876.py), [TwoPointer-O(n)](Python3/LinkedList/MiddleOfTheLinkedList/TwoPointer876.py)||testcase
|👍 886|Medium *|[Possible Bipartition](https://leetcode.com/problems/possible-bipartition/)|2020/5/27|Array|||testcase
|👍 901|Medium  |[Online Stock Span](https://leetcode.com/problems/online-stock-span/)|2020/5/19|Design|[Naive-O(n)](Python3/Design/OnlineStockSpan/Naive901.py), [Count-O(n)](Python3/Design/OnlineStockSpan/Count901.py), [Stack-O(n)](Python3/Design/OnlineStockSpan/Stack901.py)||testcase
|👍 918|Medium *|[Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/)|2020/5/15|Array|[Naive-O(n)](Python3/Array/MaximumSumCircularSubarray/Naive918.py), [MinSumSubarray-O(n)](Python3/Array/MaximumSumCircularSubarray/MinSumSubarray918.py)|[Note](Python3/Array/MaximumSumCircularSubarray/Note918.md)|use other approach
|   957|Medium  |[Prison Cells After N Days](https://leetcode.com/problems/prison-cells-after-n-days/)|2020/7/3|Array|[Naive-O(n)](Python3/Array/PrisonCellsAfterNDays/Naive957.py), [LoopDetection-O(n)](Python3/Array/PrisonCellsAfterNDays/LoopDetection957.py)|[Note-O(n)](Python3/Array/PrisonCellsAfterNDays/Note957.md)|
|👍 978|Medium  |[Longest Turbulent Subarray](https://leetcode.com/problems/longest-turbulent-subarray/)|TODO|String|||
|👍 986|Medium *|[Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/)|2020/5/23|Array|[TwoPointer-O(m+n)](Python3/Array/IntervalListIntersections/TwoPointer986.py)|[Note](Python3/Array/IntervalListIntersections/Note986.md)|testcase, do it again
|  993|Easy    |[Cousins in Binary Tree](https://leetcode.com/problems/cousins-in-binary-tree/)|2020/5/7|Binary Tree|[IterativeBFS-O(n)](Python3/BinaryTree/CousinsInBinaryTree/IterativeBFS993.py), [RecursiveDFS-O(n)](Python3/BinaryTree/CousinsInBinaryTree/RecursiveDFS993.py)||testcase
|  997|Easy    |[Find the Town Judge](https://leetcode.com/problems/find-the-town-judge/)|2020/5/10|Array|[Naive-O(n)](Python3/Array/FindTheTownJudge/Naive997.py), [Improve-O(n)](Python3/Array/FindTheTownJudge/Improve997.py)||
|  1008|Medium  |[Construct Binary Search Tree from Preorder Traversal](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/)|2020/4/20|Binary Tree|[Naive-O(n)](Python3/BinaryTree/ConstructBinarySearchTreeFromPreorderTraversal/Naive1008.py), [Naive2-O(n)](Python3/BinaryTree/ConstructBinarySearchTreeFromPreorderTraversal/Naive2_1008.py)|[Note](Python3/BinaryTree/ConstructBinarySearchTreeFromPreorderTraversal/Note1008.md)|testcase
|  1009|Easy    |[Complement of Base 10 Integer](https://leetcode.com/problems/complement-of-base-10-integer/) ([Number Complement](https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3319/))|2020/5/4|BitManipulation|[Naive-O(n)](Python3/BitManipulation/ComplementOfBase10Integer/Naive1009.py), [Pythonic-O(n)](Python3/BitManipulation/ComplementOfBase10Integer/Pythonic1009.py)||testcase
|👍 1029|Easy *  |[Two City Scheduling](https://leetcode.com/problems/two-city-scheduling/)|2020/6/3|Array|[Naive-O(nlogn)](Python3/Array/TwoCityScheduling/Naive1029.py), [Diff-O(nlogn)](Python3/Array/TwoCityScheduling/Diff1029.py), [Sorting-O(nlogn)](Python3/Array/TwoCityScheduling/Sorting1029.py)||-
|👍 1035|Medium *|[Uncrossed Lines](https://leetcode.com/problems/uncrossed-lines/)|2020/5/25|Array|[Naive-O(mn)](Python3/Array/UncrossedLines/Naive1035.py), [BottomUpDP-O(mn)](Python3/Array/UncrossedLines/BottomUpDP1035.py)|[Note](Python3/Array/UncrossedLines/Note1035.md)|testcase, do it again
|👍 1044|Hard  |[Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/)|2020/6/20|String|[Naive](Python3/String/LongestDuplicateSubstring/Naive1044.py), [BinarySearch-RabinKarp-O(nlogn)](Python3/String/LongestDuplicateSubstring/BinarySearch_RabinKarp1044.py)|[Note](Python3/String/LongestDuplicateSubstring/Note1044.md)|do it again
|  1046|Easy    |[Last Stone Weight](https://leetcode.com/problems/last-stone-weight/)|2020/4/12|Array|[Naive-O(n)](Python3/Array/LastStoneWeight/Naive1046.py)||-
|👍 1143|Medium  |[Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)|2019/10/22|String|[BruteForce-O(2ⁿ)](Python3/String/LongestCommonSubsequence/BruteForce1143.py), [DP-O(mn)](Python3/String/LongestCommonSubsequence/DP1143.py)|[Note](Python3/String/LongestCommonSubsequence/Note1143.md)|-
|  1232|Easy    |[Check If It Is a Straight Line](https://leetcode.com/problems/check-if-it-is-a-straight-line/)|2020/5/8|Math|[Naive-O(n)](Python3/Math/CheckIfItIsAStraightLine/Naive1232.py)||-
|👍 1277|Medium  |[Count Square Submatrices with All Ones](https://leetcode.com/problems/count-square-submatrices-with-all-ones/)|2020/5/22|String|[Naive-O(n^4)](Python3/Array/CountSquareSubmatricesWithAllOnes/Naive1277.py), [DP-O(mn)](Python3/Array/CountSquareSubmatricesWithAllOnes/DP1277.py)||testcase, do it again
|👍 1344|Medium  |[Angle Between Hands of a Clock](https://leetcode.com/problems/angle-between-hands-of-a-clock/)|2020/7/14|Math|[Naive-O(1)](Python3/Math/AngleBetweenHandsOfAClock/Naive1344.py)||-
|👍 1425|Hard  |[Constrained Subsequence Sum](https://leetcode.com/problems/constrained-subsequence-sum/)|TODO|Array||[Note](Python3/Array/ConstrainedSubsequenceSum/Note1425.md)|-
|  ???|Easy     |[Counting Elements](https://leetcode.com/explore/other/card/30-day-leetcoding-challenge/528/week-1/3289/)|2020/4/7|Array|[Naive-O(nlogn)](Python3/Array/CountingElements/Naive.py), [SinglePass-O(n)](Python3/Array/CountingElements/SinglePass.py)||testcase
|  ???|Easy     |[Perform String Shifts](https://leetcode.com/explore/other/card/30-day-leetcoding-challenge/529/week-2/3299/)|2020/4/15|String|[Naive-O(n)](Python3/String/PerformStringShifts/Naive.py)||testcase
|  ???|Easy     |[Leftmost Column with at Least a One](https://leetcode.com/explore/other/card/30-day-leetcoding-challenge/530/week-3/3306/)|2020/4/21|Interactive|[Naive-O(mn)](Python3/Interactive/LeftmostColumnWithAtLeastAOne/Naive.py), [BinarySearch-O(n)](Python3/Interactive/LeftmostColumnWithAtLeastAOne/BinarySearch.py), [Improve-O(n+m)](Python3/Interactive/LeftmostColumnWithAtLeastAOne/Improve.py)|[Note](Python3/Interactive/LeftmostColumnWithAtLeastAOne/LeftmostColumnWithAtLeastAOne.md)|testcase, do this again
|  ???|Easy     |[First Unique Number](https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3313/)|2020/4/28|Design|[Naive](Python3/Design/FirstUniqueNumber/Naive.py), [HT Counter](Python3/Design/FirstUniqueNumber/HTCounter.py), [Double Linked List](Python3/Design/FirstUniqueNumber/DLL.py), [Double Linked List + HT](Python3/Design/FirstUniqueNumber/DLLHT.py)|[Note](Python3/Design/FirstUniqueNumber/Note.md)|testcase, improve follow the hint (set, heap)
|  ???|Easy     |[Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree](https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/532/week-5/3315/)|2020/4/30|Binary Tree|[Naive](Python3/BinaryTree/CheckIfAStringIsAValidSequenceFromRootToLeavesPathInABinaryTree/Naive.py)||testcase, improve (like iterative dfs)
|  ???|Easy     |[Is Subsequence](https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3355/)|2020/6/9|String|[Naive-O(n)](Python3/String/IsSubsequence/Naive.py)||testcase

## [Contest](Contest)

## LeetCode Learn Progress

> [LeetCode Explore Learn](https://leetcode.com/explore/learn/)

Introduction to Algorithm

* [Recursion I](https://leetcode.com/explore/learn/card/recursion-i/)

Introduction to Data Structure

* [Binary Tree](https://leetcode.com/explore/learn/card/data-structure-tree/) - [note](Notes/DataStructure/BinaryTree.md)
* [Queue & Stack](https://leetcode.com/explore/learn/card/queue-stack/) - [note](Notes/DataStructure/QueueStack.md)
* [Binary Search Tree](https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/)
* [Trie](https://leetcode.com/explore/learn/card/trie) - [note](Notes/DataStructure/Trie_PrefixTree.md)

Learning about...

* [Binary Search](https://leetcode.com/explore/learn/card/binary-search/)

Design        |  Date    |   Category   |  Implementaiton  |  Remark  | TODO |
--------------|----------|--------------|------------------|----------|------|
Circular Queue|2019/7/4  |Data Structure|[C++](Learn/Cpp/Queue/CircularQueue.cpp)|[Note](Notes/DataStructure/QueueStack.md#Circular-Queue), [Design Circular Queue](https://leetcode.com/problems/design-circular-queue/)|-
Min Stack     |2019/12/26|Data Structure|[C++](Learn/Cpp/Stack/MinStack.cpp)|[Min Stack](https://leetcode.com/problems/min-stack/)|-

## Notes

Data Structure

* [Queue and Stack](Notes/DataStructure/QueueStack.md)
* [Binary Tree](Notes/DataStructure/BinaryTree.md)
* [Priority Queue and Heap](Notes/DataStructure/PriorityQueue_Heap.md)
* [Trie (prefix tree)](Notes/DataStructure/Trie_PrefixTree.md)

Algorithm

* [Dynamic Programming](Notes/Algorithm/DynamicProgramming.md)
* [Binary Search](Notes/Algorithm/BinarySearch.md)

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
>   3. Fibonacci Numbers (Fibonacci Sequence (eg: House Thief, Jump Game))
>      * Fibonacci numbers
>      * Staircase
>      * Number factors
>      * Minimum jumps to reach the end
>      * Minimum jumps with fee
>      * House thief
>   4. Palindromic Subsequence (Shortest Path (eg: Unique Paths I/II))
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
>
> * 0/1 Knapsack
> * Unbounded Knapsack
> * Shortest Path (eg: Unique Paths I/II)
> * Fibonacci Sequence (eg: House Thief, Jump Game)
> * Longest Common Substring/Subsequeunce

### LeetCode Links

* [**LeetCode Algorithms Problems**](https://leetcode.com/problemset/algorithms/)

> 2020 Coronavirus quarantine special events
>
> * [30-Day LeetCoding Challenge](https://leetcode.com/explore/other/card/30-day-leetcoding-challenge) - 2020/4/1~2020/4/30
>   * [🤩 30-Day LeetCoding Challenge 💪🔥 - LeetCode Discuss](https://leetcode.com/discuss/general-discussion/551411/30-day-leetcoding-challenge)
> * [May LeetCoding Challenge](https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/)
>   * [👨‍💻 May LeetCoding Challenge 🧠✨ - LeetCode Discuss](https://leetcode.com/discuss/general-discussion/595334/may-leetcoding-challenge)
> * [June LeetCoding Challenge](https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/)
>   * [🥳💎[LeetCode Polo Shirt] June LeetCoding Challenge! 👕🔥 - LeetCode Discuss](https://leetcode.com/discuss/general-discussion/655704/June-LeetCoding-Challenge)
> * [Explore - LeetCode](https://leetcode.com/explore/challenge/card/july-leetcoding-challenge)
>   * [🔥👕[LeetCode Polo Shirt] July LeetCoding Challenge! 👕🔥 - LeetCode Discuss](https://leetcode.com/discuss/general-discussion/655704/leetcode-polo-shirt-july-leetcoding-challenge)

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
  * [grandyang/leetcode: Provide all my solutions and explanations in Chinese for all the Leetcode coding problems.](https://github.com/grandyang/leetcode)

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

Quick typing math symbol

* MacOS
  * `control + command + space`
* Ubuntu
  * `ctrl + .` in naive GTK Linux apps
  * `ctrl + shift + e + space` in some other apps
  * [How to insert an emoji into a text in Ubuntu 18.04 and later? - Ask Ubuntu](https://askubuntu.com/questions/1045915/how-to-insert-an-emoji-into-a-text-in-ubuntu-18-04-and-later)
  * [Emoji Selector - GNOME Shell Extensions](https://extensions.gnome.org/extension/1162/emoji-selector/)
    * [maoschanz/emoji-selector-for-gnome: This extension provide a popup menu with some emojis ; clicking on an emoji copies it to the clipboard.](https://github.com/maoschanz/emoji-selector-for-gnome)
    * [How do I check my version of GNOME-Shell? - Ask Ubuntu](https://askubuntu.com/questions/13348/how-do-i-check-my-version-of-gnome-shell)
    * `super (win) + .`
  * GNOME Shell Extensions
    * [**How to Use GNOME Shell Extensions [Complete Guide] - It's FOSS**](https://itsfoss.com/gnome-shell-extensions/)
    * [GNOME Shell Extensions](https://extensions.gnome.org/)
    * `gnome-tweaks`
* Windows
  * `win + .`
