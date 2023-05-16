# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous_group_node = dummy = ListNode(None, head)
        
        while True:
            kth_node = self.get_kth_node(previous_group_node, 2)
            if kth_node is None:
                return dummy.next
            
            next_group_node = kth_node.next 
            previous_node = next_group_node
            current = previous_group_node.next
            
            while current != next_group_node:
                next_node = current.next 
                current.next = previous_node
                
                previous_node = current
                current = next_node 
            
            temp = previous_group_node.next
            previous_group_node.next = kth_node 
            previous_group_node = temp
            
                
            
        
    def get_kth_node(self, current, steps):
        while current and steps > 0:
            current = current.next
            steps -= 1
        return current 
        
        