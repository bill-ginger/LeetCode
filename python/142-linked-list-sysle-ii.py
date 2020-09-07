# medium

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''2020-09-07'''
class Solution:  # O(N) of time and space
    def detectCycle(self, head: ListNode) -> ListNode:
        id_list = [id(head)]
        curr = head
        while curr and curr.next:  # in case the head is None
            if id(curr.next) in id_list:
                return curr.next
            curr = curr.next
            id_list.append(id(curr))
        return None