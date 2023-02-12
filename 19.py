from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None:
            return head
        return self.rebuildListNode(head, 1, n)[0]
        
    def rebuildListNode(self, node: Optional[ListNode], curIndex: int, removeIndex: int):
        if node.next == None and removeIndex != 1:
            return [ListNode(node.val, None), curIndex]
        elif node.next == None and removeIndex == 1:
            return [None, curIndex]
        else:
            build = self.rebuildListNode(node.next, curIndex + 1, removeIndex)
            if build[1]-removeIndex+1 == curIndex:
                return build
            else:
                node.next = build[0]
                return [node, build[1]]


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

sol = Solution()
printOutList(buildListNode(1,5))
printOutList(sol.removeNthFromEnd(buildListNode(1,5), 2))
printOutList(buildListNode(1,1))
printOutList(sol.removeNthFromEnd(buildListNode(1,1), 1))
printOutList(buildListNode(1,2))
printOutList(sol.removeNthFromEnd(buildListNode(1,2), 1))