# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None or k == 1:
            return head
        else:
            dummy = ListNode(0)
            dummy.next = head
            curr = dummy
            while curr.next != None:
                curr = self.reverseK(curr, k)
            return dummy.next

    def reverseK(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        for i in range(k):
            if curr.next == None:
                return curr
            curr = curr.next
        next_head = head.next
        curr = head.next
        prev = head
        for i in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head.next = prev
        next_head.next = curr
        return next_head

#Took way too long for this