from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None: return None
        elif list1 == None: return list2
        elif list2 == None: return list1

        if list1.val <= list2.val:
            return ListNode(list1.val, self.mergeTwoLists(list1.next, list2))
        
        return ListNode(list2.val, self.mergeTwoLists(list1, list2.next))
            

def buildListNode(val: int, index: int):
    if index == 1:
        return ListNode(val, None)
    else:
        return ListNode(val, buildListNode(val+1,index-1))

def printOutList(list):
    output = []
    if list != None:
        while list.next != None:
            output.append(list.val)
            list = list.next
        output.append(list.val)
    print(output)

list1 = ListNode(1, ListNode(2, ListNode(4, None)))
list2 = ListNode(1, ListNode(3, ListNode(4, None)))

sol = Solution()
printOutList(list1)
printOutList(list2)
printOutList(sol.mergeTwoLists(list1, list2))

