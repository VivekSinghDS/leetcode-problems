# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        previous_group_node = dummy 
        
        while True:
            kth_node = self.getKth(previous_group_node, 2)
            if kth_node is None:
                break 
            
            next_group_node = kth_node.next 
            previous_node, current_node = next_group_node, previous_group_node.next
            
            while current_node != next_group_node:
                next_node = current_node.next 
                current_node.next = previous_node
                
                previous_node = current_node
                current_node = next_node 
                
            temp = previous_group_node.next
            previous_group_node.next = kth_node
            previous_group_node = temp
        
        return dummy.next 
            
    def getKth(self, current_pointer, steps):
        while current_pointer and steps > 0:
            current_pointer = current_pointer.next 
            steps -= 1
            
        return current_pointer 
        
        