# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        self.answer = False
        self.findRoot(head, root)
        return self.answer

    def findRoot(self, head: ListNode, root: TreeNode):
        if head.val == root.val:
            self.search(head, root)

        if root.left:
            self.findRoot(head, root.left)
        if root.right:
            self.findRoot(head, root.right)

    def search(self, head: ListNode, root: TreeNode) -> bool:
        if head.next:
            if root.left and root.left.val == head.next.val:
                self.search(head.next, root.left)
            if root.right and root.right.val == head.next.val:
                self.search(head.next, root.right)
        else:
            self.answer = True


# [4,2,1]
# [9,null,4,3,null,1,null,7,null,1,2]
