# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getKth(current_pointer, steps):
            while current_pointer and steps > 0:
                current_pointer = current_pointer.next
                steps -= 1
                
            return current_pointer
        
        dummy = ListNode(0, head)
        previous_group_node = dummy 
        
        while True:
            kth_node = getKth(previous_group_node, k)
            if kth_node is None:
                break 
                
            next_group = kth_node.next 
            previous = next_group 
            current = previous_group_node.next
            
            
            while current != next_group:
                next_node = current.next 
                current.next = previous
                
                previous = current 
                current = next_node
                
            temp = previous_group_node.next
            previous_group_node.next = kth_node
            previous_group_node = temp
            
        return dummy.next
    
                
            
        