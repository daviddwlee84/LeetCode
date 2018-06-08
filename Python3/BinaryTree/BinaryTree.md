# Binary Tree

## Introduction

A **tree** is a frequently-used data structure to simulate a hierarchical tree structure.

Each node of the tree will have a root value and a list of references to other nodes which are called child nodes. From graph view, a tree can also be defined as a directed acyclic graph which has **N nodes** and **N-1 edges**.

A **Binary Tree** is one of the most typical tree structure. As the name suggests, a binary tree is a tree data structure in which each node has **at most two children**, which are referred to as the left child and the right child.

By completing this card, you will be able to:

1. Understand the concept of a **tree** and a **binary tree**;
2. Be familiar with different **traversal** methods;
3. Use **recursion** to solve binary-tree-related problems;

## Traverse a Tree

### Pre-order Traversal

Pre-order traversal is to visit the root first. Then traverse the left subtree. Finally, traverse the right subtree.

### In-order Traversal

In-order traversal is to traverse the left subtree first. Then visit the root. Finally, traverse the right subtree.

### Post-order Traversal

Post-order traversal is to traverse the left subtree first. Then traverse the right subtree. Finally, visit the root.

* Deletion Process
* Mathematical Expression - handle the expression using a stack

### Level-order Traversal

Level-order traversal is to traverse the tree level by level.

Breadth-First Search is an algorithm to traverse or search in data structures like a tree or a graph. The algorithm starts with a root node and visit the node itself first. Then traverse its neighbors, traverse its second level neighbors, traverse its third level neighbors, so on and so forth.

When we do breadth-first search in a tree, the order of the nodes we visited is in level order.

Typically, we use a queue to help us to do BFS

## Solve Tree Problems Recursively

Recursion is one of the most powerful and frequent used methods for solving tree related problems.

A tree can be defined recursively as a node(the root node), which includes a value and a list of references to other nodes.
Recursion is one of the nature features of a tree. Therefore, many tree problems can be solved recursively.
For each recursion level, we can only focus on the problem within one single node and call the function recursively to solve its children.

### "Top-down" Solution

"Top-down" means that in each recursion level, we will visit the node first to come up with some values, and pass these values to its children when calling the function recursively.
So the "top-down" solution can be considered as kind of **preorder** traversal.

```
top_down(root, params)

1. return specific value for null node
2. update the answer if needed                      // anwer <-- params
3. left_ans = top_down(root.left, left_params)      // left_params <-- root.val, params
4. right_ans = top_down(root.right, right_params)   // right_params <-- root.val, params 
5. return the answer if needed                      // answer <-- left_ans, right_ans
```

For instance, consider this problem: given a binary tree, find its maximum depth.

We know that the depth of the root node is 1. For each node, if we know the depth of the node, we will know the depth of its children. Therefore, if we pass the depth of the node as a parameter when calling the function recursively, all the nodes know the depth of themselves. And for leaf nodes, we can use the depth to update the final answer.

```
maximum_depth(root, depth)

1. return if root is null
2. if root is a leaf node:
3.      answer = max(answer, depth)         // update the answer if needed
4. maximum_depth(root.left, depth + 1)      // call the function recursively for left child
5. maximum_depth(root.right, depth + 1)     // call the function recursively for right child
```

C++ Code

```cpp
int answer;		       // don't forget to initialize answer before call maximum_depth
void maximum_depth(TreeNode* root, int depth) {
    if (!root) {
        return;
    }
    if (!root->left && !root->right) {
        answer = max(answer, depth);
    }
    maximum_depth(root->left, depth + 1);
    maximum_depth(root->right, depth + 1);
}
```

### "Bottom-up" Solution

"Bottom-up" is another recursion solution. In each recursion level, we will firstly call the functions recursively for all the children nodes and then come up with the answer according to the return values and the value of the root node itself.
This process can be regarded as kind of **postorder** traversal.

```
bottom_up(root)

1. return specific value for null node
2. left_ans = bottom_up(root.left)          // call function recursively for left child
3. right_ans = bottom_up(root.right)        // call function recursively for right child
4. return answers                           // answer <-- left_ans, right_ans, root.val
```

Let's go on discussing the question about maximum depth but using a different way of thinking: for a single node of the tree, what will be the maximum depth x of the subtree rooted at itself?

If we know the maximum depth l of the subtree rooted at its left child and the maximum depth r of the subtree rooted at its right child, can we answer the previous question? Of course yes, we can choose the maximum between them and plus 1 to get the maximum depth of the subtree rooted at the selected node. That is x = max(l, r) + 1.

It means that for each node, we can get the answer after solving the problem of its children. Therefore, we can solve this problem using a "bottom-up" solution.

```
maximum_depth(root)

1. return 0 if root is null                 // return 0 for null node
2. left_depth = maximum_depth(root.left)
3. right_depth = maximum_depth(root.right)
4. return max(left_depth, right_depth) + 1  // return depth of the subtree rooted at root
```

C++

```cpp
int maximum_depth(TreeNode* root) {
	if (!root) {
		return 0;                                 // return 0 for null node
	}
	int left_depth = maximum_depth(root->left);	
	int right_depth = maximum_depth(root->right);
	return max(left_depth, right_depth) + 1;	  // return depth of the subtree rooted at root
}
```

### Conclusion

When you meet a tree problem, ask yourself two questions: can you determine some parameters to help the node know the answer of itself? Can you use these parameters and the value of the node itself to determine what should be the parameters parsing to its children? If the answers are both yes, try to solve this problem using a "top-down" recursion solution.

Or you can think the problem in this way: for a node in a tree, if you know the answer of its children, can you calculate the answer of the node? If the answer is yes, solving the problem recursively from bottom up might be a good way.




## Summary

* Depth-First Search
    * Pre-order Traversal
    * In-order Traversal (change output order)
    * Post-order Traversal (change output order)

* Breath-First Search
    * Level-order Traversal

## LeetCode Remark

### [Frequently Asked Questions](https://leetcode.com/faq/#binary-tree)

Testcase: the serialized format of a binary tree using level order traversal

## Other Resources

[Binary Tree](http://www.csie.ntnu.edu.tw/~u91029/BinaryTree.html)