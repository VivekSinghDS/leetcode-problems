# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def get_pointer():
            slow, fast = head, head 

            while fast and fast.next:
                slow = slow.next 
                fast = fast.next.next
                
                if slow == fast:
                    return slow
                
            return None 

        new_ptr = head
        slow = get_pointer()
        if not slow:
            return None 
        
        while new_ptr != slow:
            slow = slow.next
            new_ptr = new_ptr.next 
            
        return new_ptr
        