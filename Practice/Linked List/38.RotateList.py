# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr.next:
            prev = curr
            curr = curr.next
        # Last item
        prev.next = None
        curr.next = head
        return curr
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head
        for _ in range(k):
            head = self.rotateList(head)
        return head
    def print_linked_list(self, node: ListNode) -> None:
        result = str(node.val)
        while True:
            if node.next:
                node = node.next
                result += " -> " + str(node.val)
            else:
                break
        print(result)

# Create nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
# Link all nodes 1 -> 2 -> 3 -> 4 -> 5
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

s = Solution()
s.print_linked_list(node1)
note = s.rotateRight(node1, 2)
s.print_linked_list(note)

