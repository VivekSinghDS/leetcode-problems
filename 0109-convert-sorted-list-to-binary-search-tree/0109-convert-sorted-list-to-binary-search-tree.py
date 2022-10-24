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
        def find_size(cur):
            count = 0 
            while cur:
                cur = cur.next
                count += 1
                
            return count 
        
        def generate(left, right):
            nonlocal head
            if left > right:
                return None 
            
            mid = (left + right) // 2
            left = generate(left, mid - 1)
            
            root = TreeNode(head.val)
            
            root.left = left
            head = head.next
            right = generate(mid + 1, right)
            
            root.right = right
            return root
        
        return generate(0, find_size(head) - 1)
            

        