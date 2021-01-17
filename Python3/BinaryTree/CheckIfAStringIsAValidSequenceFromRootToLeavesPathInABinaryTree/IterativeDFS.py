# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from ..TreeNodeModule import TreeNode
from typing import List


class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        """
        find all path to leaf and check if it is match arr,
        if found then return immediately
        """
        # inorder
        stack = []
        curr = root

        while curr is not None or stack:
            # reach the left most node of the curr node
            while curr is not None:
                # place pointer to a tree node on the stack before traversing the node's left subtree
                stack.append(curr)
                curr = curr.left
            # curr must be None at this point

            curr = stack.pop()


void inOrder(struct Node * root)
{
    stack < Node * > s
    Node * curr = root

    while (curr != NULL | | s.empty() == false)
    {
        / * Reach the left most Node of the
        curr Node * /
        while (curr != NULL)
        {
            / * place pointer to a tree node on
            the stack before traversing
            the node's left subtree * /
            s.push(curr)
            curr = curr -> left
        }

        / * Current must be NULL at this point * /
        curr = s.top()
        s.pop()

        cout << curr -> data << " "

        / * we have visited the node and its
        left subtree.  Now, it's right
        subtree's turn * /
        curr = curr -> right
    } / * end of while * /
}
