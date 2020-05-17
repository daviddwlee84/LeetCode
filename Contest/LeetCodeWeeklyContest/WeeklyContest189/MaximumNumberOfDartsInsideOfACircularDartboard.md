# 1453. Maximum Number of Darts Inside of a Circular Dartboard

## Description

You have a very large square wall and a circular dartboard placed on the wall. You have been challenged to throw darts into the board blindfolded. Darts thrown at the wall are represented as an array of `points` on a 2D plane.

Return the maximum number of points that are within or lie on **any** circular dartboard of radius `r`.

**Example 1**:

![ex1](https://assets.leetcode.com/uploads/2020/04/29/sample_1_1806.png)

```txt
Input: points = [[-2,0],[2,0],[0,2],[0,-2]], r = 2
Output: 4
Explanation: Circle dartboard with center in (0,0) and radius = 2 contain all points.
```

**Example 2**:

![ex2](https://assets.leetcode.com/uploads/2020/04/29/sample_2_1806.png)

```txt
Input: points = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5
Output: 5
Explanation: Circle dartboard with center in (0,4) and radius = 5 contain all points except the point (7,8).
```

**Example 3**:

```txt
Input: points = [[-2,0],[2,0],[0,2],[0,-2]], r = 1
Output: 1
```

**Example 4**:

```txt
Input: points = [[1,2],[3,5],[1,-1],[2,3],[4,1],[1,3]], r = 2
Output: 4
```

**Constraints**:

* `1 <= points.length <= 100`
* `points[i].length == 2`
* `-10^4 <= points[i][0], points[i][1] <= 10^4`
* `1 <= r <= 5000`

> Hint:
>
> * If there is an optimal solution, you can always move the circle so that two points lie on the boundary of the circle.
> * When the radius is fixed, you can find either 0 or 1 or 2 circles that pass two given points at the same time.
> * Loop for each pair of points and find the center of the circle, after that count the number of points inside the circle.

## Solution

## Others' Solution

* [Simple Python O(n3) Solution with picture - LeetCode Discuss](https://leetcode.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/discuss/636345/Simple-Python-O%28n3%29-Solution-with-picture)
* [POJ 1981 - LeetCode Discuss](https://leetcode.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/discuss/636372/POJ-1981)
* [[cpp] O(N^3) solution with pictures. - LeetCode Discuss](https://leetcode.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/discuss/636332/cpp-O%28N3%29-solution-with-pictures.)

## Resources

Circle / Angular Sweep

* [POJ 1981 -- Circle and Points](http://poj.org/problem?id=1981)
* [c++ - Algorithm to cover maximal number of points with one circle of given radius - Stack Overflow](https://stackoverflow.com/questions/3229459/algorithm-to-cover-maximal-number-of-points-with-one-circle-of-given-radius/3229582#3229582)
* [Angular Sweep (Maximum points that can be enclosed in a circle of given radius) - GeeksforGeeks](https://www.geeksforgeeks.org/angular-sweep-maximum-points-can-enclosed-circle-given-radius/)

Python Combination

* [python - How to get all possible combinations of a list’s elements? - Stack Overflow](https://stackoverflow.com/questions/464864/how-to-get-all-possible-combinations-of-a-list-s-elements)
