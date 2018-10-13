# 3Sum

## Description

Given an array `nums` of n integers, are there elements a, b, c in `nums` such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

**Note**:

The solution set must not contain duplicate triplets.

**Example**:
```
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```

## Solution

### Brute Force

* Time Complexity: O(n⁴)

* Use 3 layer of loop to find every combination: O(n³)
    * Prevent the duplicates: O(n)

### Two Pointer

* Time Complexity: O(n²)

* Sort the array to reduce the time complexity of avoiding duplicate numbers
* Use two pointer and calculate the sum of the current index by `0 - nums[i]` then see if match
* Prevent duplicate number by forward the pointer since the array is sorted

[Java Solution](https://leetcode.com/problems/3sum/discuss/7380/Concise-O(N2)-Java-solution)
[Java Solution with chinese explanation](https://leetcode.windliang.cc/leetCode-15-3Sum.html)

```python
def threeSum(self, nums):
    res = []
    nums.sort()
    for i in xrange(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1; r -= 1
    return res
```

```cpp
vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        if(nums.size()<=2)return result;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size() - 2; i++) {
            int a = nums[i];
            if(a > 0) break;
            if (i > 0 && a == nums[i - 1]) continue;
            for (long j = i + 1, k = nums.size() - 1; j < k;) {
                int b = nums[j];
                int c = nums[k];
                int value = a + b + c;
                if (value == 0) {
                    result.push_back(vector<int>({a, b, c}));
                    while (j<k && b == nums[++j]);
                    while (j < k &&c == nums[--k]);
                } else if (value > 0) {
                    k--;
                } else {
                    j++;
                }
            }
        }
        return result;
    }
```

### Others

```python
class Solution:
    def threeSum(self, nums):
        result = []
        #Create Dictionary
        lookup = dict()
        for ele in nums:
            if ele in lookup:
                lookup[ele]+=1
            else:
                lookup[ele] = 1

        #See if there are 3 zeros present
        if 0 in lookup and lookup[0] > 2:
            ans = [0,0,0]
            result.append(ans)
        #Iterate positive and negative items
        pos = [pos for pos in lookup if pos > 0]
        neg = [neg for neg in lookup if neg < 0]
        #Logic : for every positive iteger, loop over every negative integer
        #and try to find some value such that p+n+i = 0, hence we need to find i = -p-n
        for p in pos:
            for n in neg:
                i = -p-n
                #Not found
                if i not in lookup:
                    continue
                #Found i : 0
                if i == 0 and lookup[i] > 0:
                    result.append([n,0,p])
                elif i == p and lookup[p] > 1:
                    result.append([n,p,p])
                elif i == n and lookup[n] > 1:
                    result.append([n,n,p])
                elif i > p:
                    result.append([n,p,i])
                elif i < n:
                    result.append([i,n,p])
        return result
```