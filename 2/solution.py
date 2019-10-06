# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        plus = 0
        curL1 = l1
        curL2 = l2
        while curL1 is not None or curL2 is not None:
            if curL1 is None:
                l1_val = 0
            else:
                l1_val = curL1.val
            if curL2 is None:
                l2_val = 0
            else:
                l2_val = curL2.val
            sum = l1_val + l2_val + plus
            rest = sum % 10
            plus = sum // 10
            curL1.val = rest
            if curL1.next is None and ((curL2 is not None and curL2.next is not None) or plus > 0):
                curL1.next = ListNode(0)
            if curL1 is not None:
                curL1 = curL1.next
            if curL2 is not None:
                curL2 = curL2.next
        return l1
