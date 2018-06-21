# Dynamic Programming

## Note

### Tips of finding DP solution

It's hard to figure out DP solution at the first glance.

1. Find Recursive solution first
    * Base Case
    * Recursive Case
2. Use recursive solution to derive DP formula
    * Recursive relationship - relationship between status i and any other previous status
3. Transform to DP form
    * Use a table/array/... to store the status (dp[i] for the ith status)
    * Base Case => Initialize dp[]
    * Recursive Case => Calculate dp[i]
4. Optimize space complexity
    * Consider what information dp[i] is depending on.
    * Only keep the necessary information and get rid of other sub-result

## Resources

[Dynamic Programming – From Novice to Advanced](https://www.topcoder.com/community/data-science/data-science-tutorials/dynamic-programming-from-novice-to-advanced/)