from typing import List
from collections import Counter
import random


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        https://leetcode.com/problems/top-k-frequent-elements/solution/

        Hoare's selection algorithm (Quickselect)

        * kind of similar with Quicksort
        * used to solve the problems "find kth something"
        """
        count = Counter(nums)
        unique = list(count.keys())

        def partition(left: int, right: int, pivot_index: int) -> int:
            """
            Hoare's Partition
            """
            pivot_frequency = count[unique[pivot_index]]
            # 1. move (swap) pivot to the end
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]

            # 2. move all less frequent elements to the left
            store_index = left
            for i in range(left, right):
                if count[unique[i]] < pivot_frequency:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            unique[right], unique[store_index] = unique[store_index], unique[right]

            return store_index

        def quickselect(left: int, right: int, k_smallest: int) -> None:
            """
            Sort a list within left..right till kth less frequent element
            takes its place
            """

            # base case: the list contains only one element
            if left == right:
                return

            # select a random pivot_index
            pivot_index = random.randint(left, right)

            # find the pivot position in a sorted list
            pivot_index = partition(left, right, pivot_index)

            # if the pivot is in its final sorted partition
            if k_smallest == pivot_index:
                return

            # go left (larger side)
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index - 1, k_smallest)

            # go right (larger side)
            else:
                quickselect(pivot_index + 1, right, k_smallest)

        n = len(unique)
        # kth top frequent element is (n - k)th less frequent.
        # Do a partial sort: from less frequent to the most frequent, till
        # (n - k)th less frequent element takes its place (n - k) in a sorted array.
        # All element on the left are less frequent.
        # All the elements on the right are more frequent.
        quickselect(0, n - 1, n - k)
        # Return top k frequent elements
        return unique[n - k:]

# Runtime: 136 ms, faster than 33.69% of Python3 online submissions for Top K Frequent Elements.
# Memory Usage: 18.3 MB, less than 44.82% of Python3 online submissions for Top K Frequent Elements.
