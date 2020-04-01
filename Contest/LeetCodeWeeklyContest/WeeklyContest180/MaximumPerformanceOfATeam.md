# 1383. Maximum Performance of a Team

## Description

There are `n` engineers numbered from 1 to `n` and two arrays: `speed` and `efficiency`, where `speed[i]` and `efficiency[i]` represent the speed and efficiency for the i-th engineer respectively. *Return the maximum **performance** of a team composed of at most `k` engineers, since the answer can be a huge number, return this modulo 10^9 + 7*.

The **performance** of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers.

**Example 1**:

```txt
Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
Output: 60
Explanation: 
We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7). That is, performance = (10 + 5) * min(4, 7) = 60.
```

**Example 2**:

```txt
Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
Output: 68
Explanation:
This is the same example as the first but k = 3. We can select engineer 1, engineer 2 and engineer 5 to get the maximum performance of the team. That is, performance = (2 + 10 + 5) * min(5, 4, 7) = 68.
```

**Example 3**:

```txt
Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
Output: 72
```

**Constraints**:

* `1 <= n <= 10^5`
* `speed.length == n`
* `efficiency.length == n`
* `1 <= speed[i] <= 10^5`
* `1 <= efficiency[i] <= 10^8`
* `1 <= k <= n`

## Soluiton

### Greedy with Priority Queue

## Others' Solution

* [[Java/C++/Python] Priority Queue - LeetCode Discuss](https://leetcode.com/problems/maximum-performance-of-a-team/discuss/539687/JavaC%2B%2BPython-Priority-Queue)

> Binary Insert
>
> * [bisect — Array bisection algorithm — Python 3.8.2 documentation](https://docs.python.org/3.8/library/bisect.html)

```py
    def maxPerformance(self, n, speed, efficiency, k):
        h = []
        res = sSum = 0
        for e, s in sorted(zip(efficiency, speed), reverse=1):
            bisect.insort(h, -s)
            sSum += s
            if len(h) > k:
                sSum += h.pop()
            res = max(res, sSum * e)
        return res % (10**9+7)
```

## Resources

* [How To identify between DP and Greedy ??? - LeetCode Discuss](https://leetcode.com/problems/maximum-performance-of-a-team/discuss/539815/How-To-identify-between-DP-and-Greedy)
