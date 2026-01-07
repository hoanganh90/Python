class ListNode:
    def __init__(self, val = 0 , next = None):
        self.val = val
        self.next = next
def findMiddle(head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
def printList( node: ListNode):
    result = ""
    while node.next:
        result = node.next + " -> "
        node = node.next
    print(result)
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

middleNode = findMiddle(node1)
print(middleNode.val)