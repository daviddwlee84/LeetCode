# Python Tricks and Useful Libraries

## Memory: for turning an recursive solution into a Top-down DP solution

### `functools.lru_cache`

```py
from functools import lru_cache

class Solution:
    def func(self, n: int) -> int:
        @lru_cache(None)
        def dp(n):
            # do some calculation to get `ans`
            return ans
        return dp(n)
```

> Decorate a function
>
> ```py
> @deco
> def f(x):
>     pass
> ```
>
> make `f` become `deco(f)`

### Reuse memory through cases

```py
class Solution:
    memo = {}  # THIS CAN REUSE MEMO THROUGH THE TESTCASES!!!

    def func(self, n: int) -> int:
        def dp(n):
            if n not in Solution.memo:
                # do some calculation to get `ans` ...
                Solution.memo[n] = ans
            return Solution.memo[n]

        return dp(n)
```

## Permutation / Combination

> TODO

`itertools.permutations`

`itertools.combinations`

## Dictionary

...

## Binary Search

`bisect.py`

...

## Sorting

...
