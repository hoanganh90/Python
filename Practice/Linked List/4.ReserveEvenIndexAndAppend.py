# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reverseList (head: SinglyLinkedList):
    prev = None
    curr = head
    while curr:
        # Store the next node
        next_node = curr.next
        
        #Flip the arrow. Point the curr.next to prev
        curr.next = prev
        
        # Move prev up to curr
        prev = curr
        
        # Move curr up to the saved next node
        curr = next_node
    return prev
def extractAndAppendSponsoredNodes(head):
    if not head or not head.next:
        return head
    # Write your code here
    Extract_Even_Nodes = head.next
    remaining_Odd_nodes = head
    while Extract_Even_Nodes and Extract_Even_Nodes.next:
        #By setting odd.next = even.next, you are physically removing the even node from the main sequence.
        remaining_Odd_nodes.next = Extract_Even_Nodes.next
        remaining_Odd_nodes = remaining_Odd_nodes.next
        
        Extract_Even_Nodes.next = remaining_Odd_nodes.next
        Extract_Even_Nodes = Extract_Even_Nodes.next
        
    # Maintaining the Tail: After the while loop, the pointer odd is naturally sitting at the very last node of the remaining list. This is your "attachment point."
    remaining_Odd_nodes.next = None
    new_reserse_List = reverseList(Extract_Even_Nodes)
    # The Append: odd.next = reversed_even acts like a bridge, connecting the end of your original # nodes to the start of your newly reversed nodes.
    remaining_Odd_nodes.next = new_reserse_List
    return head