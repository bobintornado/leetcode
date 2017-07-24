# Runtime: 96 ms Your runtime beats 100.00 % of python submissions.

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # idea add l2 to l1
        original_head = l1
        carry = 0

        while l2 is not None:
            # for this step
            val = l1.val + l2.val + carry
            carry = 0

            if val >= 10:
                val = val - 10
                carry = 1

            l1.val = val

            # for next step
            # prepare l2
            l2 = l2.next

            # prepare l1
            if l2 is not None and l1.next is None:
                l1.next = ListNode(0)

            if l2 is not None:
                l1 = l1.next

        while carry == 1:
            # prepare l1
            if l1.next is None:
                l1.next = ListNode(1)
                break

            l1 = l1.next

            val = l1.val + carry
            carry = 0

            if val >= 10:
                val = val - 10
                carry = 1

            l1.val = val

        return original_head
