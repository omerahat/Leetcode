# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseList(head):

    if not head:
        return None
    
    if head.next == None:
        return head
    
    prev = None
    current = head
    next = head.next

    while current:
        current.next = prev
        prev = current
        current = next
        if next:
            next = next.next
    
    return prev
