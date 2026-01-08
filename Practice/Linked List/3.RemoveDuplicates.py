class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    if not head:
        return head
    right = head
    while right and right.next:
        if right.val == right.next.val:
            right.next = right.next.next
        else: # ALWAYS move forward if no duplicate was found
            right = right.next
    return head
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
node3 = ListNode(2)
node4 = ListNode(4)

# Link them: 1 -> 2 -> 3 -> 4
node1.next = node2
node2.next = node3
node3.next = node4

print("Original List:")
print_linked_list(node1) # Output: 1 -> 2 -> 2 -> 4
deleted_duplicates = deleteDuplicates(node1)
print_linked_list(deleted_duplicates) # Output: 1 -> 2 -> 4