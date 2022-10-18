# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        left_previous, current_node = dummy, head
        for i in range(left - 1):
            left_previous = current_node
            current_node = current_node.next
            
        # print(left_previous.val, current_node.val)
        previous_node = None 
        
        for i in range(right - left + 1):
            temp_node = current_node.next 
            current_node.next = previous_node 
            previous_node = current_node
            current_node = temp_node
        
        # print(current_node.val, previous_node.val)
        left_previous.next.next = current_node
        left_previous.next = previous_node
        return dummy.next
            
        
            
        
            
        