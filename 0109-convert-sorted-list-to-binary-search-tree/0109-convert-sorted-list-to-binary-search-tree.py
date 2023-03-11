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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def get_size(root):
            size = 0
            while root:
                root = root.next
                size += 1
                
            return size 
        
        
        def generate(left, right):
            nonlocal head 
            
            if left > right:
                return None
            
            mid = (left + right) // 2
            left_part = generate(left, mid - 1)
            node = TreeNode(head.val)
            head = head.next
            right_part = generate(mid + 1, right)
            
            node.left = left_part
            node.right = right_part 
            
            return node 
        
        return generate(0, get_size(head) - 1)
            