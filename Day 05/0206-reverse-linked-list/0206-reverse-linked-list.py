# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head == None):
            return None
    
        shiv = None
        
        while(head is not None):
            aru = head.next
            head.next = shiv
            shiv = head
            head = aru
            
        return shiv
            