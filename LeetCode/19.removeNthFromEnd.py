# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def ListNode removeNthFromEnd(ListNode head, int n) {
        int size = 0;
        ListNode temp = head;
        while (temp != null) {
            size++;
            temp = temp.next;
        }
        if (n == size) {
            return head.next;
        }
        temp = head;
        int i = 0;
        while (i < size - n - 1) {
            temp = temp.next;
            i++;
        }
        temp.next = temp.next.next;
        return head;
    }
s = Solution()
print(s.removeNthFromEnd([1,2,3,4,5],1))
        