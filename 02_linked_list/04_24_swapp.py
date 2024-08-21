class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swap_pairs(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(next=head)
        current = dummy_head

        while current.next and current.next.next:
            temp = current.next
            temp1 = current.next.next.next

            current.next = current.next.next
            current.next.next = temp  # 此时dummy -> head的节点已断temp意义体现，引入temp1意义是节点2next要指向1此时3丢失了
            temp.next = temp1
            current = current.next.next  # 循环条件＋1

            return dummy_head.next

