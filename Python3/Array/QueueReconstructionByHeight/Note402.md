# 406. Queue Reconstruction by Height

## Description

Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers `(h, k)`, where `h` is the height of the person and `k` is the number of people in front of this person who have a height greater than or equal to `h`. Write an algorithm to reconstruct the queue.

**Note**:

The number of people is less than 1,100.

**Example**:

```txt
Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
```

Hint

1. What can you say about the position of the shortest person? If the position of the shortest person is *i*, how many people would be in front of the shortest person?
2. Once you fix the position of the shortest person, what can you say about the position of the second shortest person?

## Solution

## Others' Solution

* [[Python] Tired of inserting from the tallest? Here is how to insert from the lowest - LeetCode Discuss](https://leetcode.com/problems/queue-reconstruction-by-height/discuss/673016/Python-Tired-of-inserting-from-the-tallest-Here-is-how-to-insert-from-the-lowest)
* [Queue Reconstruction by Height · Google Interview](https://evelynn.gitbooks.io/google-interview/queue-reconstruction-by-height.html)

```py
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if not people: return []

        # obtain everyone's info
        # key=height, value=k-value, index in original array
        peopledct, height, res = {}, [], []

        for i in range(len(people)):
            p = people[i]
            if p[0] in peopledct:
                peopledct[p[0]] += (p[1], i),
            else:
                peopledct[p[0]] = [(p[1], i)]
                height += p[0],

        height.sort()      # here are different heights we have

        # sort from the tallest group
        for h in height[::-1]:
            peopledct[h].sort()
            for p in peopledct[h]:
                res.insert(p[0], people[p[1]])

        return res
```
