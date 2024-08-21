class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def get_intersection_node(self, headA: ListNode, headB: ListNode):
        lenA = self.get_length(headA)
        lenB = self.get_length(headB)

        if lenA > lenB:
            headA = self.move_forward(headA, lenA - lenB)
        else:
            headB = self.move_forward(headB, lenB - lenA)

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None

    def get_length(self, head: ListNode) -> int:
        length = 0
        while head:
            head = head.next
            length += 1
        return length

    def move_forward(self, head: ListNode, steps: int) -> ListNode:
        while steps > 0:
            head = head.next
            steps -= 1
        return head
