from typing import List
from collections import defaultdict


class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        """
        uwi's Solution

        (This won't work in Python: TLE)
        """
        nums1_val = [False] * 10000001
        nums2_val = [False] * 10000001

        for num in nums1:
            nums1_val[num] = True
        for num in nums2:
            nums2_val[num] = True

        dp_nums1 = 0
        dp_nums2 = 0

        for num in range(1, 10000001):
            if nums1_val[num]:
                dp_nums1 += num
            if nums2_val[num]:
                dp_nums2 += num

            if nums1_val[num] and nums2_val[num]:
                dp_nums1 = dp_nums2 = max(dp_nums1, dp_nums2)

        return max(dp_nums1, dp_nums2) % 1000000007

# TLE
#
# [5,8,14,19,25,26,34]
# [8,10,18]


# 	class Solution {
# 	    public int maxSum(int[] nums1, int[] nums2) {
# 	        int m = 10000001;
# 	        boolean[] a = new boolean[m];
# 	        boolean[] b = new boolean[m];
# 	        for(int v : nums1)a[v] = true;
# 	        for(int v : nums2)b[v] = true;
# 	        long da = 0, db = 0;
# 	        for(int i = 1;i < m;i++){
# 	        	if(a[i])da += i;
# 	        	if(b[i])db += i;
# 	        	if(a[i] && b[i]){
# 	        		da = Math.max(da, db);
# 	        		db = da;
# 	        	}
# 	        }
# 	        int ans = (int)(Math.max(da, db)%1000000007);
# 	        return ans;
# 	    }
# 	}
