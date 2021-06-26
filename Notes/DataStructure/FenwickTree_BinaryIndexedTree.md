# Fenwick Tree / Binary Indexed Tree

## Purpose

1. Search prefix sum `query(i)`: return the prefix sum of `[0 ... i - 1]`
   * Time complexity: O(log n)
2. Update single node `update(i, v)`: update the position `i` with value `v`
   * Time complexity: O(log n)

## Template

```py
class FenwickTree:
    def __init__(self, n):
        self.size = n
        self.tree = [0 for _ in range(n + 1)]

    def __lowbit(self, index: int):
        """
        To get the "lowest" bit with 1 (and also the following 0)
        index is a positive number
        `-index` is equivalent to `(~index + 1)`
        """
        return index & (-index)

    def update(self, index: int, delta: int):
        """
        Update a single node: plus `delta` for the position of `index`
        """
        while index <= self.size:
            self.tree[index] += delta
            index += self.__lowbit(index)

    def query(self, index: int):
        """
        Search within an interval: how many number less equal than `index`
        Query is about the "prefix sum"
        """
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= self.__lowbit(index)
        return res
```

## Resources

* [花花酱 Fenwick Tree / Binary Indexed Tree - 刷题找工作 SP3 - YouTube](https://www.youtube.com/watch?v=WbafSgetDDk)
* [**树状数组（Java 、Python） - 计算右侧小于当前元素的个数 - 力扣（LeetCode）**](https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/solution/shu-zhuang-shu-zu-by-liweiwei1419/)
* [树状数组（Binary Indexed Tree），看这一篇就够了_正西风落叶下长安-CSDN博客](https://blog.csdn.net/Yaokai_AssultMaster/article/details/79492190)
* [樹狀陣列 - 維基百科，自由的百科全書](https://zh.wikipedia.org/wiki/%E6%A0%91%E7%8A%B6%E6%95%B0%E7%BB%84)

### Related Task

* [Count of Smaller Numbers After Self - LeetCode](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)
  * [计算右侧小于当前元素的个数 - 计算右侧小于当前元素的个数 - 力扣（LeetCode）](https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/solution/ji-suan-you-ce-xiao-yu-dang-qian-yuan-su-de-ge-s-7/)
* [剑指 Offer 51. 数组中的逆序对 - 力扣（LeetCode）](https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/)
