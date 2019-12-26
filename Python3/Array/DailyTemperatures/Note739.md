# 739. Daily Temperatures

## Description

Given a list of daily temperatures `T`, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put `0` instead.

For example, given the list of temperatures `T = [73, 74, 75, 71, 69, 72, 76, 73]`, your output should be `[1, 1, 4, 2, 1, 1, 0, 0]`.

**Note**: The length of `temperatures` will be in the range `[1, 30000]`. Each temperature will be an integer in the range `[30, 100]`.

## Solution

### Stack + Hash Table

> not exactly a stack

1. Pop from the end of `T` and record its `value: position` in the hash table
2. See if any number is larger than itself and is already in the hash table

### Stack

1. Push current index into stack if current temperature is higher
2. When find a higher one, pop all lower temperatures
