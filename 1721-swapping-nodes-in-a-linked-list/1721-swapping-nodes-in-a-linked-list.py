# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pre_left = pre_right = dummy = ListNode(None, head)
        left = right = head
        
        for i in range(1, k):
            pre_left = left
            left = left.next
            
        check_null = left 
        while check_null.next:
            pre_right = right 
            right = right.next
            check_null = check_null.next
            
        if left == right:
            return head 
        
        pre_left.next = right
        pre_right.next = left 
        left.next, right.next = right.next, left.next
        return dummy.next
                    
            
        