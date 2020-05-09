# [Binary Search](https://leetcode.com/explore/learn/card/binary-search)

## Overview

### What is Binary Search?

Binary Search is one of the most fundamental and useful algorithms in Computer Science. It describes the process of searching for a specific value in an ordered collection.

> Terminology used in Binary Search:
>
> * Target - the value that you are searching for
> * Index - the current location that you are searching
> * Left, Right - the indicies from which we use to maintain our search Space
> * Mid - the index that we use to apply a condition to determine if we should search left or right

## Background

### How does it work?

In its simplest form, Binary Search operates on a contiguous sequence with a specified left and right index. This is called the Search Space. Binary Search maintains the left, right, and middle indicies of the search space and compares the search target or applies the search condition to the middle value of the collection; if the condition is unsatisfied or values unequal, the half in which the target cannot lie is eliminated and the search continues on the remaining half until it is successful. If the search ends with an empty half, the condition cannot be fulfilled and target is not found.

**Note**:

Binary Search can take many alternate forms and might not always be as straight forward as searching for a specific value. Sometimes you will have to apply a specific condition or rule to determine which side (left or right) to search next.

### Identification and Template Introduction

#### How do we identify Binary Search?

As mentioned in earlier, Binary Search is an algorithm that divides the search space in 2 after every comparison. Binary Search should be considered every time you need to search for an index or element in a collection. If the collection is unordered, we can always sort it first before applying Binary Search.

#### 3 Parts of a Successful Binary Search

Binary Search is generally composed of 3 main sections:

1. Pre-processing - Sort if collection is unsorted.
2. Binary Search - Using a loop or recursion to divide search space in half after each comparison.
3. Post-processing - Determine viable candidates in the remaining space.

#### 3 Templates for Binary Search

When we first learned Binary Search, we might struggle. We might study hundreds of Binary Search problems online and each time we looked at a developer's code, it seemed to be implemented slightly differently. Although each implementation divided the problem space in 1/2 at each step, one had numerous questions:

* Why was it implemented slightly differently?
* What was the developer thinking?
* Which way was easier?
* Which way is better?

After many failed attempts and lots of hair-pulling, we found 3 main templates for Binary Search. To prevent hair-pulling and to make it easier for new developers to learn and understand, we have provided them in the next chapter.

## Template I

## Template II

## Template III

## Resources

* [Google AI Blog: Extra, Extra - Read All About It: Nearly All Binary Searches and Mergesorts are Broken](https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html)
