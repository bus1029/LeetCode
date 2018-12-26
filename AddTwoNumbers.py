# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #         up = 0
        #         head = None
        #         tail = None

        #         while True:
        #             l1_val, l2_val = 0, 0

        #             if l1 is None and l2 is None:
        #                 break
        #             elif l1 is None and l2 is not None:
        #                 l2_val = l2.val
        #             elif l1 is not None and l2 is None:
        #                 l1_val = l1.val
        #             else:
        #                 l1_val, l2_val = l1.val, l2.val

        #             if up == 0:
        #                 if l1_val + l2_val > 10:
        #                     up = 1

        #                     if head is None:
        #                         head = ListNode(l1_val + l2_val - 10)
        #                         tail = head.next
        #                     else:
        #                         tail = ListNode(l1_val + l2_val - 10)
        #                         tail = tail.next
        #             else:
        #                 if l1_val + l2_val + up > 10:
        #                     up = 1

        #                     if head is None:
        #                         head = ListNode(l1_val + l2_val + up - 10)
        #                         tail = head.next
        #                     else:
        #                         tail = ListNode(l1_val + l2_val + up - 10)
        #                         tail = tail.next

        #                 else:
        #                     up = 0

        #                     if tail is None:
        #                         head = ListNode(l1_val + l2_val)
        #                         print(head.val)
        #                         tail = head.next
        #                     else:
        #                         tail = ListNode(l1_val + l2_val)
        #                         tail = tail.next

        #             if l1 is not None:
        #                 l1 = l1.next

        #             if l2 is not None:
        #                 l2 = l2.next

        ans = 0
        unit = 1

        while l1 or l2:
            if l1:
                ans += l1.val * unit
                l1 = l1.next
            if l2:
                ans += l2.val * unit
                l2 = l2.next
            unit *= 10

        alpha = cur = ListNode(0)

        for n in reversed(str(ans)):
            cur.next = ListNode(int(n))
            cur = cur.next

        return alpha.next


