# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        
        def retrieve_vals(root):
            vals = list()
            while root:
                vals.append(root.val)
                root = root.next
            return vals
        
        vals1 = retrieve_vals(l1)
        vals2 = retrieve_vals(l2)
        number1 = 0
        number2 = 0
        for i in range(len(vals1)):
            number1 += 10 ** i * vals1[i]
        for i in range(len(vals2)):
            number2 += 10 ** i * vals2[i]    
        res = number1 + number2
        res_list = list()
        if res == 0:
            res_list = [0]
        else:    
            while res != 0:
                res_list.append(res % 10)
                res = res // 10
        dummy = ListNode()
        current = dummy
        i = 0
        while i < len(res_list):
            current.next = ListNode(res_list[i])
            current = current.next
            i += 1
        return dummy.next 
        