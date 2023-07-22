# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if(head == None or head.next == None or k==0):
            return head
        
        aru = head
        shiv = head
        
        count = 1
        while(aru.next is not None):
            aru = aru.next
            count+=1
            
        aru = head
        
        print(count)
        
        k = k % count
            
        for i in range(abs(count-k-1)):
            aru = aru.next
            
        while(shiv.next is not None):
            shiv = shiv.next
        
        shiv.next = head
        ptr = head
        head = aru.next
        aru.next = None
        
        return head