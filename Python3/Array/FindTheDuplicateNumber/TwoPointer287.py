from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/find-the-duplicate-number/discuss/704693/Python-Two-pointers-Linked-List-Cycle-O(n)-explained

        consider list as linked list, where i is connected with nums[i]
        try to find the loop

        This solution work based on the following condition:
        "Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive)"

        and reduce the problem to Linked List Cycle II (https://leetcode.com/problems/linked-list-cycle-ii/solution/)


        Floyd's Tortoise and Hare (Cycle Detection)
        https://leetcode.com/problems/find-the-duplicate-number/solution/
        """
        slow, fast = nums[0], nums[0]

        while True:
            # similar with node = node.next
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast:
                break

        # now fast pointer gains slow pointer

        # move slow (one of them) to the start
        slow = nums[0]

        # run with the same speed until they collide
        while slow != fast:
            slow, fast = nums[slow], nums[fast]

        return slow

# Runtime: 84 ms, faster than 30.81% of Python3 online submissions for Find the Duplicate Number.
# Memory Usage: 16.4 MB, less than 23.69% of Python3 online submissions for Find the Duplicate Number.
