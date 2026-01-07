# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # Move right pointer n steps ahead
        for _ in range(n):
            if right: # Safety check
                right = right.next
        
        # Move both until right reaches the end
        while right:
            left = left.next
            right = right.next
            
        # NOW: left is BEFORE the node we want to delete
        # "Skip it"
        left.next = left.next.next
        return dummy.next
    def printList(self, node: ListNode):
        result = ""
        while node.next:
            result = str(node.val) + " -> "
            node = node.next
        print(result)

s = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4

new_node = s.removeNthFromEnd(node1, 2)
s.printList(new_node)