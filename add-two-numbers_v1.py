# Runtime: 146 ms

def to_number(list_node):
    total = list_node.val
    list_node = list_node.next
    position = 1

    while list_node is not None:
        total = total + list_node.val * 10 ** position
        list_node = list_node.next
        position = position + 1

    return total


def to_list_node(number):
    string = str(number)
    head_node = None
    current_node = None

    for s in reversed(string):
        val = int(s)
        if head_node is None:
            head_node = ListNode(val)
            current_node = head_node
        else:
            current_node.next = ListNode(val)
            current_node = current_node.next

    return head_node


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # idea add l2 to l1

        n1 = to_number(l1)
        n2 = to_number(l2)

        val = n1 + n2

        result = to_list_node(val)

        return result
