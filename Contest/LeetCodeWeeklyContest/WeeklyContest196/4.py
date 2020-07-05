class Solution:
    def minInteger(self, num: str, k: int) -> str:
        """
        https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/discuss/720127/Python-bytedance-interview-question
        """
        # convert into int
        num = [*map(int, num)]

        if k > (len(num) ** 2) // 2:
            # we have enough k to get the global smallest number by sorting
            return ''.join(map(str, sorted(num)))

        answer = []
        queue = [(val, i) for i, val in enumerate(num)]
        while k and queue:
            # move the minimum number in the possible reach range to the very front
            # (sorted by the value, then its index (to use the minimum of k if they are the same number))
            index, (val, _) = min(enumerate(queue[:k+1]), key=lambda p: p[1])
            k -= index
            del queue[index]
            answer.append(val)

        # extend the rest of the unchange number
        answer.extend([val for val, _ in queue])
        return ''.join(map(str, answer))


# Runtime: 5412 ms, faster than 11.11% of Python3 online submissions for Minimum Possible Integer After at Most K Adjacent Swaps On Digits.
# Memory Usage: 18.7 MB, less than 100.00% of Python3 online submissions for Minimum Possible Integer After at Most K Adjacent Swaps On Digits.
