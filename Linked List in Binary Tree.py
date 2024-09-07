# https://leetcode.com/problems/linked-list-in-binary-tree/?envType=daily-question&envId=2024-09-07
# Linked List in Binary Tree

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        def check_path(node: TreeNode, index: int) -> bool:
            stack = [(node, index)]
            while stack:
                current, idx = stack.pop()
                if idx == len(arr):
                    return True
                if current and current.val == arr[idx]:
                    stack.append((current.right, idx + 1))
                    stack.append((current.left, idx + 1))
            return False
        
        tree_stack = [root]

        while tree_stack:
            node = tree_stack.pop()
            if node:
                if check_path(node, 0):
                    return True
                tree_stack.append(node.right)
                tree_stack.append(node.left)
        
        return False