# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        temp = head
        while temp:
            if not stack:
                stack.append(temp.val)
                
            else:
                while stack and stack[-1] < temp.val:
                    stack.pop()
                    
                stack.append(temp.val)
                
            temp = temp.next
        root = dummy = ListNode(None)
        while stack:
            value = stack.pop(0)
            root.next = ListNode(value)
            root = root.next
            
        return dummy.next
            
        