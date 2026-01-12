# Problem - https://leetcode.com/problems/merge-two-sorted-lists/description/

# Intial Approach


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1:
            return list2
        if not list2:
            return list1

        ans_head = ListNode(-1)

        ans = ans_head

        while list1 and list2:

            if list1.val > list2.val:
                
                new = ListNode(list2.val)
                ans.next = new
                ans = ans.next
                
                list2 = list2.next

            else:

                new = ListNode(list1.val)
                ans.next = new
                ans = ans.next
                list1 = list1.next
        
        if list1:
            while list1:

                new = ListNode(list1.val)
                ans.next = new
                ans = ans.next
                list1 = list1.next

        if list2:
            while list2:
                new = ListNode(list2.val)
                ans.next = new
                ans = ans.next
                list2 = list2.next
                
        return ans_head.next

Time Complexity - O(N1+N2)
Space Complexity - O(N1+N2) // Results Storage

# ======= Slitly Optimized Approach =================

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1:
            return list2
        if not list2:
            return list1

        ans_head = ListNode(-1)

        ans = ans_head

        while list1 and list2:

            if list1.val > list2.val:
                
                new = ListNode(list2.val)
                ans.next = new
                ans = ans.next
                
                list2 = list2.next

            else:

                new = ListNode(list1.val)
                ans.next = new
                ans = ans.next
                list1 = list1.next
        
        if list1:
            ans.next = list1

        if list2:
            ans.next = list2

        return ans_head.next


        

Time Complexity - O(N1+N2)
Space Complexity - O(N1+N2) // Results Storage


        


