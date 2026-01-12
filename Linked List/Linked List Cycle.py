#  Problem - https://leetcode.com/problems/linked-list-cycle/description/

# Intial Traversing Approach
"""
If a Node is visited twice then it has a cycle else no cycle
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # Hash map to store seen nodes
        hash_map = {}

        temp = head

        while temp:

            if temp in hash_map:
                return True
            hash_map[temp] = hash_map.get(temp,0) + 1
            temp = temp.next
        
        return False


Time Complexit - O(N)
Space Complexity - O(N) //HashMap

# ============ Slow and Fast Pointer Approach =============

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
    
        slow,fast = head,head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False

#  Reference - https://leetcode.com/problems/linked-list-cycle/solutions/1829489/c-easy-to-understand-2-pointer-fast-slow-rw9u/
