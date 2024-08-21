class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def detect_cycle(self, head: ListNode) -> ListNode:
        slow = fast =head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:  # 步幅相差1，推算从第一轮相遇处出发到入口的长度与直线部分长度相同
                slow = head
                while slow != fast:  # 相遇之后，一个设到相遇处，一个设到head，再次相遇即入口
                    slow = slow.next
                    fast = fast.next
                return slow

        return None