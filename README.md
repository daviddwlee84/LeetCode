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

* Virtual Environment
  * [Installing packages using pip and virtual environments — Python Packaging User Guide](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)
  * [Creating a Virtual Environment – Real Python](https://realpython.com/lessons/creating-virtual-environment/)
  * [venv — Creation of virtual environments — Python 3.9.0 documentation](https://docs.python.org/3/library/venv.html)
* Install Latest Python
  * [How to Install Python 3.8 on Ubuntu 18.04 | Linuxize](https://linuxize.com/post/how-to-install-python-3-8-on-ubuntu-18-04/)
* Python Docker
  * [Docker Hub](https://hub.docker.com/_/python)

```sh
docker pull python:3.8
```

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

> *Naive* means the first thought of mine (usually a little better than Brute-Force, but may need to be optimized.)

### LeetCode Patterns

* [Leetcode Patterns – Medium](https://medium.com/leetcode-patterns)
  * Leetcode Pattern 0 - Iterative traversals on Trees
  * Leetcode Pattern 1 - DFS + BFS
  * Leetcode Pattern 2 - Sliding Windows for Strings
  * Leetcode Pattern 3 - Backtracking
  * Leetcode Pattern 4 - Meta Stuff

### Remark

* Category
  * `Category1, Category2, ...`
  * Usually record in (input data) Data Structure. (The Algorithm (and additional/special Data Structure) strategy will be noted in the Method field)
  * Code will be put in the main category folder (i.e. the first one).
  * Some category may be the Related Topic tags marked by LeetCode.
  * (Add Pattern 0~4 in brackets)
  * TODO: Most of the categories need to be updated. (The date before 2018/9/22)
  * TODO: Mark "Good for Beginner" or "Good for Intermediate" etc.

|Number | Difficulty | Problem | Date | Category | Method-TimeComplexity | Remark | TODO |
|-------------:|-------------|-------------|-------------|-------------|-------------|-------------|------|
|👍 001|Easy    |[Two Sum](https://leetcode.com/problems/two-sum/)|2018/3/12|Array, HT|[Naive-O(nlogn)](Python3/Array/TwoSum/Naive001.py), [HT-O(n)](Python3/Array/TwoSum/HashTable001.py), [Sorted HT-O(n)](Python3/Array/TwoSum/SortedHashTable001.py)|[Note](Python3/Array/TwoSum//Note001.md)|-
|  002|Medium  |[Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)|2018/3/12|Linked List|[Naive-O(n)](Python3/LinkedList/AddTwoNumbers/Naive002.py)|[Note](Python3/LinkedList/AddTwoNumbers/Note002.md)|Make a shorter version
|👍 003|Medium *|[Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)|2018/9/24|String, HT|[Sliding Window](Python3/String/LongestSubstringWithoutRepeatingCharacters/SlidingWindow003.py), [Sliding Window Optimized](Python3/String/LongestSubstringWithoutRepeatingCharacters/SlidingWindowOptimized003.py)|[Note](Python3/String/LongestSubstringWithoutRepeatingCharacters/Note003.md)|-
|👍 005|Medium *|[Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)|2019/2/28|String, DP|[Naive-O(n³)](Python3/String/LongestPalindromicSubstring/Naive005.py), [DP-O(n²)](Python3/String/LongestPalindromicSubstring/DP005.py), [Expand Around Center-O(n²)](Python3/String/LongestPalindromicSubstring/ExpandAroundCenter005.py)|[Note](Python3/String/LongestPalindromicSubstring/Note005.md)|-
|  006|Medium  |[ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/)|2018/3/22|Array|[Naive-O(n)](Python3/Array/ZigZagConversion/Naive006.py)|[Note](Python3/Array/ZigZagConversion/Note006.md)|-
|  007|Easy    |[Reverse Integer](https://leetcode.com/problems/reverse-integer/)|2018/3/22|Array|[Naive-O(n)](Python3/Array/ReverseInteger/Naive007.py)|[Note](Python3/Array/ReverseInteger/Note007.md)|-
|  008|Medium  |[String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)|2018/9/30|String (TODO: move to AdHoc)|[Naive-O(n)](Python3/String/StringToInteger/Naive008.py)|[Note](Python3/String/StringToInteger/Note008.md)|-
|  009|Easy    |[Palindrome Number](https://leetcode.com/problems/palindrome-number/)|2018/3/22|Array|[Naive-O(n)](Python3/Array/PalindromeNumber/Naive009.py), [Without using string-O(n)](Python3/Array/PalindromeNumber/NotString009.py)|[Note](Python3/Array/PalindromeNumber/Note009.md)|-
|  010|Hard *  |[Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)|2018/10/13|String|[DC-O((m+n) x 2ⁿ)](Python3/String/RegularExpressionMatching/DC010.py), [Top-Down DP-O(mn)](Python3/String/RegularExpressionMatching/TopDownDP010.py), [Bottom-Up DP-O(mn)](Python3/String/RegularExpressionMatching/BottomUpDP010.py)|[Note](Python3/String/RegularExpressionMatching/Note010.md)|-
|👍 011|Medium *|[Container With Most Water](https://leetcode.com/problems/container-with-most-water/)|2018/9/22|Array|[Naive-O(n²)](Python3/Array/ContainerWithMostWater/Naive011.py), [Two Pointer-O(n)](Python3/Array/ContainerWithMostWater/TwoPointer011.py), [Naive 2-O(n²)](Python3/Array/ContainerWithMostWater/Naive2_011.py, [Two Pointer 2-O(n)](Python3/Array/ContainerWithMostWater/TwoPointer2_011.py)|[Note](Python3/Array/ContainerWithMostWater/Note011.md)|-
|  012|Medium  |[Integer to Roman](https://leetcode.com/problems/integer-to-roman/)|TODO|String (TODO: move to AdHoc)|[Naive-O(n)](Python3/String/IntegerToRoman/Naive012.py)|[Note](Python3/String/IntegerToRoman/Note012.md)|-
|  013|Easy    |[Roman to Integer](https://leetcode.com/problems/roman-to-integer/)|2018/9/29|String (TODO: move to AdHoc)|[Naive-O(n)](Python3/String/RomanToInteger/Naive013.py)|[Note](Python3/String/RomanToInteger/Note013.md)|-
|  014|Easy    |[Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)|2018/9/16|Array|[Naive-O(n*len)](Python3/Array/LongestCommonPrefix/Naive014.py)|[Note](Python3/Array/LongestCommonPrefix/Note014.md)|-
|👍 015|Medium ▲|[3Sum](https://leetcode.com/problems/3sum/)|2018/10/13|Array|[TwoPointer-O(n²)](Python3/Array/3Sum/TwoPointer015.py), [Naive-O(n²)](Python3/Array/3Sum/Naive015.py), [TwoPointer2-O(n²)](Python3/Array/3Sum/TwoPointer2_015.py), [BinarySearch-O(n²)](Python3/Array/3Sum/BinarySearch015.py)|[Note](Python3/Array/3Sum/Note015.md)|do it again
|  016|Medium  |[3Sum Closest](https://leetcode.com/problems/3sum-closest/)|2018/10/13|Array|[TwoPointer-O(n²)](Python3/Array/3SumClosest/TwoPointer016.py)|[Note](Python3/Array/3SumClosest/Note016.md)|-
|  017|Medium  |[Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)|2019/3/1|String|[Backtracking-O(n!)](Python3/String/LetterCombinationsOfAPhoneNumber/Backtracking017.py)|[Note](Python3/String/LetterCombinationsOfAPhoneNumber/Note017.md)|-
|👍 018|Medium ▲|[4Sum](https://leetcode.com/problems/4sum/)|2019/3/2|Array, HT|[GeneralizedTwoPointer-O(n³)](Python3/Array/4Sum/GeneralizedTwoPointer018.py)|[Note](Python3/Array/4Sum/Note018.md)|-
|   019|Medium *|[Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)|2019/3/3|Linked List|[HT-O(n)](Python3/LinkedList/RemoveNthNodeFromEndOfList/HT019.py), [TwoPointer-O(n)](Python3/LinkedList/RemoveNthNodeFromEndOfList/TwoPointer019.py)|[Note](Python3/LinkedList/RemoveNthNodeFromEndOfList/Note019.md), Sina Interview|do it again
|👍 020|Easy    |[Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)|2018/9/15|String, Stack|[Naive-O(n)](Python3/String/ValidParentheses/Naive020.py), [Stack-O(n)](Python3/String/ValidParentheses/Stack020.py), [HashTable-O(n)](Python3/String/ValidParentheses/Dict020.py)|[Note](Python3/String/ValidParentheses/Note020.md), Learn: Queue & Stack|-
|  021|Easy    |[Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)|2018/6/27|Linked List|[Better-O(n)](Python3/LinkedList/MergeTwoSortedLists/Better021.py), [Naive-O(n)](Python3/LinkedList/MergeTwoSortedLists/Naive021.py)|[Note](Python3/LinkedList/MergeTwoSortedLists/Note021.md)|-
|  023|Hard    |[Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)|2018/6/26|Linked List|[Naive-O(kn)](Python3/LinkedList/MergeKSortedLists/Naive023.py), [DC-O(nlogk)](Python3/LinkedList/MergeKSortedLists/DC023.py)|[Note](Python3/LinkedList/MergeKSortedLists/Note023.md)|Compare K each time, Heap, attrgetter
|👍 022|Medium *|[Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)|2019/3/6|String|[Backtracking-O(n!)](Python3/String/GenerateParentheses/Backtracking022.py), [Naive-O(n!)](Python3/String/GenerateParentheses/Naive022.py)|[Note](Python3/String/GenerateParentheses/Note022.md)|-
|  024|Medium  |[Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)|2018/5/31|Linked List|[Naive-O(n)](Python3/LinkedList/SwapNodesInPairs/Naive024.py), [Recursive-O(n)](Python3/LinkedList/SwapNodesInPairs/Recursive024.py)|[Note](Python3/LinkedList/SwapNodesInPairs/Note024.md)|-
|  026|Easy    |[Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)|2018/6/14|Array|[Naive-O(n)](Python3/Array/RemoveDuplicatesfromSortedArray/Naive026.py), [Better-O(n)](Python3/Array/RemoveDuplicatesfromSortedArray/Better026.py)|[Note](Python3/Array/RemoveDuplicatesfromSortedArray/Note026.md)|-
|  027|Easy    |[Remove Element](https://leetcode.com/problems/remove-element/)|2019/7/2|Array|[Naive-O(n)](Python3/Array/RemoveElement/Naive027.py), [Naive2-O(n)](Python3/Array/RemoveElement/Naive2027.py)|[Note](Python3/Array/RemoveElement/Note027.md)|-
|  028|Easy    |[Implement strStr()](https://leetcode.com/problems/implement-strstr/)|2019/7/2|String|[Naive-O(n)](Python3/String/Implement_strStr/Naive028.py)|[Note](Python3/String/Implement_strStr/Note028.md)|-
|  031|Medium ▲|[Next Permutation](https://leetcode.com/problems/next-permutation/)|2019/3/4|Array|[SinglePass-O(n)](Python3/Array/NextPermutation/SinglePass031.py)|[Note](Python3/Array/NextPermutation/Note031.md)|Permutation with duplicates
|👍 033|Medium *|[Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)|2019/3/5|Array|[BinarySearch-O(log(n))](Python3/Array/SearchInRotatedSortedArray/BinarySearch033.py), [BinarySearch2-O(log(n))](Python3/Array/SearchInRotatedSortedArray/BinarySearch2_033.py)|[Note](Python3/Array/SearchInRotatedSortedArray/Note033.md), FreeWheel 2020 Fall Recruit|do it again
|👍 035|Easy    |[Search Insert Position](https://leetcode.com/problems/search-insert-position/)|2019/7/3|Array|[BinarySearch-O(log(n))](Python3/Array/SearchInsertPosition/BinarySearch035.py), [Naive-O(logn)](Python3/Array/SearchInsertPosition/Naive035.py)|[Note](Python3/Array/SearchInsertPosition/Note035.md)|-
|  036|Medium ▼|[Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)|2018/6/21|Array|[HT-O(n)](Python3/Array/ValidSudoku/HashTable036.py)|[Note](Python3/Array/ValidSudoku/Note036.md)|-
|  037|Hard    |[Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)|TODO|Array||[Note](Python3/Array/SudokuSolver/Note037.md)|-
|  038|Easy    |[Count and Say](https://leetcode.com/problems/count-and-say/)|2019/9/30|String|[Naive-O(n)](Python3/String/CountAndSay/Naive038.py)|[Note](Python3/String/CountAndSay/Note038.md)|-
|  039|Medium  |[Combination Sum](https://leetcode.com/problems/combination-sum/)|2019/3/7|Array|[Backtracking-O(n!)](Python3/Array/CombinationSum/Backtracking039.py), [Naive-O(n!)](Python3/Array/CombinationSum/Naive039.py)|[Note](Python3/Array/CombinationSum/Note039.md)|improve time complexity by not use sort
|👍 042|Hard *  |[Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)|TODO|Array|||-
|👍 044|Hard    |[Wildcard Matching](https://leetcode.com/problems/wildcard-matching/)|TODO|String||[Note](Python3/String/WildcardMatching/Note044.md)|DP, NFA
|👍 045|Medium *|[Jump Game II](https://leetcode.com/problems/jump-game-ii/)|2020/10/14|Array|[DP-O(n^2)](Python3/Array/JumpGameII/DP045.py), [Greedy-O(n^2)](Python3/Array/JumpGameII/Greedy045.py), [BFS-O(n^2)](Python3/Array/JumpGameII/BFS045.py), [Greedy 2-O(n^2)](Python3/Array/JumpGameII/Greedy2_045.py)||do it again with all solutions
|👍 046|Medium *|[Permutations](https://leetcode.com/problems/permutations/)|2018/5/31|Array|[Backtracking-O(n!)](Python3/Array/Permutations/Backtracking046.py), [Recursive-O(n!)](Python3/Array/Permutations/Recursive046.py), [DFS Based-O(n!)](Python3/Array/Permutations/DFS046.py)|[Note](Python3/Array/Permutations/Note046.md)|-
|👍 048|Medium *|[Rotate Image](https://leetcode.com/problems/rotate-image/)|2019/12/2|Array|[Naive-O(n)](Python3/Array/RotateImage/Naive048.py)|[Note](Python3/Array/RotateImage/Note048.md), Microsoft 2020 Fall Recruit|-
|👍 049|Medium *|[Group Anagrams](https://leetcode.com/problems/group-anagrams/)|2019/12/3|String, HT|[Naive-O(nk)](Python3/String/GroupAnagrams/Naive049.py), [Sorting-O(nklogk)](Python3/String/GroupAnagrams/Sorting049.py), [Counter-O(nk)](Python3/String/GroupAnagrams/Counter049.py)|[Note](Python3/String/GroupAnagrams/Note049.md)|testcase
|👍 050|Medium *|[Pow(x, n)](https://leetcode.com/problems/powx-n/)|2020/7/16|Math|[Naive-O(n)](Python3/Math/PowXN/Naive050.py), [Recursive-O(logn)](Python3/Math/PowXN/Recursive050.py), [Recursive 2-O(logn)](Python3/Math/PowXN/Recursive2_050.py), [Bit Manipulation-O(logn)](Python3/Math/PowXN/BitManipulation050.py)||-
|👍 051|Hard *  |[N-Queens](https://leetcode.com/problems/n-queens/)|2020/7/25|Array|[Naive-O(n^2)](Python3/Array/NQueens/Naive051.py)||testcase, TODO: another slash way in isValid
|   052|Hard    |[N-Queens II](https://leetcode.com/problems/n-queens-ii/)|2020/7/25|Array|[Naive-O(n^2)](Python3/Array/NQueensII/Naive052.py)||testcase, TODO: another slash way in isValid
|👍 053|Easy ▲  |[Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)|2018/6/12|Array, DP, DC|[BruteForce-O(n³)](Python3/Array/MaximumSubarray/Naive053.py), [DP-O(n)](Python3/Array/MaximumSubarray/DP053.py), [DC-O(nlogn)](Python3/Array/MaximumSubarray/DC053.py)|[Note](Python3/Array/MaximumSubarray/Note053.md)|Do it again
|👍 055|Medium *|[Jump Game](https://leetcode.com/problems/jump-game/)|2020/4/26|Array|[Backtracking-O(2^n)](Python3/Array/JumpGame/Backtracking055.py), [DPTopDown-O(n^2)](Python3/Array/JumpGame/DPTopDown055.py), [DPBottomUp-O(n^2)](Python3/Array/JumpGame/DPBottomUp055.py), [Greedy-O(n)](Python3/Array/JumpGame/Greedy055.py), [Greedy2-O(n)](Python3/Array/JumpGame/Greedy2_055.py)|[Note](Python3/Array/JumpGame/Note055.md), Good DP walk through|-
|  056|Medium *|[Merge Intervals](https://leetcode.com/problems/merge-intervals/)|2020/2/21|Array|[Sorting-O(nlogn)](Python3/Array/MergeIntervals/Sorting056.py), [Naive-O(nlogn)](Python3/Array/MergeIntervals/Naive056.py), [Better-O(nlogn)](Python3/Array/MergeIntervals/Better056.py), [Graph-O(n^2)](Python3/Array/MergeIntervals/Graph056.py), [Tree(Stream)-O(n^2)](Python3/Array/MergeIntervals/Tree056.py)|[Note](Python3/Array/MergeIntervals/Note056.md)|Improve performance
|  058|Easy    |[Length of Last Word](https://leetcode.com/problems/length-of-last-word/)|2019/9/30|String|Not even worth to do|-|-
|👍 060|Medium *|[Permutation Sequence](https://leetcode.com/problems/permutation-sequence/)|2020/6/20|String|[Naive-O(n!)](Python3/String/PermutationSequence/Naive060.py), [Backtracking-O(n!)](Python3/String/PermutationSequence/Backtracking060.py), [Math-O(n)](Python3/String/PermutationSequence/Math060.py)||do it again (math one)
|   061|Medium *|[Rotate List](https://leetcode.com/problems/rotate-list/)|2020/10/7|Linked List|[Naive-O(n)](Python3/LinkedList/RotateList/Naive061.py)||do it again with better way
|👍 062|Medium  |[Unique Paths](https://leetcode.com/problems/unique-paths/)|2020/6/29|Array|[Naive-O(m+n)](Python3/Array/UniquePaths/Naive062.py), [DP-O(mn)](Python3/Array/UniquePaths/DP062.py)||-
|👍 064|Medium *|[Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)|2020/4/19|Array|[Naive-O(mn)](Python3/Array/MinimumPathSum/Naive064.py), [NoAdditionalSpace-O(mn)](Python3/Array/MinimumPathSum/NoAdditionalSpace064.py)||testcase
|  066|Easy    |[Plus One](https://leetcode.com/problems/plus-one/)|2019/10/19|Array|[Naive-O(n)](Python3/Array/PlusOne/Naive066.py), [FullAdder](Python3/Array/PlusOne/FullAdder066.py)|-|-
|  067|Easy    |[Add Binary](https://leetcode.com/problems/add-binary/)|2019/10/22|String|[Adder-O(n)](Python3/String/AddBinary/Adder067.py), [Iterative-O(n)](Python3/String/AddBinary/Iterative067.py)|-|-
|  069|Easy    |[Sqrt(x)](https://leetcode.com/problems/sqrtx/)|2019/10/22|Search|[Naive-O(n)](Python3/Search/Sqrt_x/Naive069.py), [BinarySearch-O(logn)](Python3/Search/Sqrt_x/BinarySearch069.py), [BinarySearch2-O(logn)](Python3/Search/Sqrt_x/BinarySearch2_069.py), [BinarySearch3-O(logn)](Python3/Search/Sqrt_x/BinarySearch3_069.py)|-|-
|  070|Easy    |[Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)|2018/6/13|DP|[DP-O(n)](Python3/Array/ClimbingStairs/DP070.py), [Recursive-O(n)](Python3/Array/ClimbingStairs/Recursive070.py), [Naive-O(n)](Python3/Array/ClimbingStairs/Naive070.py)|[Note](Python3/Array/ClimbingStairs/Note070.md)|-
|  071|Medium  |[Simplify Path](https://leetcode.com/problems/simplify-path/)|2019/12/17|String|[Stack-O(n)](Python3/String/SimplifyPath/Stack071.py), [Naive-O(n)](Python3/String/SimplifyPath/Naive071.py)|[Note](Python3/String/SimplifyPath/Note071.md)|-
|👍 072|Hard    |[Edit Distance](https://leetcode.com/problems/edit-distance/)|2019/10/30|String|[DP-O(mn)](Python3/String/EditDistance/DP072.py), [Recursive-O(mⁿ)](Python3/String/EditDistance/Recursive072.py)|[Note](Python3/String/EditDistance/Note072.md)|-
|👍 075|Medium  |[Sort Colors](https://leetcode.com/problems/sort-colors/)|2020/6/11|Array|[CountingSort-O(n)](Python3/Array/SortColors/CountingSort075.py), [DutchNationalFlagProblem-O(n)](Python3/Array/SortColors/DutchNationalFlagProblem075.py)|[Note](Python3/Array/SortColors/Note075.md)|testcase, do this again
|👍 078|Medium  |[Subsets](https://leetcode.com/problems/subsets/)|2018/6/27|BM|[Binary-O(2ⁿ)](Python3/BitManipulation/Subsets/Binary078.py), [DFSBased-O(2ⁿ)](Python3/BitManipulation/Subsets/DFS078.py), [Backtracking-O(2ⁿ)](Python3/BitManipulation/Subsets/Backtracking078.py), [Naive-O(2ⁿ)](Python3/BitManipulation/Subsets/Naive078.py)|[Note](Python3/BitManipulation/Subsets/Note078.md)|-
|👍 079|Medium *|[Word Search](https://leetcode.com/problems/word-search/)|2020/6/30|Array|[Naive-O(nlogn)](Python3/Array/WordSearch/Naive079.py), [DFS-O(mn4^s)](Python3/Array/WordSearch/DFS079.py), [DFS 2-O(mn4^s)](Python3/Array/WordSearch/DFS2_079.py)||do it again
|  082|Easy    |[Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)|2021/1/5|Linked List|[Naive-O(n)](Python3/LinkedList/RemoveDuplicatesFromSortedListII/Naive082.py)|-|testcase
|  083|Easy    |[Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)|2019/10/22|Linked List|[Naive-O(n)](Python3/LinkedList/RemoveDuplicatesFromSortedList/Naive083.py)|-|-
|  085|Hard    |[Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/)|TODO|Array||[Note](Python3/Array/MaximalRectangle/Note085.md)|-
|👍 086|Medium *|[Partition List](https://leetcode.com/problems/partition-list/)|2020/10/18|Linked List|[TwoPointer-O(n)](Python3/LinkedList/PartitionList/TwoPointer086.py)||[Naive-O(n) Fix WA](Python3/LinkedList/PartitionList/Naive086.py), do it again
|  088|Easy    |[Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)|2019/11/18|Array|[Naive-O(n)](Python3/Array/MergeSortedArray/Naive088.py)||-
|  089|Medium  |[Gray Code](https://leetcode.com/problems/gray-code/)|2021/7/1|BitManipulation|[Direct Ordering-O(n)](Python3/BitManipulation/GrayCode/DirectOrdering89.py), [Mirror Ordering-O(n)](Python3/BitManipulation/GrayCode/MirrorOrdering89.py), [Binary to Gray-O(n)](Python3/BitManipulation/GrayCode/BinaryToGray89.py), [Better-O(n)](Python3/BitManipulation/GrayCode/Better89.py)||-
|  091|Medium *|[Decode Ways](https://leetcode.com/problems/decode-ways/)|2020/9/28|Array|[Naive-O(n)](Python3/Array/DecodeWays/Naive91.py), |[Note](Python3/Array/DecodeWays/Note91.md)|TODO: Top-down DP, Bottom-up DP, Constant Space DP
|👍 092|Medium *|[Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)|2020/9/20|Linked List|[Naive-O(n)](Python3/LinkedList/ReverseLinkedListII/Naive092.py), [OnePass-O(n)](Python3/LinkedList/ReverseLinkedListII/OnePass092.py)||testcase, OnePass
|  093|Medium  |[Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/)|2019/12/16|Array|[Backtracking-O(nlogn)](Python3/Array/RestoreIPAddresses/Backtracking093.py)|[Note](Python3/Array/RestoreIPAddresses/Note93.md)|-
|  094|Medium  |[Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)|2018/5/29|Binary Tree|[Recursive-O(n)](Python3/BinaryTree/BinaryTreeInorderTraversal/Recursive94.py), [Iterative-O(n)](Python3/BinaryTree/BinaryTreeInorderTraversal/Iterative94.py)|[Note](Python3/BinaryTree/BinaryTreeInorderTraversal/Note94.md)|-
|👍 096|Medium *|[Unique Binary Search Tree](https://leetcode.com/problems/unique-binary-search-trees/)|2020/6/24|Binary Tree|[Naive-O(n)](Python3/BinaryTree/UniqueBinarySearchTree/Naive096.py)||testcase, do it again
|  098|Medium ▼|[Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)|2018/6/25|BST|[Inorder-O(n)](Python3/BinaryTree/ValidateBinarySearchTree/InorderTraversal098.py), [DFS-O(n)](Python3/BinaryTree/ValidateBinarySearchTree/DFS098.py)|[Note](Python3/BinaryTree/ValidateBinarySearchTree/Note098.md)|-
|👍 100|Easy    |[Same Tree](https://leetcode.com/problems/same-tree/)|2019/11/20|Binary Tree|[Recursive-O(n)](Python3/BinaryTree/SameTree/Recursive100.py), [Naive-O(n)](Python3/BinaryTree/SameTree/Naive100.py)|[Note](Python3/BinaryTree/SameTree/Note100.md)|-
|👍 101|Easy ▲  |[Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)|2018/6/8|Binary Tree|[Recursive-O(n)](Python3/BinaryTree/SymmetricTree/Recursive101.py), [Iterative-O(n)](Python3/BinaryTree/SymmetricTree/Iterative101.py)|[Note](Python3/BinaryTree/SymmetricTree/Note101.md)|-
|  102|Medium *|[Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)|2018/6/7|Binary Tree|[BFS-O(n)](Python3/BinaryTree/BinaryTreeLevelOrderTraversal/BFS102.py)|[Note](Python3/BinaryTree/BinaryTreeLevelOrderTraversal/Note102.md)|-
|👍  103|Medium *|[Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)|2020/7/22|Binary Tree|[Naive-O(n)](Python3/BinaryTree/BinaryTreeZigzagLevelOrderTraversal/Naive102.py), [Without Reverse-O(n)](Python3/BinaryTree/BinaryTreeZigzagLevelOrderTraversal/WithoutReverse102.py)||-
|👍  104|Easy   |[Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)|2018/6/8|Binary Tree|[Top-Down-O(n)](Python3/BinaryTree/MaximumDepthofBinaryTree/TopDown104.py), [Bottom-up-O(n)](Python3/BinaryTree/MaximumDepthofBinaryTree/BottomUp104.py), [Top-Down2-O(n)](Python3/BinaryTree/MaximumDepthofBinaryTree/TopDown104_2.py)|[Note](Python3/BinaryTree/MaximumDepthofBinaryTree/Note104.md)|-
|  105|Medium *|[Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)|2018/6/9|Binary Tree|[DC-O(n)](Python3/BinaryTree/ConstructBinaryTreefromPreorderandInorderTraversal/DivideAndConquer105.py)|[Note](Python3/BinaryTree/ConstructBinaryTreefromPreorderandInorderTraversal/Note105.md)|-
|  106|Medium *|[Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)|2018/6/8|Binary Tree|[DC-O(n)](Python3/BinaryTree/ConstructBinaryTreefromInorderandPostorderTraversal/DivideAndConquer106.py), [Naive-O(n)](Python3/BinaryTree/ConstructBinaryTreefromInorderandPostorderTraversal/Naive106.py)|[Note](Python3/BinaryTree/ConstructBinaryTreefromInorderandPostorderTraversal/Note106.md)|use index instead of copy array
|  107|Easy    |[Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)|2019/12/30|Binary Tree|[Naive-O(n)](Python3/BinaryTree/BinaryTreeLevelOrderTraversalII/Naive107.py), [Naive 2-O(n)](Python3/BinaryTree/BinaryTreeLevelOrderTraversalII/Naive2_107.py)|-|-
|  108|Easy    |[Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/)|2019/11/13|BST|[Recursive-O(n)](Python3/BinaryTree/ConvertSortedArrayToBinarySearchTree/Recursive108.py)|[Note](Python3/BinaryTree/ConvertSortedArrayToBinarySearchTree/Note108.md)|Test case
|  109|Medium  |[Convert Sorted List to Binary Search Tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/)|2019/11/13|BST|[TwoPointerRecursive-O(nlogn)](Python3/BinaryTree/ConvertSortedListToBinarySearchTree/TwoPointerRecursive109.py)|[Note](Python3/BinaryTree/ConvertSortedListToBinarySearchTree/Note109.md)|Inorder Simulation, Test case
|👍 110|Easy ▲  |[Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/submissions/)|2019/12/30|Binary Tree|[Naive-O(n)](Python3/BinaryTree/BalancedBinaryTree/Naive110.py), [Better Recursive-O(n)](Python3/BinaryTree/BalancedBinaryTree/Recursive110.py), [Postorder Iterative-O(n)](Python3/BinaryTree/BalancedBinaryTree/PostorderIterative110.py)|[Note](Python3/BinaryTree/BalancedBinaryTree/Note110.md)|do it again
|  111|Easy    |[Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)|2019/11/1|Binary Tree|[BFS-O(n)](Python3/BinaryTree/MinimumDepthOfBinaryTree/BFS111.py)||-
|👍 112|Easy    |[Path Sum](https://leetcode.com/problems/path-sum/)|2018/6/8|Binary Tree|[Naive-O(n)](Python3/BinaryTree/PathSum/Naive112.py)|[Note](Python3/BinaryTree/PathSum/Note112.md)|Can be imporved
|👍 113|Medium |[Path Sum II](https://leetcode.com/problems/path-sum-ii/)|2019/12/23|Binary Tree|[Naive-O(n)](Python3/BinaryTree/PathSumII/Naive113.py)|[Note](Python3/BinaryTree/PathSumII/Note113.md)|-
|👍 114|Medium |[Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)|2019/12/31|Binary Tree|[Naive-O(n)](Python3/BinaryTree/FlattenBinaryTreeToLinkedList/Naive114.py)|[Note](Python3/BinaryTree/FlattenBinaryTreeToLinkedList/Note114.md)|more elegant way
|  116|Medium  |[Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)|2019/12/24|Binary Tree|[Naive-O(n)](Python3/BinaryTree/PopulatingNextRightPointersInEachNode/Naive116.py), [DFS-O(n)](Python3/BinaryTree/PopulatingNextRightPointersInEachNode/DFS116.py)|[Note](Python3/BinaryTree/PopulatingNextRightPointersInEachNode/Note116.md)|Test
|  117|Medium *|[Populating Next Right Pointers in Each Node II](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/)|2019/12/24|Binary Tree|[DFS-O(n)](Python3/BinaryTree/PopulatingNextRightPointersInEachNodeII/DFS117.py)|[Note](Python3/BinaryTree/PopulatingNextRightPointersInEachNodeII/Note117.md)|Test
|  118|Easy    |[Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/)|2019/12/28|Array|[Naive-O(n)](Python3/Array/PascalsTriangle/Naive118.py)|[Note](Python3/Array/PascalsTriangle/Note118.md)|Faster approach (memory, recursive, iterative)
|  120|Medium *|[Triangle](https://leetcode.com/problems/triangle/)|2019/12/25|Array|[Naive-O(n)](Python3/Array/Triangle/Naive120.py)|[Note](Python3/Array/Triangle/Note120.md)|less space DP
|  121|Easy    |[Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)|2018/6/13|Array|[Not so DP-O(n)](Python3/Array/BestTimetoBuyandSellStock/DP121.py), [Naive-O(n)](Python3/Array/BestTimetoBuyandSellStock/Naive121.py), [DP-O(n)](Python3/Array/BestTimetoBuyandSellStock/DP2_121.py)|[Note](Python3/Array/BestTimetoBuyandSellStock/Note121.md)|-
|👍 122|Easy    |[Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)|2018/6/14|Array|[Greedy-O(n)](Python3/Array/BestTimetoBuyandSellStockII/Greedy122.py), [Tricky-O(n)](Python3/Array/BestTimetoBuyandSellStockII/Tricky122.py), [Max-O(n)](Python3/Array/BestTimetoBuyandSellStockII/Max122.py)|[Note](Python3/Array/BestTimetoBuyandSellStockII/Note122.md)|-
|👍 124|Hard *  |[Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)|2020/4/29|BinaryTree|[Recursive-O(nlogn)](Python3/BinaryTree/BinaryTreeMaximumPathSum/Recursive124.py)|-|testcase, do this again
|  125|Easy    |[Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)|2020/1/2|String|[Naive-O(n)](Python3/String/ValidPalindrome/Naive125.py), [Naive2 (Two Pointer)-O(n)](Python3/String/ValidPalindrome/Naive2_125.py)|-|-
|  127|Medium *|[Word Ladder](https://leetcode.com/problems/word-ladder/)|2019/12/25|String|[BFS-O(n)](Python3/String/WordLadder/BFS127.py)|[Note](Python3/String/WordLadder/Note127.md)|Bidirectional BFS
|👍 128|Hard ▼  |[Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)|2019/11/14|Array|[Naive-O(n²)](Python3/Array/LongestConsecutiveSequence/Naive128.py), [HT-O(n)](Python3/Array/LongestConsecutiveSequence/HT128.py)|[Note](Python3/Array/LongestConsecutiveSequence/Note128.md)|-
|👍 129|Medium *|[Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/)|2020/6/26|Binary Tree|[Naive-O(nlogn)](Python3/BinaryTree/SumRootToLeafNumbers/Naive129.py), [DFS-O(n)](Python3/BinaryTree/SumRootToLeafNumbers/DFS129.py)||-
|👍 130|Medium  |[Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)|2020/3/25|Array|[Naive-O(mn)](Python3/Array/SurroundedRegions/Naive130.py), [Boarders-O(mn)](Python3/Array/SurroundedRegions/Boarders130.py)|[Note](Python3/Array/SurroundedRegions/Note130.md)|
|  133|Medium  |[Clone Graph](https://leetcode.com/problems/clone-graph/)|2020/1/16|Graph|[Recursive-O(n)](Python3/Graph/CloneGraph/Recursive133.py), [DFS-O(n)](Python3/Graph/CloneGraph/DFS133.py)|[Note](Python3/Graph/CloneGraph/Note133.md), Learn: Queue & Stack|Do it again
|👍 135|Hard *  |[Candy](https://leetcode.com/problems/candy/)|2021/6/27|Array|[Brute Force-O(n^2)](Python3/Array/Candy/BruteForce135.py), [Two arrays-O(n)](Python3/Array/Candy/TwoArrays135.py)||do it again
|👍 136|Easy    |[Single Number](https://leetcode.com/problems/single-number/)|2019/12/18|Array|[HT-O(n)](Python3/Array/SingleNumber/HT136.py), [Set-O(n)](Python3/Array/SingleNumber/Set136.py), [BM-O(n)](Python3/Array/SingleNumber/BM136.py)|[Note](Python3/Array/SingleNumber/Note136.md)|-
|👍 137|Medium *|[Single Number II](https://leetcode.com/problems/single-number-ii/)|2020/6/22|Array|[Naive-O(n)](Python3/Array/SingleNumberII/Naive137.py), [BitManipulation-O(n)](Python3/Array/SingleNumberII/BitManipulation137.py), [BitManipulation 2-O(n)](Python3/Array/SingleNumberII/BitManipulation2_137.py), [Math-O(n)](Python3/Array/SingleNumberII/Math137.py)||testcase
|👍 138|Medium *|[Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/)|2021/2/10|Linked List|[Naive-O(n)](Python3/LinkedList/CopyListWithRandomPointer/Naive138.py), [Interweave-O(n)](Python3/LinkedList/CopyListWithRandomPointer/Interweave138.py), [Map-O(n)](Python3/LinkedList/CopyListWithRandomPointer/Map138.py)||testcase
|👍 139|Medium  |[Word Break](https://leetcode.com/problems/word-break/)|2020/1/14|String|[Recursive-O(2ⁿ)](Python3/String/WordBreak/Recursive139.py), [DP-O(n²)](Python3/String/WordBreak/DP139.py)|[Note](Python3/String/WordBreak/Note139.md)|-
|👍 140|Hard *  |[Word Break II](https://leetcode.com/problems/word-break-ii/)|2020/7/30|String|[Naive-O(n^2)](Python3/String/WordBreakII/Naive140.py), [Backtracking-O(n^2)](Python3/String/WordBreakII/Backtracking140.py), [DP](Python3/String/WordBreakII/DP140.py)||Bottom up DP
|  141|Easy *  |[Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)|2019/12/31|Linked List|[Naive-O(n)](Python3/LinkedList/LinkedListCycle/Naive141.py), [TwoPointer-O(n)](Python3/LinkedList/LinkedListCycle/TwoPointer141.py), [TwoPointer 2-O(n)](Python3/LinkedList/LinkedListCycle/TwoPointer2_141.py)|[Note](Python3/LinkedList/LinkedListCycle/Note141.md), Microsoft|testcase
|👍 142|Medium *|[Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)|2020/6/25|Linked List|[TwoPointer-O(n)](Python3/LinkedList/LinkedListCycleII/TwoPointer142.py)||do it again
|  143|Medium  |[Reorder List](https://leetcode.com/problems/reorder-list/)|2020/3/25|Linked List|[Naive-O(n)](Python3/LinkedList/ReorderList/Naive143.py), [Improved-O(n)](Python3/LinkedList/ReorderList/Improved143.py)||testcase
|  144|Medium  |[Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)|2018/5/29|Binary Tree|[Recursive-O(n)](Python3/BinaryTree/BinaryTreePreorderTraversal/Recursive144.py), [Iterative-O(n)](Python3/BinaryTree/BinaryTreePreorderTraversal/Iterative144.py)|[Note](Python3/BinaryTree/BinaryTreePreorderTraversal/Note144.md)|-
|  145|Hard ▼  |[Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)|2018/6/2|Binary Tree|[Recursive-O(n)](Python3/BinaryTree/BinaryTreePostorderTraversal/Recursive145.py), [Iterative-O(n)](Python3/BinaryTree/BinaryTreePostorderTraversal/Iterative145.py)|[Note](Python3/BinaryTree/BinaryTreePostorderTraversal/Note145.md)|-
|👍 146|Hard * ▼|[LRU Cache](https://leetcode.com/problems/lru-cache/)|2018/6/25|Design|[Naive](Python3/Design/LRUCache/Naive146.py), [OrderedDict](Python3/Design/LRUCache/OrderedDict146.py), [DoubleLinkedList](Python3/Design/LRUCache/DoubleLinkedList146.py)|[Note](Python3/Design/LRUCache/Note146.md)|
|  147|Medium  |[Insertion Sort List](https://leetcode.com/problems/insertion-sort-list/)|2020/1/14|Linked List|[Naive-O(n²)](Python3/LinkedList/InsertionSortList/Naive147.py)|[Note](Python3/LinkedList/InsertionSortList/Note147.md)|Do it again with other style
|👍 148|Medium *|[Sort List](https://leetcode.com/problems/sort-list/)|2020/5/11|Linked List|[MergeSort-O(nlogn)](Python3/LinkedList/SortList/MergeSort148.py)||Do it again, [InsertionSort-O(n^2)](Python3/LinkedList/SortList/InsertionSort148.py), testcase
|👍 150|Medium |[Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)|2020/2/10|Array|[Stack-O(n)](Python3/Array/EvaluateReversePolishNotation/Stack150.py)|[Note](Python3/Array/EvaluateReversePolishNotation/Note150.md), Learn: Queue & Stack|-
|  151|Medium *|[Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/)|2019/10/22|String|[Pythonic-O(n)](Python3/String/ReverseWordsInAString/Pythonic151.py), [Trick-O(n)](Python3/String/ReverseWordsInAString/Trick151.py), [Naive-O(n)](Python3/String/ReverseWordsInAString/Naive151.py), [C Style-O(n)](Python3/String/ReverseWordsInAString/CStyle151.py)|[Note](Python3/String/ReverseWordsInAString/Note151.md), Microsoft Intern Interview|-
|👍 153|Medium *|[Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)|2020/7/25|Array|[Naive-O(logn)](Python3/Array/FindMinimumInRotatedSortedArray/Naive153.py), [Simpler-O(logn)](Python3/Array/FindMinimumInRotatedSortedArray/Simpler153.py)||-
|👍 154|Hard *  |[Find Minimum in Rotated Sorted Array II](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)|2020/7/25|Array|[Naive-O(logn)](Python3/Array/FindMinimumInRotatedSortedArrayII/Naive154.py), [YetAnother-O(logn)](Python3/Array/FindMinimumInRotatedSortedArrayII/YetAnother154.py)||-
|  155|Easy    |[Min Stack](https://leetcode.com/problems/min-stack/)|2018/6/28|Design|[Naive](Python3/Design/MinStack/Naive155.py), [Improve](Python3/Design/MinStack/Improve155.py)|[Note](Python3/Design/MinStack/Note155.md), Learn: Queue & Stack|Naive?!
|  167|Easy    |[Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)|2019/9/18|Array|[TwoPointer-O(n)](Python3/Array/TwoSumII/TwoPointer167.py)|[Note](Python3/Array/TwoSumII/Note167.md)|-
|  169|Easy    |[Majority Element](https://leetcode.com/problems/majority-element/)|2020/5/6|Array|[Naive-O(n)](Python3/Array/MajorityElement/Naive169.py), [Counter-O(n)](Python3/Array/MajorityElement/Counter169.py), [Sorting-O(nlogn)](Python3/Array/MajorityElement/Sorting169.py), [Boyer-Moore Voting-O(n)](Python3/Array/MajorityElement/Voting169.py)||-
|👍 174|Hard *  |[Dungeon Game](https://leetcode.com/problems/dungeon-game/)|2020/6/21|Array|[DP-O(mn)](Python3/Array/DungeonGame/DP174.py)||do it again, TODO: bottom-up dp with binary search
|  189|Easy *  |[Rotate Array](https://leetcode.com/problems/rotate-array/)|2018/6/14|Array|[NaiveInPlace-O(k)](Python3/Array/RotateArray/NaiveInPlace189.py), [ExtraArray-O(n)](Python3/Array/RotateArray/UseArray189.py), [Simplest-O(n)](Python3/Array/RotateArray/Simplest189.py)|[Note](Python3/Array/RotateArray/Note189.md)|TODO: (Try all other solutions e.g. Cyclic Replacements / Reverse)
|  190|Easy    |[Reverse Bits](https://leetcode.com/problems/rotate-array/)|2020/7/12|Bit Manipulation|[Naive-O(n)](Python3/BitManipulation/ReverseBits/Naive190.py), [String-O(n)](Python3/BitManipulation/ReverseBits/String190.py)||testcase
|  191|Easy    |[Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)|2021/2/1|Bit Manipulation|[Naive-O(n)](Python3/BitManipulation/NumberOf1Bits/Naive191.py)||testcase, other alternatives
|  198|Easy    |[House Robber](https://leetcode.com/problems/house-robber/)|2018/6/14|DP|[DP-O(n)](Python3/DynamicProgramming/HouseRobber/DP198.py)|[Note](Python3/DynamicProgramming/HouseRobber/Note198.md)|Can improve space complexity
|👍 199|Medium *|[Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)|2021/2/6|Binary Tree|[Naive-O(n)](Python3/BinaryTree/BinaryTreeRightSideView/Naive199.py)||testcase
|👍 200|Medium *|[Number of Islands](https://leetcode.com/problems/number-of-islands/)|2019/7/5|Search|[BFS-O(n²)](Python3/Search/NumberOfIslands/BFS200.py), [DFS-O(n²)](Python3/Search/NumberOfIslands/DFS200.py)|[Note](Python3/Search/NumberOfIslands/Note200.md), Learn: Queue & Stack, Dropbox OA|try Union, do this again
|👍 201|Medium |[Bitwise AND of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/)|2020/4/23|BitManipulation|[Naive-O(n)](Python3/BitManipulation/BitwiseANDOfNumbersRange/Naive201.py), [Improve-O(n)](Python3/BitManipulation/BitwiseANDOfNumbersRange/Improve201.py)||
|  202|Easy    |[Happy Number](https://leetcode.com/problems/happy-number/)|2020/4/2|Math|[Naive-O(n)](Python3/Math/HappyNumber/Naive202.py)||testcase
|  203|Easy    |[Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/)|2020/3/18|Linked List|[Dummy Node-O(n)](Python3/LinkedList/RemoveLinkedListElements/Naive203.py), [Single Pointer-O(n)](Python3/LinkedList/RemoveLinkedListElements/SinglePointer203.py)||testcase
|👍 204|Easy *  |[Count Primes](https://leetcode.com/problems/count-primes/)|TODO|Math|||-
|  206|Easy    |[Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)|2018/6/26|Linked List|[Iterative-O(n)](Python3/LinkedList/ReverseLinkedList/Iterative206.py), [Recursive-O(n)](Python3/LinkedList/ReverseLinkedList/Recursive206.py)|[Note](Python3/LinkedList/ReverseLinkedList/Note206.md), Microsoft Intern Interview|-
|👍 207|Medium *|[Course Schedule](https://leetcode.com/problems/course-schedule/)|2020/7/18|Array|[CycleDetect-O(n)](Python3/Array/CourseSchedule/CycleDetect207.py), [TopologicalSort-O(n)](Python3/Array/CourseSchedule/TopologicalSort207.py), [DFS-O(n)](Python3/Array/CourseSchedule/DFS207.py)|-|do it again
|👍 208|Medium *|[Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)|2018/6/24|Design|[Naive](Python3/Design/ImplementTrie/Naive208.py), [Trie (using Hashmap)](Python3/Design/ImplementTrie/Trie208.py), [Trie (using Array)](Python3/Design/ImplementTrie/Trie_array208.py)|[Note](Python3/Design/ImplementTrie/Note208.md)|testcase
|👍 210|Medium *|[Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)|2020/7/18|Array|[TopologicalSort-O(n)](Python3/Array/CourseScheduleII/TopologicalSort210.py)|-|do it again, testcase
|👍 211|Medium *|[Add and Search Word - Data structure design](https://leetcode.com/problems/add-and-search-word-data-structure-design/)|2020/6/30|Design|[Naive-O(n)](Python3/Design/AddAndSearchWord/Naive211.py), [RegEx-O(n)](Python3/Design/AddAndSearchWord/RegEx211.py), [Tire-O(n)](Python3/Design/AddAndSearchWord/Tire211.py)|[Note](Python3/Design/AddAndSearchWord/Note211.md), [Tire 2-O(n)](Python3/Design/AddAndSearchWord/Tire2_211.py)|do it again
|👍 212|Hard *  |[Word Search II](https://leetcode.com/problems/word-search-ii/)|2020/6/30|Array|[Tire-O(n)](Python3/Array/WordSearchII/Naive212.py)|-|do it again, testcase
|👍 214|Hard *  |[Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/)|~~2020/11/8~~ TODO|String||[Note](Python3/String/ShortestPalindrome/Note214.md)|
|👍 215|Medium *|[Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)|2019/9/18|Array|[Naive-O(nlogn)](Python3/Array/KthLargestElementInAnArray/Naive215.py), [QuickSort-O(n)](Python3/Array/KthLargestElementInAnArray/QuickSort215.py), [SelectionSortLike-O(nk)](Python3/Array/KthLargestElementInAnArray/SelectionSortLike215.py), [Heap (Cheat)-O(nlogn)](Python3/Array/KthLargestElementInAnArray/HeapCheat215.py), [Heap-O(nlogn)](Python3/Array/KthLargestElementInAnArray/Heap215.py), [QuickSelect-O(n)](Python3/Array/KthLargestElementInAnArray/QuickSelect215.py), [QuickSelect2-O(n)](Python3/Array/KthLargestElementInAnArray/QuickSelect2_215.py)|[Note](Python3/Array/KthLargestElementInAnArray/Note215.md), Microsoft Intern Interview|do it again
|👍 216|Medium *|[Combination Sum III](https://leetcode.com/problems/combination-sum-iii/)|TODO|Math|[Naive-O(n)](Python3/Math/CombinationSumIII/Naive216.py)||DP
|👍 221|Medium *|[Maximal Square](https://leetcode.com/problems/maximal-square/)|2020/4/27|Array|[Naive-O(k x (mn)^2)](Python3/Array/MaximalSquare/Naive221.py), [BruteForce-O((mn)^2)](Python3/Array/MaximalSquare/BruteForce221.py), [DP-O(mn)](Python3/Array/MaximalSquare/DP221.py), [Better DP-O(mn)](Python3/Array/MaximalSquare/DP_2_221.py)|[Note](Python3/Array/MaximalSquare/Note221.md)|-
|👍 221|Medium *|[Count Complete Tree Nodes](https://leetcode.com/problems/count-complete-tree-nodes/)|2020/6/23|Binary Tree|[Naive-O(n)](Python3/BinaryTree/CountCompleteTreeNodes/Naive221.py), [BinarySearch-O(n)](Python3/BinaryTree/CountCompleteTreeNodes/BinarySearch221.py)||testcase
|  225|Easy    |[Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)|2018/6/24|Design|[Two Queue](Python3/Design/ImplementStackusingQueues/TwoQueue225.py)|[Note](Python3/Design/ImplementStackusingQueues/Note225.md), Learn: Queue & Stack|-
|👍 226|Easy *  |[Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)|2020/6/1|Binary Tree|[Naive](Python3/BinaryTree/InvertBinaryTree/Naive226.py)|[Note](Python3/BinaryTree/InvertBinaryTree/Note226.md)|-
|👍 230|Medium *|[Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)|2020/5/20|Binary Tree|[Naive-O(n)](Python3/BinaryTree/KthSmallestElementInABST/Naive230.py), [Iterative-O(n)](Python3/BinaryTree/KthSmallestElementInABST/Iterative230.py)|[Note](Python3/BinaryTree/KthSmallestElementInABST/Note230.md)|testcase
|  231|Easy *  |[Power of Two](https://leetcode.com/problems/power-of-two/)|2020/6/8|Math|[Naive-O(n)](Python3/Math/PowerOfTwo/Naive231.py), [String-O(n)](Python3/Math/PowerOfTwo/String231.py), [BitManipulation-O(n)](Python3/Math/PowerOfTwo/BitManipulation231.py)||do it again
|  232|Easy    |[Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)|2018/6/24|Design|[Two Stack](Python3/Design/ImplementQueueusingStacks/TwoStack232.py)|[Note](Python3/Design/ImplementQueueusingStacks/Note232.md), Learn: Queue & Stack|-
|👍 235|Easy    |[Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)|2021/6/30|Binary Tree|[Naive-O(n)](Python3/BinaryTree/LowestCommonAncestorOfABinarySearchTree/Naive235.py)||-
|👍 236|Medium  |[Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)|2018/6/10|Binary Tree|[Naive-O(n)](Python3/BinaryTree/LowestCommonAncestorofaBinaryTree/Naive236.py), [Naive 2-O(n)](Python3/BinaryTree/LowestCommonAncestorofaBinaryTree/Naive2_236.py), [Elegant-O(n)](Python3/BinaryTree/LowestCommonAncestorofaBinaryTree/Elegant236.py)|[Note](Python3/BinaryTree/LowestCommonAncestorofaBinaryTree/Note236.md), [Naive 3-O(n)](Python3/BinaryTree/LowestCommonAncestorofaBinaryTree/Naive3_236.py)|testcase
|  237|Easy    |[Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/)|2020/3/18|Linked List|[Naive-O(1)](Python3/LinkedList/DeleteNodeInALinkedList/Naive237.py)|(not worth to do)|testcase..
|👍 238|Medium *|[Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)|2020/3/18|Array|[ProductList-O(n)](Python3/Array/ProductOfArrayExceptSelf/ProductList238.py), [ProductList2-O(n)](Python3/Array/ProductOfArrayExceptSelf/ProductList2_238.py), [SingleProductList-O(n)](Python3/Array/ProductOfArrayExceptSelf/SingleProductList238.py)|[Note](Python3/Array/ProductOfArrayExceptSelf/Note238.md)|do it again
|👍 239|Hard * |[Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)|TODO|Array|[Naive-O(n^2)](Python3/Array/SlidingWindowMaximum/Naive239.py), [Monotonic Queue-O(n)](Python3/Array/SlidingWindowMaximum/MonotonicQueue239.py)|Dropbox 2021 Summer Intern OA, Facebook 2021 Summer Intern OA|do this now!!
|  242|Easy    |[Valid Anagram](https://leetcode.com/problems/valid-anagram/)|2021/2/11|String|[Naive-O(n)](Python3/String/ValidAnagram/Naive242.py)||testcase
|  252|Easy *|[Meeting Rooms](https://leetfree.com/problems/meeting-rooms.html) (premium)|2020/2/20|Array|[Sorting-O(nlogn)](Python3/Array/MeetingRooms/Sorting252.py)|[Note](Python3/Array/MeetingRooms/Note252.md), Facebook|-
|👍 253|Medium *|[Meeting Rooms II](https://leetfree.com/problems/meeting-rooms-ii.html) (premium)|2020/3/14|Array|[Sorting-O(nlogn)](Python3/Array/MeetingRoomsII/Sorting253.py)|[Note](Python3/Array/MeetingRoomsII/Note253.md), Facebook|-
|👍 257|Easy ▲  |[Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/)|2018/6/11|Binary Tree|[Iterative-O(n)](Python3/BinaryTree/BinaryTreePaths/Iterative257.py), [Recursive-O(n)](Python3/BinaryTree/BinaryTreePaths/Recursive257.py)|[Note](Python3/BinaryTree/BinaryTreePaths/Note257.md), Learn: Queue & Stack|-
|   258|Easy    |[Add Digits](https://leetcode.com/problems/add-digits/)|2020/3/18|Array|[Naive-O(n)](Python3/Array/AddDigits/Naive258.py), [Iterative-O(n)](Python3/Array/AddDigits/Iterative258.py), [NoLoop-O(1)](Python3/Array/AddDigits/NoLoop258.py)|[Note](Python3/Array/AddDigits/Note258.md), Microsoft, not good|-
|👍 260|Medium *|[Single Number III](https://leetcode.com/problems/single-number-iii/)|2020/6/22|Array|[Naive-O(n)](Python3/Array/SingleNumberIII/Naive260.py), [BitManipulation-O(n)](Python3/Array/SingleNumberIII/BitManipulation260.py)||
|   263|Easy    |[Ugly Number](https://leetcode.com/problems/ugly-number/)|2020/7/4|Array|[Naive-O(n)](Python3/Math/UglyNumber/Naive263.py)||
|👍 264|Medium *|[Ugly Number II](https://leetcode.com/problems/ugly-number-ii/)|2020/7/4|Array|[PriorityQueue-O(n)](Python3/Math/UglyNumberII/PriorityQueue264.py), [DP-O(n)](Python3/Math/UglyNumberII/DP264.py)|[Note](Python3/Math/UglyNumberII/Note264.md), Microsoft Intern Interview|do it again
|   268|Easy    |[Missing Number](https://leetcode.com/problems/missing-number/)|2022/12/18|Array|[Naive-O(n^2)](Python3/Array/MissingNumber/Naive268.py), [BitManipulation-O(n)](Python3/Array/MissingNumber/BitManipulation268.py)||testcase
|👍 269|Hard *  |[Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)|TODO|Array|||-
|   278|Easy    |[First Bad Version](https://leetcode.com/problems/first-bad-version/)|2020/5/1|Iteractive|[Naive-O(logn)](Python3/Array/FirstBadVersion/Naive278.py)||testcase
|   274|Medium  |[H-Index](https://leetcode.com/problems/h-index/)|2020/6/18|Array|[CumulativeSum-O(n)](Python3/Array/H-Index/CumulativeSum274.py)|sorting-based solution see 275|testcase, do it again
|   275|Medium  |[H-Index II](https://leetcode.com/problems/h-index-ii/)|2020/6/18|Array|[Linear-O(n)](Python3/Array/H-IndexII/Linear275.py), [BinarySearch-O(n)](Python3/Array/H-IndexII/BinarySearch275.py)||testcase, do it again
|👍 279|Medium *|[Perfect Squares](https://leetcode.com/problems/perfect-squares/)|2019/8/22|Search|[BFS-O(n)](Python3/Search/PerfectSquares/BFS279.py), [Recursive-O(n!)](Python3/Search/PerfectSquares/Recursive279.py), [Top-Down DP-O(n)](Python3/Search/PerfectSquares/TopDownDP279.py), [Linear Check-O(n * sqrt(n))](Python3/Search/PerfectSquares/LinearCheck279.py), [Bottom-Up DP-O(n)](Python3/Search/PerfectSquares/BottomUpDP279.py), [Math-O(sqrt(n))](Python3/Search/PerfectSquares/Math279.py)|[Note](Python3/Search/PerfectSquares/Note279.md)|do it again
|👍 285|Medium *|[Inorder Successor in BST](https://leetcode.com/problems/inorder-successor-in-bst/) (premium)|~~2020/11/2~~ TODO|Binary Tree|[Iterative-O(logn)](Python3/BinaryTree/InorderSuccessorInBST/Naive285.py)|[Note](Python3/BinaryTree/InorderSuccessorInBST/Note285.md)|do it again, testcase
|👍 287|Medium  |[Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)|2020/6/25|Array|[Naive-O(n^2)](Python3/Array/FindTheDuplicateNumber/Naive287.py), [TwoPointer(Linked List)-O(n)](Python3/Array/FindTheDuplicateNumber/TwoPointer287.py), [Set-O(n)](Python3/Array/FindTheDuplicateNumber/Set287.py), [Linked List-O(n)](Python3/Array/FindTheDuplicateNumber/LinkedList287.py)||do it again, testcase
|   283|Easy    |[Move Zeroes](https://leetcode.com/problems/move-zeroes/)|2020/4/4|Array|[Naive-O(n)](Python3/Array/MoveZeroes/Naive283.py), [TwoPointer-O(n)](Python3/Array/MoveZeroes/TwoPointer283.py)|-|testcase
|   284|Medium  |[Peeking Iterator](https://leetcode.com/problems/peeking-iterator/)|2021/2/8|Design|[Naive-O(1)](Python3/Design/PeekingIterator/Naive284.py)|-|testcase
|   290|Easy    |[Word Pattern](https://leetcode.com/problems/word-pattern/)|2022/12/18|String|[HashMap-O(n)](Python3/String/WordPattern/HashMap290.py)|-|-
|  297|Hard    |[Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)|2019/11/14|Binary Tree|[Naive-O(n)](Python3/BinaryTree/SerializeAndDeserializeBinaryTree/Naive297.py), [Naive2-O(n)](Python3/BinaryTree/SerializeAndDeserializeBinaryTree/Naive2_297.py)|[Note](Python3/BinaryTree/SerializeAndDeserializeBinaryTree/Note297.md)|do it again with pre-order + queue
|👍 300|Medium *|[Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)|2019/11/11|Array|[BruteForce-O(2ⁿ)](Python3/Array/LongestIncreasingSubsequence/BruteForce300.py), [MemoryRecursive-O(n²)](Python3/Array/LongestIncreasingSubsequence/MemoryRecursive300.py), [DP-O(n²)](Python3/Array/LongestIncreasingSubsequence/DP300.py), [BinarySearch-O(nlogn)](Python3/Array/LongestIncreasingSubsequence/BinarySearch300.py), [DP 2-O(n²)](Python3/Array/LongestIncreasingSubsequence/DP2_300.py), [BinarySearch 2-O(nlogn)](Python3/Array/LongestIncreasingSubsequence/BinarySearch2_300.py)|[Note](Python3/Array/LongestIncreasingSubsequence/Note300.md)|do it again
|  303|Easy *   |[Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/)|2021/7/3|Design|[PrefixSum-O(1)](Python3/Design/RangeSumQuery-Immutable/PrefixSum303.py)|good for beginner|-
|👍 304|Medium *|[Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/)|2021/7/3|Design|[Naive-O(n^2)](Python3/Design/RangeSumQuery2D-Immutable/Naive304.py), [PrefixSum-O(1)](Python3/Design/RangeSumQuery2D-Immutable/PrefixSum304.py)||-
|👍 309|Medium *|[Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)|2020/7/29|Array|[StateMachine-O(n)](Python3/Array/BestTimeToBuyAndSellStockWithCooldown/StateMachine309.py), [DP-O(n)](Python3/Array/BestTimeToBuyAndSellStockWithCooldown/DP309.py)||-
|👍 310|Medium *|[Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees/)|~~2020/11/8~~ TODO|Graph|||-
|👍 315|Hard *  |[Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)|2021/6/26|Array|[Binary Index Tree-O(nlogn)](Python3/Array/CountOfSmallerNumbersAfterSelf/BinaryIndexedTree315.py), [Merge Sort-TODO](Python3/Array/CountOfSmallerNumbersAfterSelf/MergeSort315.py)|[Note](Python3/Array/CountOfSmallerNumbersAfterSelf/Note315.md)|do it again
|👍 316|Medium *|[Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/)|2020/10/11|String|[Greedy-O(n)](Python3/String/RemoveDuplicateLetters/Greedy316.py)||do it again
|👍 322|Medium *|[Coin Change](https://leetcode.com/problems/coin-change/)|2020/10/5|Array|[Naive-O(n)](Python3/Array/CoinChange/Naive322.py), [DP-O(n * a)](Python3/Array/CoinChange/DP322.py)||testcase, do it again
|👍 324|Medium *|[Wiggle Sort II](https://leetcode.com/problems/wiggle-sort-ii/)|2021/2/7|Array|[Naive-O(n)](Python3/Array/WiggleSortII/Naive324.py), [Median-O(n)](Python3/Array/WiggleSortII/Median324.py)||testcase, DO IT AGAIN
|👍 328|Medium *|[Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/)|2020/5/16|Linked List|[Naive-O(n)](Python3/LinkedList/OddEvenLinkedList/Naive328.py)||testcase, do it again
|👍 329|Hard *  |[Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/)|2021/7/30|Graph|[DFS](Python3/Graph/LongestIncreasingPathInAMatrix/DFS329.py)||do it again
|👍 330|Hard    |[Patching Array](https://leetcode.com/problems/patching-array/)|2020/8/17|Array|[Naive-O(n^2)](Python3/Array/PatchingArray/Naive330.py), [Trick-O(n)](Python3/Array/PatchingArray/Trick330.py)||-
|👍 332|Medium *|[Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/)|2020/6/28|Array|[Naive-O(n)](Python3/Array/ReconstructItinerary/Naive332.py), [EulerianPath-O(ElogE)](Python3/Array/ReconstructItinerary/EulerianPath332.py), [DFS-O(nlogn)](Python3/Array/ReconstructItinerary/DFS332.py)||do it again
|   338|Easy    |[Counting Bits](https://leetcode.com/problems/counting-bits/)|2022/12/18|BitManipulation|[Naive-O(n)](Python3/BitManipulation/CountingBits/Naive338.py), [Naive2-O(n)](Python3/BitManipulation/CountingBits/Naive2_338.py)||-
|   342|Easy    |[Power of Four](https://leetcode.com/problems/power-of-four/)|2020/8/4|Math|[Naive-O(n)](Python3/Math/PowerOfFour/Naive342.py), [Math-O(n)](Python3/Math/PowerOfFour/Math342.py)||testcase
|   344|Easy    |[Reverse String](https://leetcode.com/problems/reverse-string/)|2020/6/4|String|[Naive-O(n)](Python3/String/ReverseString/Naive344.py), [Recursive-O(n)](Python3/String/ReverseString/Recursive344.py)|[Note](Python3/String/ReverseString/Note344.md)|testcase
|👍 347|Medium *|[Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements)|2019/9/27|Array|[Naive-O(nlogn)](Python3/Array/TopKFrequentElements/Naive347.py), [HT Heap-O(nlogk)](Python3/Array/TopKFrequentElements/HTHeap347.py), [HT Heap 2-O(nlogk)](Python3/Array/TopKFrequentElements/HTHeap2_347.py), [Quickselect-avg O(n)](Python3/Array/TopKFrequentElements/Quickselect347.py), [Bucket Sort-O(n)](Python3/Array/TopKFrequentElements/BucketSort347.py), [HT-O(n)](Python3/Array/TopKFrequentElements/HT347.py)|[Note](Python3/Array/TopKFrequentElements/Note347.md)|-
|   363|Hard *  |[Max Sum of Rectangle No Larger Than K](https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/)|2021/7/3|Array|[Prefix Sum-O(m^2 n^2)](Python3/Array/MaxSumOfRectangleNoLargerThanK/PrefixSum363.py)|Similar problem: 325, 363, 560, 974, 1074|do it again
|   367|Easy    |[Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/)|2020/5/9|Math|[Naive-O(n)](Python3/Math/ValidPerfectSquare/Naive367.py), [BinarySearch-O(n)](Python3/Math/ValidPerfectSquare/BinarySearch367.py)|-|testcase
|👍 368|Medium  |[Largest Divisible Subset](https://leetcode.com/problems/largest-divisible-subset/)|2020/6/13|Array|[Naive-O(n!)](Python3/Array/LargestDivisibleSubset/Naive368.py), [DP-O(n²)](Python3/Array/LargestDivisibleSubset/DP368.py)|[Note](Python3/Array/LargestDivisibleSubset/Note368.md)|do it again (DP)
|👍 373|Medium  |[Find K Pairs with Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/)|2020/5/3|Array|[Priority Queue-O(klogk)](Python3/Array/FindKPairsWithSmallestSums/PriorityQueue373.py), [Heap Merge Sort](Python3/Array/FindKPairsWithSmallestSums/HeapMergeSort373.py)|related to 1439 (competition)|testcase, do it again
|👍 376|Medium  |[Wiggle Subsequence](https://leetcode.com/problems/wiggle-subsequence/)|2020/9/13|Array|[Naive-O(n)](Python3/Array/WiggleSubsequence/Naive376.py), [BottomUpDP-O(n)](Python3/Array/WiggleSubsequence/BottomUpDP376.py)||
|👍 378|Medium  |[Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)|2021/7/7|Array|[Naive-O(n^2logn)](Python3/Array/KthSmallestElementInASortedMatrix/Naive378.py)|[Note](Python3/Array/KthSmallestElementInASortedMatrix/Note378.md)|do it again (merge sort, binary search)
|   380|Medium  |[Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/)|2020/6/12|Design|[Naive-O(1)](Python3/Design/InsertDeleteGetRandomO(1)/Naive380.py)||testcase, use HT + array
|👍 382|Medium *|[Linked List Random Node](https://leetcode.com/problems/linked-list-random-node/)|~~2020/11/8~~ TODO|Linked List|||Reservoir Sampling
|   383|Easy    |[Ransom Note](https://leetcode.com/problems/ransom-note/)|2020/5/4|String|[Naive-O(n)](Python3/String/RansomNote/Naive383.py)|-|testcase
|   387|Easy    |[First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/)|2020/5/5|String|[Naive-O(n)](Python3/String/FirstUniqueCharacterInAString/Naive387.py)|-|testcase
|👍 402|Medium  |[Remove K Digits](https://leetcode.com/problems/remove-k-digits/)|2020/5/13|String|[Naive-O(n)](Python3/String/RemoveKDigits/Greedy402.py)||do this again
|   404|Easy    |[Sum of Left Leaves](https://leetcode.com/problems/sum-of-left-leaves/)|2020/8/1|BinaryTree|[Naive-O(n)](Python3/BinaryTree/SumOfLeftLeaves/Naive404.py)|-|testcase
|👍 406|Medium *|[Queue Reconstruction by Height](https://leetcode.com/problems/queue-reconstruction-by-height/)|2020/6/6|Array|[Sorting-O(n^2)](Python3/Array/QueueReconstructionByHeight/Sorting402.py), [InsertFromLowest-O(nlogn)](Python3/Array/QueueReconstructionByHeight/InsertFromLowest402.py), [InsertFromHighest-O(nlogn)](Python3/Array/QueueReconstructionByHeight/InsertFromHighest402.py), [Insert-O(n)](Python3/Array/QueueReconstructionByHeight/Insert402.py)|[Note](Python3/Array/QueueReconstructionByHeight/Note402.md)|do it again, testcase
|👍 413|Medium *|[Arithmetic Slices](https://leetcode.com/problems/arithmetic-slices/)|2021/2/18|Array|[Naive-O(n)](Python3/Array/ArithmeticSlices/Naive413.py)||testcase, do it again
|👍 416|Medium *|[Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)|TODO|Array|||-
|   419|Medium  |[Battleships in a Board](https://leetcode.com/problems/battleships-in-a-board/)|TODO|Array|||
|👍 426|Medium  |[Convert Binary Search Tree to Sorted Doubly Linked List](https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list)|TODO|BST|Need subscription||-
|👍 430|Medium *|[Flatten a Multilevel Doubly Linked List](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/)|2020/7/10|Linked List|[Naive-O(n)](Python3/LinkedList/FlattenAMultilevelDoublyLinkedList/Naive430.py), [Stack-O(n)](Python3/LinkedList/FlattenAMultilevelDoublyLinkedList/Stack430.py)||do it again, testcase
|👍 435|Medium *|[Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)|TODO|Array|||
|👍 438|Medium  |[Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)|2020/5/17|String|[Naive-O(n)](Python3/String/FindAllAnagramsInAString/Naive438.py)||-
|👍 441|Easy    |[Arranging Coins](https://leetcode.com/problems/arranging-coins/)|2020/7/1|Math|[Naive-O(n)](Python3/Math/ArrangingCoins/Naive441.py), [Binary Search-O(logn)](Python3/Math/ArrangingCoins/BinarySearch441.py), [Math-O(1)](Python3/Math/ArrangingCoins/Math441.py)||-
|👍 451|Medium  |[Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/)|2020/5/22|String|[Naive-O(n)](Python3/String/SortCharactersByFrequency/Naive451.py), [PQ-O(n)](Python3/String/SortCharactersByFrequency/PQ451.py)||testcase
|👍 452|Medium  |[Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)|2020/10/10|Array|[Naive-O(nlogn)](Python3/Array/MinimumNumberOfArrowsToBurstBalloons/Naive452.py)||-
|  460|Hard    |[LFU Cache](https://leetcode.com/problems/lfu-cache/)|2018/6/25|Design|[Naive](Python3/Design/LFUCache/Naive460.py)|[Note](Python3/Design/LFUCache/Note460.md)|OrderedDict, LinkedList
|  461|Easy    |[Hamming Distance](https://leetcode.com/problems/hamming-distance/)|2020/7/5|Bit Manipulation|[Naive-O(n)](Python3/BitManipulation/HammingDistance/Naive461.py)||testcase
|👍 463|Easy    |[Island Perimeter](https://leetcode.com/problems/island-perimeter/)|2020/7/7|Array|[Naive-O(n)](Python3/Array/IslandPerimeter/Naive463.py), [Neighbour-O(n)](Python3/Array/IslandPerimeter/Neighbour463.py), [CountEdge-O(n)](Python3/Array/IslandPerimeter/CountEdge463.py), [StringEdge-O(n)](Python3/Array/IslandPerimeter/StringEdge463.py)||testcase
|👍 468|Medium  |[Validate IP Address](https://leetcode.com/problems/validate-ip-address/)|2020/6/16|String|[Naive-O(n)](Python3/String/ValidateIPAddress/Naive468.py)|Microsoft Intern Interview|todo: pure regex, pure rule
|👍 477|Medium  |[Total Hamming Distance](https://leetcode.com/problems/total-hamming-distance/)|TODO|Bit Manipulation|||[string approach](https://leetcode.com/problems/total-hamming-distance/discuss/96229/python-via-strings)
|👍 494|Medium |[Target Sum](https://leetcode.com/problems/target-sum/)|2020/2/10|Array|[Naive-O(n²)](Python3/Array/TargetSum/Naive494.py), [RecursiveWithMemory-O(l*n)](Python3/Array/TargetSum/RecursiveWithMemory494.py), [2D DP-O(l*n)](Python3/Array/TargetSum/DP_2D_494.py), [1D DP-O(l*n)](Python3/Array/TargetSum/DP_1D_494.py)|[Note](Python3/Array/TargetSum/Note494.md), Learn: Queue & Stack|more optimization on DP
|👍 518|Medium *|[Coin Change 2](https://leetcode.com/problems/coin-change-2/)|2020/6/7|Array|[Naive-O(n^t)](Python3/Array/CoinChange2/Naive518.py), [DP-O(nt)](Python3/Array/CoinChange2/DP518.py)|[Note](Python3/Array/CoinChange2/Note518.md)|do it again (bottom up 1D DP)
|👍 503|Medium *|[Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/)|TODO|Array|||-
|   520|Easy    |[Detect Capital](https://leetcode.com/problems/detect-capital/)|2020/8/3|String|[Naive-O(n)](Python3/String/DetectCapital/Naive520.py), [CapitalCount-O(n)](Python3/String/DetectCapital/CapitalCount520.py), [RegEx-O(n)](Python3/String/DetectCapital/RegEx520.py)||-
|👍 525|Medium *|[Contiguous Array](https://leetcode.com/problems/contiguous-array/)|2020/4/13|Array|[Naive-O(n²)](Python3/Array/ContiguousArray/Naive525.py), [HT-O(n)](Python3/Array/ContiguousArray/HT525.py), [ExtraArray-O(n)](Python3/Array/ContiguousArray/ExtraArray525.py), [HT2-O(n)](Python3/Array/ContiguousArray/HT2_525.py)|Didi Interview|do it again
|👍 526|Medium  |[Beautiful Arrangement](https://leetcode.com/problems/beautiful-arrangement/)|2021/1/3|Array|[BruteForce-O(n!)](Python3/Array/BeautifulArrangement/BruteForce526.py), [Backtracking with Memory](Python3/Array/BeautifulArrangement/BacktrackingWithMemory526.py)||testcase
|  528|Medium *|[Random Pick with Weight](https://leetcode.com/problems/random-pick-with-weight/)|2020/6/5|Design|[Naive-O(n)](Python3/Design/RandomPickWithWeight/Naive528.py), [Naive2-O(n)](Python3/Design/RandomPickWithWeight/Naive2_528.py), [Binary Search-O(n)](Python3/Design/RandomPickWithWeight/BinarySearch528.py), [OnePass-O(n)](Python3/Design/RandomPickWithWeight/OnePass528.py)|[Note](Python3/Design/RandomPickWithWeight/Note528.md)|testcase
|  532|Medium  |[K-diff Pairs in an Array](https://leetcode.com/problems/k-diff-pairs-in-an-array/)|2020/10/3|Array|[Naive-O(n^2)](Python3/Array/K-diffPairsInAnArray/Naive532.py), [HT-O(n)](Python3/Array/K-diffPairsInAnArray/HT532.py), [Naive2-O(n)](Python3/Array/K-diffPairsInAnArray/Naive2_532.py)||testcase
|👍 538|Medium *|[Convert BST to Greater Tree](https://leetcode.com/problems/convert-bst-to-greater-tree/)|2021/2/7|BinaryTree|[DFS-O(n)](Python3/BinaryTree/ConvertBSTToGreaterTree/DFS538.py), [Array-O(n)](Python3/BinaryTree/ConvertBSTToGreaterTree/Array538.py)|same as problem 1038|testcase, do it again
|👍 540|Medium  |[Single Element in a Sorted Array](https://leetcode.com/problems/single-element-in-a-sorted-array/)|2020/5/12|Array|[Naive-O(n)](Python3/Array/SingleElementInASortedArray/Naive540.py), [BinarySearchXOR-O(logn)](Python3/Array/SingleElementInASortedArray/BinarySearchXOR540.py)||testcase
|👍 543|Easy    |[Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)|2020/4/11|Binary Tree|[DFS-O(n)](Python3/BinaryTree/DiameterOfBinaryTree/DFS543.py)||testcase
|👍 547|Medium  |[Friend Circles](https://leetcode.com/problems/friend-circles/)|~~2020/11/2~~ TODO|Graph|[DFS-O(n)](Python3/Graph/FriendCircles/DFS547.py)||testcase
|  559|Easy    |[Maximum Depth of N-ary Tree](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/)|2019/11/14|Tree|[Naive-O(n)](Python3/BinaryTree/MaximumDepthOfNaryTree/Naive559.py), [DFS-O(n)](Python3/BinaryTree/MaximumDepthOfNaryTree/DFS559.py)|[Note](Python3/BinaryTree/MaximumDepthOfNaryTree/Note559.md)|Test
|👍 560|Medium  |[Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)|2020/4/22|Array|[BruteForce-O(n^3)](Python3/Array/SubarraySumEqualsK/BruteForce560.py), [CumulativeSum-O(n²)](Python3/Array/SubarraySumEqualsK/CumulativeSum560.py), [WithoutSpace-O(n²)](Python3/Array/SubarraySumEqualsK/WithoutSpace560.py), [HT-O(n)](Python3/Array/SubarraySumEqualsK/HT560.py)|[Note](Python3//Array/SubarraySumEqualsK/Note560.md)|
|  563|Easy    |[Binary Tree Tilt](https://leetcode.com/problems/binary-tree-tilt/)|2020/8/1|BinaryTree|[Naive-O(n)](Python3/BinaryTree/BinaryTreeTilt/Naive559.py)||iterative
|  566|Easy    |[Reshape the Matrix](https://leetcode.com/problems/reshape-the-matrix/)|2021/7/5|Array|[Naive-O(n)](Python3/Array/ReshapeTheMatrix/Naive566.py)|good for beginner|-
|👍 567|Medium  |[Permutation in String](https://leetcode.com/problems/permutation-in-string/)|2020/5/18|String|[Naive-O(n)](Python3/String/PermutationInString/Naive567.py)||testcase
|  594|Easy    |[Longest Harmonious Subsequence](https://leetcode.com/problems/longest-harmonious-subsequence/)|2021/2/4|Array|[Naive-O(n)](Python3/Array/LongestHarmoniousSubsequence/Naive594.py)||testcase
|👍 621|Medium *|[Task Scheduler](https://leetcode.com/problems/task-scheduler/)|2020/7/28|Array|[Naive-O(nlogn)](Python3/Array/TaskScheduler/Naive621.py)|[Note](Python3/Array/TaskScheduler/Note621.md)|TODO: more solution
|👍 624|Easy    |[Maximum Distance in Arrays](https://leetcode.com/problems/maximum-distance-in-arrays/) (premium)|2020/10/5|Array|[Naive-O(n)](Python3/Array/MaximumDistanceInArrays/Naive624.py)||-
|👍 630|Hard *  |[Course Schedule III](https://leetcode.com/problems/course-schedule-iii/)|2021/5/2|Array|[Naive-O(n+1!)](Python3/Array/CourseScheduleIII/Naive630.py), [Top-down DP-O(n * d)](Python3/Array/CourseScheduleIII/TopDownDP630.py), [PriorityQueue-O(nlogn)](Python3/Array/CourseScheduleIII/PriorityQueue630.py)|-|topological sort, Do it again (all total official has 6)
|👍 636|Medium *|[Exclusive Time of Functions](https://leetcode.com/problems/exclusive-time-of-functions/)|2020/10/25|Ad Hoc|[Naive-O(n)](Python3/AdHoc/ExclusiveTimeOfFunctions/Naive636.py)||testcase
|   639|Hard    |[Decode Ways II](https://leetcode.com/problems/decode-ways-ii/)|TODO|String||-|-
|👍 658|Medium *|[Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements)|2021/7/2|Array|[Naive-O(logn + k)](Python3/Array/FindKClosestElements/Naive658.py), [Double Sort-O(nlogn + klogk)](Python3/Array/FindKClosestElements/DoubleSort658.py), [Find Left Bound-O(log(n - k) + k)](Python3/Array/FindKClosestElements/FindLeftBound658.py)|[Note](Python3/Array/FindKClosestElements/Note658.md)|do it again
|👍 662|Medium *|[Maximum Width of Binary Tree](https://leetcode.com/problems/maximum-width-of-binary-tree/)|2020/7/9|Binary Tree|[Naive-O(n)](Python3/BinaryTree/MaximumWidthOfBinaryTree/Naive662.py)|[Note](Python3/BinaryTree/MaximumWidthOfBinaryTree/Note662.md)|do it again (more elegant way), testcase
|👍 665|Medium *|[Non-decreasing Array](https://leetcode.com/problems/non-decreasing-array)|2021/5/4|Array|[Greedy-O(n)](Python3/Array/NonDecreasingArray/Greedy665.py)|[Note](Python3/Array/NonDecreasingArray/Note665.md)|do it again
|👍 669|Medium *|[Trim a Binary Search Tree](https://leetcode.com/problems/trim-a-binary-search-tree/)|2021/2/2|Binary Tree|[Recursive DFS-O(n)](Python3/BinaryTree/TrimABinarySearchTree/RecursiveDFS669.py)||do it again
|👍 673|Medium  |[Number of Longest Increasing Subsequence](https://leetcode.com/problems/number-of-longest-increasing-subsequence/)|TODO|String|||
|👍 674|Easy    |[Longest Continuous Increasing Subsequence](https://leetcode.com/problems/longest-continuous-increasing-subsequence/)|TODO|String|||
|👍 678|Medium *|[Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/)|2020/4/17|String|[Naive-O(n*3^n)](Python3/String/ValidParenthesisString/Naive678.py), [DP-O(n)](Python3/String/ValidParenthesisString/DP678.py), [Greedy-O(n)](Python3/String/ValidParenthesisString/Greedy678.py)|[Note](Python3/String/ValidParenthesisString/Note678.md)|do this again
|👍 684|Medium *|[Redundant Connection](https://leetcode.com/problems/redundant-connection/)|2020/10/18|Graph|[DSU-O(n)](Python3/Graph/RedundantConnection/DSU684.py), [Union Find-O(n)](Python3/Graph/RedundantConnection/UnionFind684.py), [Cycle Prevention DFS-O(n^2)](Python3/Graph/RedundantConnection/CyclePreventionDFS684.py)||do this again, DFS, BFS
|👍 685|Hard    |[Redundant Connection II](https://leetcode.com/problems/redundant-connection-ii/)|TODO|Graph|||DSU
|  687|Medium  |[Longest Univalue Path](https://leetcode.com/problems/longest-univalue-path/)|TODO|Binary Tree||[Note](Python3/BinaryTree/LongestUnivaluePath/Note687.md)|-
|👍 698|Medium *|[Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/)|TODO|Array|||-
|  700|Easy    |[Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/)|2020/6/15|Binary Tree|[Naive-O(logn)](Python3/BinaryTree/SearchInABinarySearchTree/Naive700.py)||testcase
|  701|Medium *|[Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/)|2020/10/6|Binary Tree|[Naive-O(logn)](Python3/BinaryTree/InsertIntoABinarySearchTree/Naive701.py), [Recursive-O(logn)](Python3/BinaryTree/InsertIntoABinarySearchTree/Recursive701.py)||testcase
|  703|Easy    |[Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)|2020/5/8|Design|[Naive-O(n)](Python3/Design/KthLargestElementInAStream/Naive703.py), [Heap-O(n)](Python3/Design/KthLargestElementInAStream/Heap703.py)|[Note](Python3/Design/KthLargestElementInAStream/Note703.md)|testcase
|  704|Easy    |[Binary Search](https://leetcode.com/problems/binary-search)|2020/5/9|Array|[Iterative(<)-O(logn)](Python3/Array/BinarySearch/Iterative704.py), [Recursive(<=)-O(logn)](Python3/Array/BinarySearch/Recursive704.py)||Test
|  705|Easy    |[Design HashSet](https://leetcode.com/problems/design-hashset/)|2020/8/2|Design|[Naive-O(1)](Python3/Design/DesignHashSet/Naive705.py), [With Hash Function-O(1)](Python3/Design/DesignHashSet/HashFunction705.py)||testcase
|  733|Easy    |[Flood Fill](https://leetcode.com/problems/flood-fill/)|2020/5/11|Array|[Naive-O(n)](Python3/Array/FloodFill/Naive733.py), [DFS-O(n)](Python3/Array/FloodFill/DFS733.py), [IterativeDFS-O(n)](Python3/Array/FloodFill/IterativeDFS733.py)||Test
|👍 718|Medium *|[Maximum Length of Repeated Subarray](https://leetcode.com/problems/maximum-length-of-repeated-subarray/)|2021/7/8|Array|[DP-O(mn)](Python3/Array/MaximumLengthOfRepeatedSubarray/DP718.py)||Binary Search with Rolling Hash
|👍 739|Medium  |[Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)|2019/12/26|Array|[Naive-O(n²)](Python3/Array/DailyTemperatures/Naive739.py), [Naive2-O(n²)](Python3/Array/DailyTemperatures/Naive2_739.py), [Stack-O(n²)](Python3/Array/DailyTemperatures/Stack739.py)|[Note](Python3/Array/DailyTemperatures/Note739.md), Learn: Queue & Stack|-
|👍 745|Hard *  |[Prefix and Suffix Search](https://leetcode.com/problems/prefix-and-suffix-search/)|2021/5/1|Design|[RegularExpression-O(n)](Python3/Design/PrefixAndSuffixSearch/RE745.py), [Paired Trie-O(nk^2 + qk)](Python3/Design/PrefixAndSuffixSearch/PairedTrie745.py), [Trie of Suffix Wrapped Words-O(nk^2 + qk)](Python3/Design/PrefixAndSuffixSearch/SuffixWrappedWords745.py), [Double Set-O(n)](Python3/Design/PrefixAndSuffixSearch/DoubleSet745.py)||-
|👍 752|Medium  |[Open the Lock](https://leetcode.com/problems/open-the-lock/)|2019/7/5|Search|[BFS-O(n²)](Python3/Search/OpenTheLock/BFS752.py)|[Note](Python3/Search/OpenTheLock/Note752.md), Learn: Queue & Stack|Improve time complexity
|👍 763|Medium  |[Partition Labels](https://leetcode.com/problems/partition-labels/)|2020/9/5|String|[Naive-O(n)](Python3/String/PartitionLabels/Naive763.py)||
|  771|Easy    |[Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/)|2020/5/2|String|[Naive-O(n)](Python3/String/JewelsAndStones/Naive771.py), [Naive2-O(n)](Python3/String/JewelsAndStones/Naive2_771.py)||testcase
|👍 784|Easy    |[Letter Case Permutation](https://leetcode.com/problems/letter-case-permutation/)|2020/7/25|String|[Naive-O(n)](Python3/String/LetterCasePermutation/Naive784.py), [Naive 2-O(n)](Python3/String/LetterCasePermutation/Naive2_784.py)||testcase, more elegant way
|👍 785|Medium *|[Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/)|2021/2/14|Graph|[Color-O(V + E)](Python3/Graph/IsGraphBipartite/Color785.py)||do it again
|👍 787|Medium *|[Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)|2020/6/14|Graph|[Naive-O(V + E)](Python3/Graph/CheapestFlightsWithinKStops/Naive787.py), [BFS-O(V + E)](Python3/Graph/CheapestFlightsWithinKStops/BFS787.py), [DP-O(n²)](Python3/Graph/CheapestFlightsWithinKStops/DP787.py), [Naive 2-O(V + E)](Python3/Graph/CheapestFlightsWithinKStops/Naive2_787.py)|[Note](Python3/Graph/CheapestFlightsWithinKStops/Note787.md)|do it again
|  790|Medium   |[Domino and Tromino Tiling](https://leetcode.com/problems/domino-and-tromino-tiling/)|TODO|Geometry|||-
|👍 797|Medium *|[All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-target/)|2020/7/24|Graph|[Naive-O(2^n)](Python3/Graph/AllPathsFromSourceToTarget/Naive797.py), [Backtracking-O(2^n)](Python3/Graph/AllPathsFromSourceToTarget/Backtracking797.py)||do it again, TODO: iterative version
|  801|Medium  |[Minimum Swaps To Make Sequences Increasing](https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/)|TODO|Array||[Note](Python3/Array/MinimumSwapsToMakeSequencesIncreasing/Note801.md)|-
|  821|Easy    |[Shortest Distance to a Character](https://leetcode.com/problems/shortest-distance-to-a-character/)|2021/2/7|String|[Naive-O(n)](Python3/String/ShortestDistanceToACharacter/Naive821.py)||testcase, more simple approach
|   829|Hard *  |[Consecutive Numbers Sum](https://leetcode.com/problems/consecutive-numbers-sum/)|TODO|Math|||-
|  844|Easy    |[Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/)|2020/4/9|String|[Naive-O(n)](Python3/String/BackspaceStringCompare/Naive844.py), [TwoPointer-O(n)](Python3/String/BackspaceStringCompare/TwoPointer844.py)||testcase
|👍 857|Hard *  |[Minimum Cost to Hire K Workers](https://leetcode.com/problems/minimum-cost-to-hire-k-workers/)|2020/3/17|Array|[Greedy-O(n²logn)](Python3/Array/MinimumCostToHireKWorkers/Greedy857.py), [Greedy w/ PQ-O(nlogn)](Python3/Array/MinimumCostToHireKWorkers/GreedyPQ857.py)|[Note](Python3/Array/MinimumCostToHireKWorkers/Note857.md)|-
|  859|Easy    |[Buddy Strings](https://leetcode.com/problems/buddy-strings/)|2020/10/12|String|[Naive-O(n^2)](Python3/String/BuddyStrings/Naive859.py), [Naive-O(n)](Python3/String/BuddyStrings/Naive2_859.py), [Better-O(n)](Python3/String/BuddyStrings/Better859.py)||testcase
|👍 862|Hard *  |[Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/)|TODO|Array||[Note](Python3/Array/ShortestSubarrayWithSumAtLeastK/Note862.md)|Deque
|👍 875|Medium  |[Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)|2020/8/8|Array|[Naive-O(n)](Python3/Array/KokoEatingBananas/Naive875.py), [BinarySearch-O(n)](Python3/Array/KokoEatingBananas/BinarySearch875.py)||testcase
|  876|Easy    |[Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)|2020/4/8|Linked List|[Naive-O(n)](Python3/LinkedList/MiddleOfTheLinkedList/Naive876.py), [TwoPointer-O(n)](Python3/LinkedList/MiddleOfTheLinkedList/TwoPointer876.py)||testcase
|👍 886|Medium *|[Possible Bipartition](https://leetcode.com/problems/possible-bipartition/)|2020/5/27|Array|||testcase
|👍 901|Medium  |[Online Stock Span](https://leetcode.com/problems/online-stock-span/)|2020/5/19|Design|[Naive-O(n)](Python3/Design/OnlineStockSpan/Naive901.py), [Count-O(n)](Python3/Design/OnlineStockSpan/Count901.py), [Stack-O(n)](Python3/Design/OnlineStockSpan/Stack901.py)||testcase
|   916|Medium  |[Word Subsets](https://leetcode.com/problems/word-subsets/)|2020/9/5|String|[Naive-O(n)](Python3/String/WordSubsets/Naive916.py), [Improve-O(n)](Python3/String/WordSubsets/Improve916.py), [Counter-O(n)](Python3/String/WordSubsets/Counter916.py)||testcase
|👍 918|Medium *|[Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/)|2020/5/15|Array|[Naive-O(n)](Python3/Array/MaximumSumCircularSubarray/Naive918.py), [MinSumSubarray-O(n)](Python3/Array/MaximumSumCircularSubarray/MinSumSubarray918.py)|[Note](Python3/Array/MaximumSumCircularSubarray/Note918.md)|use other approach
|  933|Easy    |[Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/)|2020/10/1|Design|[Naive-O(n)](Python3/Design/NumberOfRecentCells/Naive933.py), [Naive2-O(n)](Python3/Design/NumberOfRecentCells/Naive2_933.py), [BinarySearch-O(logn)](Python3/Design/NumberOfRecentCells/BinarySearch933.py), [Queue-O(min(n, 3000))](Python3/Design/NumberOfRecentCells/Queue933.py), [CircularList-O(n)](Python3/Design/NumberOfRecentCells/CircularList933.py)||testcase
|👍 952|Hard *  |[Largest Component Size by Common Factor](https://leetcode.com/problems/largest-component-size-by-common-factor/)|TODO|Array|||
|   957|Medium  |[Prison Cells After N Days](https://leetcode.com/problems/prison-cells-after-n-days/)|2020/7/3|Array|[Naive-O(n)](Python3/Array/PrisonCellsAfterNDays/Naive957.py), [LoopDetection-O(n)](Python3/Array/PrisonCellsAfterNDays/LoopDetection957.py)|[Note-O(n)](Python3/Array/PrisonCellsAfterNDays/Note957.md)|
|👍 978|Medium  |[Longest Turbulent Subarray](https://leetcode.com/problems/longest-turbulent-subarray/)|TODO|String|||
|👍 986|Medium *|[Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/)|2020/5/23|Array|[TwoPointer-O(m+n)](Python3/Array/IntervalListIntersections/TwoPointer986.py)|[Note](Python3/Array/IntervalListIntersections/Note986.md)|testcase, do it again
|  993|Easy    |[Cousins in Binary Tree](https://leetcode.com/problems/cousins-in-binary-tree/)|2020/5/7|Binary Tree|[IterativeBFS-O(n)](Python3/BinaryTree/CousinsInBinaryTree/IterativeBFS993.py), [RecursiveDFS-O(n)](Python3/BinaryTree/CousinsInBinaryTree/RecursiveDFS993.py)||testcase
|👍 994|Medium  |[Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)|2020/9/13|Graph|[Naive-O(V + E)](Python3/Graph/RottingOranges/Naive994.py)||
|  997|Easy    |[Find the Town Judge](https://leetcode.com/problems/find-the-town-judge/)|2020/5/10|Array|[Naive-O(n)](Python3/Array/FindTheTownJudge/Naive997.py), [Improve-O(n)](Python3/Array/FindTheTownJudge/Improve997.py)||
|👍 1004|Medium  |[Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/)|2021/6/29|Array|[Naive-O(n)](Python3/Array/MaxConsecutiveOnesIII/Naive1004.py)||-
|  1008|Medium  |[Construct Binary Search Tree from Preorder Traversal](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/)|2020/4/20|Binary Tree|[Naive-O(n)](Python3/BinaryTree/ConstructBinarySearchTreeFromPreorderTraversal/Naive1008.py), [Naive2-O(n)](Python3/BinaryTree/ConstructBinarySearchTreeFromPreorderTraversal/Naive2_1008.py)|[Note](Python3/BinaryTree/ConstructBinarySearchTreeFromPreorderTraversal/Note1008.md)|testcase
|  1009|Easy    |[Complement of Base 10 Integer](https://leetcode.com/problems/complement-of-base-10-integer/) ([Number Complement](https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3319/))|2020/5/4|BitManipulation|[Naive-O(n)](Python3/BitManipulation/ComplementOfBase10Integer/Naive1009.py), [Pythonic-O(n)](Python3/BitManipulation/ComplementOfBase10Integer/Pythonic1009.py), [BM-O(n)](Python3/BitManipulation/ComplementOfBase10Integer/BM1009.py)||testcase
|👍 1010|Easy    |[Pairs of Songs With Total Durations Divisible by 60](https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/)|2020/10/14|Array|[Naive-O(n^2)](Python3/Array/PairsOfSongsWithTotalDurationsDivisibleBy60/Naive1010.py), [PrefixSum-O(n)](Python3/Array/PairsOfSongsWithTotalDurationsDivisibleBy60/PrefixSum1010.py)||testcase
|👍 1029|Easy *  |[Two City Scheduling](https://leetcode.com/problems/two-city-scheduling/)|2020/6/3|Array|[Naive-O(nlogn)](Python3/Array/TwoCityScheduling/Naive1029.py), [Diff-O(nlogn)](Python3/Array/TwoCityScheduling/Diff1029.py), [Sorting-O(nlogn)](Python3/Array/TwoCityScheduling/Sorting1029.py)||-
|👍 1035|Medium *|[Uncrossed Lines](https://leetcode.com/problems/uncrossed-lines/)|2020/5/25|Array|[Naive-O(mn)](Python3/Array/UncrossedLines/Naive1035.py), [BottomUpDP-O(mn)](Python3/Array/UncrossedLines/BottomUpDP1035.py)|[Note](Python3/Array/UncrossedLines/Note1035.md)|testcase, do it again
|👍 1041|Medium  |[Robot Bounded In Circle](https://leetcode.com/problems/robot-bounded-in-circle/)|2020/11/8|Array|[Naive-O(n)](Python3/Array/RobotBoundedInCircle/Naive1041.py)|LinkedIn 2021 Summer Intern|testcase, do it again
|👍 1044|Hard  |[Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/)|2020/6/20|String|[Naive](Python3/String/LongestDuplicateSubstring/Naive1044.py), [BinarySearch-RabinKarp-O(nlogn)](Python3/String/LongestDuplicateSubstring/BinarySearch_RabinKarp1044.py)|[Note](Python3/String/LongestDuplicateSubstring/Note1044.md)|do it again
|  1046|Easy    |[Last Stone Weight](https://leetcode.com/problems/last-stone-weight/)|2020/4/12|Array|[Naive-O(n)](Python3/Array/LastStoneWeight/Naive1046.py)||-
|  1047|Easy    |[Remove All Adjacent Duplicates In String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/)|2021/6/28|String|[Naive-O(n^n)](Python3/String/RemoveAllAdjacentDuplicatesInString/Naive1047.py), [Stack-O(n)](Python3/String/RemoveAllAdjacentDuplicatesInString/Stack1047.py), [Remove Pattern-O(n)](Python3/String/RemoveAllAdjacentDuplicatesInString/RemovePattern1047.py)|Good for beginner|-
|  1071|Easy    |[Greatest Common Divisor of Strings](https://leetcode.com/problems/greatest-common-divisor-of-strings/)|2022/12/19|String|[Naive-O(n^n)](Python3/String/GreatestCommonDivisorOfStrings/Naive1071.py)||-
|👍  1091|Medium  |[Shortest Path in Bnary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/)|2021/2/13|Graph|[Naive-O(n)](Python3/Graph/ShortestPathInBinaryMatrix/Naive1091.py)||testcase
|👍 1094|Medium  |[Car Pooling](https://leetcode.com/problems/car-pooling/)|2020/9/21|Array|[Naive-O(n)](Python3/Array/CarPooling/Naive1094.py)||testcase
|👍 1143|Medium  |[Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)|2019/10/22|String|[BruteForce-O(2ⁿ)](Python3/String/LongestCommonSubsequence/BruteForce1143.py), [DP-O(mn)](Python3/String/LongestCommonSubsequence/DP1143.py)|[Note](Python3/String/LongestCommonSubsequence/Note1143.md)|-
|👍 1200|Medium *|[Minimum Absolute Difference](https://leetcode.com/problems/minimum-absolute-difference/)|TODO|Array|||-
|👍 1220|Hard *  |[Count Vowels Permutation](https://leetcode.com/problems/count-vowels-permutation/)|2021/7/4|Math|[DP-O(5n)](Python3/Math/CountVowelsPermutation/DP1220.py)|good DP problem|do it again
|  1232|Easy    |[Check If It Is a Straight Line](https://leetcode.com/problems/check-if-it-is-a-straight-line/)|2020/5/8|Math|[Naive-O(n)](Python3/Math/CheckIfItIsAStraightLine/Naive1232.py)||-
|👍 1249|Medium *|[Minimum Remove to Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/)|2020/7/25|String|[Naive-O(n)](Python3/String/MinimumRemoveToMakeValidParentheses/Naive1249.py), [Naive 2-O(n)](Python3/String/MinimumRemoveToMakeValidParentheses/Naive2_1249.py)||stack, follow up: O(1) space
|👍 1277|Medium  |[Count Square Submatrices with All Ones](https://leetcode.com/problems/count-square-submatrices-with-all-ones/)|2020/5/22|String|[Naive-O(n^4)](Python3/Array/CountSquareSubmatricesWithAllOnes/Naive1277.py), [DP-O(mn)](Python3/Array/CountSquareSubmatricesWithAllOnes/DP1277.py)||testcase, do it again
|👍 1288|Medium  |[Remove Covered Intervals](https://leetcode.com/problems/remove-covered-intervals/)|2020/10/4|Array|[Naive-O(n)](Python3/Array/RemoveCoveredIntervals/Naive1288.py)||testcase, do it with other solution
|👍 1291|Medium  |[Sequential Digits](https://leetcode.com/problems/sequential-digits/)|2019/12/15|Math|[Naive-O(n)](Contest/LeetCodeWeeklyContest/WeeklyContest167/1291-SequentialDigits.py), [Recursive-O(nlogn)](Python3/Math/SequentialDigits/Recursive1291.py), [Naive2-O(n)](Python3/Math/SequentialDigits/Naive1291.py)|[Weekly Contest 167](Contest/README.md#Weekly-Contest-167)|testcase, Naive2 (generate sequence in order)
|👍 1293|Hard *  |[Shortest Path in a Grid with Obstacles Elimination](https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/)|2021/7/30|Graph|[BFS](Python3/Graph/ShortestPathInAGridWithObstaclesElimination/BFS1293.py)|Google Interview|do it again
|👍 1337|Easy    |[The K Weakest Rows in a Matrix](https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/)|2021/2/15|Array|[Naive-O(n)](Python3/Array/TheKWeakestRowsInAMatrix/Naive1337.py)||max heap + binary search
|   1338|Medium ▼|[Reduce Array Size to The Half](https://leetcode.com/problems/reduce-array-size-to-the-half/)|2021/7/6|Array|[Naive-O(n)](Python3/Array/ReduceArraySizeToTheHalf/Naive1338.py)||-
|   1342|Easy    |[Number of Steps to Reduce a Number to Zero](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/)|2020/9/20|Math|[Naive-O(n)](Python3/Math/NumberOfStepsToReduceANumberToZero/Naive1342.py), [Naive 2-O(n)](Python3/Math/NumberOfStepsToReduceANumberToZero/Naive2_1342.py)||(good for beginners)
|👍 1344|Medium  |[Angle Between Hands of a Clock](https://leetcode.com/problems/angle-between-hands-of-a-clock/)|2020/7/14|Math|[Naive-O(1)](Python3/Math/AngleBetweenHandsOfAClock/Naive1344.py)||-
|   1379|Medium ▼|[Find a Corresponding Node of a Binary Tree in a Clone of That Tree](https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/)|2021/1/2|Binary Tree|[Naive-O(n)](Python3/BinaryTree/FindACorrespondingNodeOfABinaryTreeInACloneOfThatTree/Naive1379.py)|[Note](Python3/BinaryTree/FindACorrespondingNodeOfABinaryTreeInACloneOfThatTree/Note1379.md)|testcase, iterative
|👍 1425|Hard  |[Constrained Subsequence Sum](https://leetcode.com/problems/constrained-subsequence-sum/)|TODO|Array||[Note](Python3/Array/ConstrainedSubsequenceSum/Note1425.md)|-
|👍 1462|Medium *|[Course Schedule IV](https://leetcode.com/problems/course-schedule-iv/)|TODO|Array|-|-|-
|👍 1475|Easy *  |[Final Prices With a Special Discount in a Shop](https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/)|2020/8/22|Array|[Naive-O(n^2)](Python3/Array/FinalPricesWithASpecialDiscountInAShop/Naive1475.py), [TwoPointer-O(n^2)](Python3/Array/FinalPricesWithASpecialDiscountInAShop/TwoPointer1475.py), [Stack-O(n^2)](Python3/Array/FinalPricesWithASpecialDiscountInAShop/Stack1475.py)||-
|👍 1480|Easy *  |[Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/)|2021/5/3|Array|[Naive-O(n)](Python3/Array/RunningSumOf1dArray/Naive1480.py), [In-Place-O(n)](Python3/Array/RunningSumOf1dArray/InPlace1480.py)||-
|👍 1539|Medium  |[Kth Missing Positive Number](https://leetcode.com/problems/kth-missing-positive-number/)|2021/1/6|Array|[Naive-O(n+k)](Python3/Array/KthMissingPositiveNumber/Naive1539.py)|-|better solution (log n)
|👍 1547|Hard    |[Minimum Cost to Cut a Stick](https://leetcode.com/problems/minimum-cost-to-cut-a-stick/)|2020/10/17|Array|[Top-Down DP-O(n^2)](Python3/Array/MinimumCostToCutAStick/TopDownDP1547.py)|FreeWheel 2020 OA, [Weekly Contest 201](Contest/README.md#Weekly-Contest-201)|testcase
|👍 1601|Hard    |[Maximum Number of Achievable Transfer Requests](https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/)|2020/9/28|Graph|[Naive-O(2^n)](Python3/Graph/MaximumNumberOfAchievableTransferRequests/Naive1601.py)||testcase
|👍 1640|Easy    |[Check Array Formation Through Concatenation](https://leetcode.com/problems/check-array-formation-through-concatenation/)|2021/1/1|Array|[DFS-O(n)](Contest/LeetCodeWeeklyContest/WeeklyContest213/1.py), [HashTable-O(n)](Python3/Array/CheckArrayFormationThroughConcatenation/HT1640.py)|[Weekly Contest 213](Contest/README.md#Weekly-Contest-213), [Note](Python3/Array/CheckArrayFormationThroughConcatenation/Note1640.md)|testcase, do it again
|👍 1861|Medium  |[Rotating the Box](https://leetcode.com/problems/rotating-the-box/)|TODO|AdHoc||Code Signal|-
|👍 1928|Hard *  |[Minimum Cost to Reach Destination in Time](https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/)|TODO|Graph||Google Interview|-
|👍 1971|Easy    |[Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/)|2022/12/19|Graph|[BFS-O(n)](Python3/Graph/FindIfPathExistsInGraph/BFS1971.py), [DFS-O(n)](Python3/Graph/FindIfPathExistsInGraph/DFS1971.py), [UnionFind-O(n)](Python3/Graph/FindIfPathExistsInGraph/UnionFind1971.py)||
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

Design        |  Date    |   Category   |  Implementation  |  Remark  | TODO |
--------------|----------|--------------|------------------|----------|------|
Circular Queue|2019/7/4  |Data Structure|[C++](Learn/Cpp/Queue/CircularQueue.cpp)|[Note](Notes/DataStructure/QueueStack.md#Circular-Queue), [Design Circular Queue](https://leetcode.com/problems/design-circular-queue/)|-
Min Stack     |2019/12/26|Data Structure|[C++](Learn/Cpp/Stack/MinStack.cpp)|[Min Stack](https://leetcode.com/problems/min-stack/)|-

## Notes

Data Structure

* [Queue and Stack](Notes/DataStructure/QueueStack.md)
* [Binary Tree](Notes/DataStructure/BinaryTree.md)
* [Priority Queue and Heap](Notes/DataStructure/PriorityQueue_Heap.md)
* [Trie (prefix tree)](Notes/DataStructure/Trie_PrefixTree.md)
* [Fenwick Tree / Binary Indexed Tree](Notes/DataStructure/FenwickTree_BinaryIndexedTree.md) (TODO)
* [Disjoint Set (Union-Find)](Notes/DataStructure/DisjointSet_UnionFind.md)

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

### Online Judgement / Assessment

* [LeetFree](https://www.leetfree.com/)
* [Codeforces](http://codeforces.com/)
* [Newcoder](https://www.nowcoder.com/) - Interview OA in China
  * [劍指Offer](https://www.nowcoder.com/ta/coding-interviews)
* [**CodeSignal**](https://app.codesignal.com/) - Intern Interview OA in America
* [HackerRank](https://www.hackerrank.com/) - Interview OA
* [binarysearch.io](https://binarysearch.io/)
* [Topcoder Top Technology Talent On-Demand](https://www.topcoder.com/)

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

### Course

* [Algorithms | Coursera](https://www.coursera.org/specializations/algorithms) (Paid)

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
> * [July LeetCoding Challenge](https://leetcode.com/explore/challenge/card/july-leetcoding-challenge)
>   * [🔥👕[LeetCode Polo Shirt] July LeetCoding Challenge! 👕🔥 - LeetCode Discuss](https://leetcode.com/discuss/general-discussion/655704/leetcode-polo-shirt-july-leetcoding-challenge)
>   * [Is Leetcode discontinuing with the Monthly challenges? - LeetCode Discuss](https://leetcode.com/discuss/explore/july-leetcoding-challenge/758118/is-leetcode-discontinuing-with-the-monthly-challenges)
> * [August LeetCoding Challenge](https://leetcode.com/explore/challenge/card/august-leetcoding-challenge)
>   * [🔥👕[LeetCode Polo Shirt] August LeetCoding Challenge! 👕🔥 - LeetCode Discuss](https://leetcode.com/discuss/general-discussion/655704/leetcode-polo-shirt-august-leetcoding-challenge)
> * [September LeetCoding Challenge](https://leetcode.com/explore/challenge/card/september-leetcoding-challenge)
>   * [🕔🚀 September LeetCoding Challenge and the Time Travel Ticket! 🚀🕤 - LeetCode Discuss](https://leetcode.com/discuss/general-discussion/655704/september-leetcoding-challenge-and-the-time-travel-ticket)
> * [October LeetCoding Challenge](https://leetcode.com/explore/featured/card/october-leetcoding-challenge/)
>   * [🕔🚀 October LeetCoding Challenge and the Time Travel Ticket! 🚀🕤 - LeetCode Discuss](https://leetcode.com/discuss/general-discussion/655704/october-leetcoding-challenge-and-the-time-travel-ticket)
> * [May LeetCoding Challenge 2021](https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021)
>   * [🏅 May LeetCoding Challenge and the Badge!🏅 - LeetCode Discuss](https://leetcode.com/discuss/general-discussion/655704)
> * [June LeetCode Challenge 2021](https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/)
> * [July LeetCode Challenge 2021](https://leetcode.com/explore/featured/card/july-leetcoding-challenge-2021/)

#### Top Interview Questions

* [Top Interview Questions - Easy Collection](https://leetcode.com/explore/interview/card/top-interview-questions-easy/)
* [Top Interview Questions - Medium Collection](https://leetcode.com/explore/interview/card/top-interview-questions-medium/)
* [Top Interview Questions - Hard Collection](https://leetcode.com/explore/interview/card/top-interview-questions-hard/)

> LeetCode Premium Top Question List:
>
> TOP GOOGLE QUESTION: `[1, 85, 127, 224, 315, 329, 346, 359, 394, 444, 489, 528, 552, 560, 562, 642, 652, 659, 690, 715, 722, 727, 729, 752, 753, 767, 809, 833, 843, 844, 846, 900, 946, 951, 1031, 1048, 1060, 1110, 1138, 1153, 1231, 1293, 1296, 1345, 1376, 1423, 1438, 1463, 1477, 1548]`
> TOP MICROSOFT QUESTION: `[1, 2, 5, 8, 15, 17, 23, 25, 33, 34, 41, 42, 45, 46, 49, 53, 54, 55, 79, 85, 88, 98, 102, 103, 105, 124, 127, 138, 140, 146, 151, 155, 160, 200, 210, 212, 232, 236, 240, 273, 287, 295, 297, 340, 428, 445, 468, 545, 767, 1239]`
> TOP FACEBOOK QUESTION: `[23, 34, 56, 65, 67, 88, 124, 125, 133, 140, 158, 173, 199, 211, 215, 227, 238, 249, 269, 270, 273, 278, 282, 297, 301, 311, 339, 340, 398, 415, 438, 523, 528, 543, 560, 621, 636, 670, 680, 689, 721, 785, 938, 953, 973, 986, 987, 1026, 1249, 1428]`
> TOP AMAZON QUESTION: `[1, 5, 21, 23, 42, 49, 56, 126, 127, 138, 139, 140, 146, 185, 200, 210, 212, 227, 239, 253, 269, 273, 295, 297, 348, 353, 380, 403, 437, 460, 472, 588, 682, 692, 721, 763, 815, 819, 863, 901, 937, 957, 973, 994, 1091, 1120, 1152, 1167, 1192, 1429]`

### Detail Solutions

* C++
  * [《LeetCode題解》](https://legacy.gitbook.com/book/siddontang/leetcode-solution/details)
  * [wisdompeak/LeetCode: This repository contains the solutions and explanations to the algorithm problems on LeetCode. Only medium or above are included. All are written in C++/Python and implemented by myself. The problems attempted multiple times are labelled with hyperlinks.](https://github.com/wisdompeak/LeetCode)
  * [Huifeng Guan - YouTube](https://www.youtube.com/user/wisdompeak)
* JavaScript
  * [《初學者練習 - LeetCode with Javascript》](https://legacy.gitbook.com/book/skyyen999/-leetcode-with-javascript/details)
  * [azl397985856/leetcode: LeetCode Solutions: A Record of My Problem Solving Journey.](https://github.com/azl397985856/leetcode)
* Go
  * [LeetCode-in-Go](https://github.com/aQuaYi/LeetCode-in-Go)
* Mixed
  * [qiyuangong/leetcode: Python & JAVA Solutions for Leetcode](https://github.com/qiyuangong/leetcode)
  * [haoel/leetcode: LeetCode Problems' Solutions](https://github.com/haoel/leetcode)
  * [grandyang/leetcode: Provide all my solutions and explanations in Chinese for all the Leetcode coding problems.](https://github.com/grandyang/leetcode)

### Study Group

* Cruel Study Group
  * [残酷刷题群](http://board.cruelcoding.com/) ([graduates](http://board.cruelcoding.com/graduates.html))
    * [wisdompeak/lc-score-board: A smart application that automatically updates weekly contest score board for my Wechat coding group](https://github.com/wisdompeak/lc-score-board)
    * [残酷群2021年会 - Google 簡報](https://docs.google.com/presentation/d/1wIYIszpPuKEKTMAQXyb4lllhXApNWfa9J53lYK5gHmM/edit#slide=id.g10a25ba6884_0_86)
    * [LeetCode打卡记录 - Google 試算表](https://docs.google.com/spreadsheets/d/1kBGyRsSdbGDu7DzjQcC-UkZjZERdrP8-_QyVGXHSrB8/edit#gid=0)
  * [在残酷刷题群里是什么样的体验？ - 知乎](https://www.zhihu.com/question/457519650)
    * [Pool的残酷故事2021](https://roasted-ermine-595.notion.site/Pool-2021-60dd832e786d41d88a01b31b70a5be5f)

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
* VSCode debug
  * [Testing Python in Visual Studio Code](https://code.visualstudio.com/docs/python/testing#_debug-tests)
  * [Python Test Explorer for Visual Studio Code - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=LittleFoxTeam.vscode-python-test-adapter)

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

VSCode ignore formatting on file

* [X] [visual studio code - How to exclude file extensions and languages from "format on save" in VSCode? - Stack Overflow](https://stackoverflow.com/questions/44831313/how-to-exclude-file-extensions-and-languages-from-format-on-save-in-vscode)

```txt
 ! [new branch]      master     -> origin/master  (unable to update local ref)
warning: url has no scheme: 
fatal: credential url cannot be parsed:
error: update_ref failed for ref 'refs/remotes/origin/master': cannot lock ref 'refs/remotes/origin/master': unable to resolve reference 'refs/remotes/origin/master': reference broken
```

* [command line interface - Git error on git pull (unable to update local ref) - Stack Overflow](https://stackoverflow.com/questions/10068640/git-error-on-git-pull-unable-to-update-local-ref)
* [Error: Cannot lock ref 'refs/remotes/origin/master'](https://github.com/desktop/desktop/issues/6121#issuecomment-437145964)
