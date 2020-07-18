from typing import List
from collections import Counter, defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        https://leetcode.com/problems/top-k-frequent-elements/discuss/81697/Python-O(n)-solution-without-sort-without-heap-without-quickselect

        Kind of reverse hash table
        Actually equivalent to Bucket Sort
        """
        count = Counter(nums)
        frequency = defaultdict(list)
        for num, cnt in count.items():
            frequency[cnt].append(num)

        result = []
        for times in reversed(range(1, len(nums) + 1)):
            result.extend(frequency[times])
            if len(result) >= k:
                # It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
                # i.e. there will always exist len(result) == k
                break

        return result

# Runtime: 112 ms, faster than 56.68% of Python3 online submissions for Top K Frequent Elements.
# Memory Usage: 23.9 MB, less than 5.05% of Python3 online submissions for Top K Frequent Elements.


# Pure Counter
#
#from collections import Counter
#
# class Solution:
#    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#        most_common = Counter(nums).most_common()
#        fin = []
#        for l in range(0,k):
#            fin.append(most_common[l][0])
#
#        return fin
