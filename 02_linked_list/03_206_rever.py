class ListNode:
    def __init__(self, val=int, next=None):
        self.val = val
        self.next = next


class Solution:
    def revear_linked_list(self, head: ListNode) -> ListNode:
        cur = head
        pre = None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp  # 注意此处的先后顺序
        return pre