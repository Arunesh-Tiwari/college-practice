class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p, q = l1, l2
        if p is None:
            return q
        elif q is None:
            return p
        if p.val < q.val:
            r = p
            p = p.next
        else:
            r = q
            q = q.next
        temp = r
        while p and q:
            if p.val<q.val:
                temp.next = p
                p = p.next
            else:
                temp.next = q
                q = q.next
            temp = temp.next
        if p is None:   
            temp.next = q
        else:
            temp.next = p
        return r