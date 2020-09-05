from typing import List
from collections import Counter


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        """
        https://leetcode.com/problems/word-subsets/discuss/175854/C%2B%2BJavaPython-Straight-Forward
        """

        count = Counter()

        # Get the max count for each char
        for b in B:
            count |= Counter(b)

        # Get the min count for each a and entire b, if it is still the same => all a is not less than b
        return [a for a in A if (Counter(a) & count) == count]

# Runtime: 1116 ms, faster than 58.85% of Python3 online submissions for Word Subsets.
# Memory Usage: 17.6 MB, less than 44.26% of Python3 online submissions for Word Subsets.

# https://docs.python.org/3.8/library/collections.html#collections.Counter
#
# c & d                       # intersection:  min(c[x], d[x]) 
# Counter({'a': 1, 'b': 1})
# c | d                       # union:  max(c[x], d[x])
# Counter({'a': 3, 'b': 2})


if __name__ == "__main__":
    A = ["amazon", "apple", "facebook", "google", "leetcode"]
    B = ["e", "o", "eee"]
    count = Counter()
    for b in B:
        count |= Counter(b)
    print(count)

    for a in A:
        print(a, Counter(a) & count, count)
