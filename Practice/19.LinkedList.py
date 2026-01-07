class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
def reverseList(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        #1 Save the next node - So we don't lose the rest of the list
        next_node = curr.next
        #2 Flip the arrow: make curr.next point to prev
        curr.next = prev
        #3 Move prev up to curr
        prev = curr
        #4. Move curr up to the save next node
        curr = next_node
    return prev
def print_linked_list(node: ListNode) -> None:
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

# Link them: 1 -> 2 -> 3 -> 4
node1.next = node2
node2.next = node3
node3.next = node4

print("Original List:")
print_linked_list(node1) # Output: 1 -> 2 -> 3 -> 4

# Run your reversal function
new_head = reverseList(node1)

print("Reversed List:")
print_linked_list(new_head) # Output: 4 -> 3 -> 2 -> 1
