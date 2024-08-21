class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def delete_n_element(self, head: ListNode, n:int) -> ListNode:
        dummy_head = ListNode(next=head)
        fast = slow = dummy_head

        for i in range(n+1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy_head.next