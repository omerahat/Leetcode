# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def getIntersectionNode(self, headA, headB):
    firstPointer= headA
    secondPointer = headB

    while firstPointer != secondPointer:
        if firstPointer != None:
            firstPointer = firstPointer.next 
        else:
            firstPointer.next = headB

        if secondPointer != None:
            secondPointer  = secondPointer.next
        else:
            secondPointer.next = headA
        
    return firstPointer

