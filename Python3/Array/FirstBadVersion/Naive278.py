# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

def isBadVersion(version) -> bool:
    pass

class Solution:
    def firstBadVersion(self, n):
        """
        Binary Search

        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        
        while left <= right:
            # In other language, we should use left + (right - left) / 2 to prevent from TLE (integer overflow)
            # start = 2147483647
            # end = 2147483647
            # mid using (start + end)/2 = -1
            # mid using start + (end - start)/2 = 2147483647

            mid = (left + right) // 2

            if isBadVersion(mid):
                if not isBadVersion(mid - 1) or mid < 1:
                    # right at the intersection of good and bad
                    return mid
                else:
                    right = mid - 1
            else:
                left = mid + 1
