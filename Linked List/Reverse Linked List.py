# Problem - https://leetcode.com/problems/reverse-linked-list/description/

#  Intial Approach

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        temp = head
        prev = None
        lat = None

        while temp:
            
            new_node = ListNode(temp.val)
            new_node.next = lat
            lat = new_node
            prev = temp
            temp = temp.next

        return lat

Time Complexity - O(N)
Space Complexity - O(1)
