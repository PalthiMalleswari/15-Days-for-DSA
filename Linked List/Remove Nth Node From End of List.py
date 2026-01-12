# Problem - https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

#================= Intial Solution ======================


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        hash_map = {}

        temp  = head
        i=0

        while temp:
            hash_map[i] = temp
            temp = temp.next
            i +=1

        rm_index = len(hash_map)-n
        prev_index = len(hash_map)-n-1

        if rm_index in hash_map and prev_index in hash_map:
            cur = hash_map[rm_index]
            prev = hash_map[prev_index]
            prev.next = cur.next
            cur.next = None

        else:
            head = hash_map.get(rm_index+1,None)

        return head
      
Time Complexity - O(N)
Space Complexity - O(N) // Hash Map

# ======== Slite Difference ====================
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
         # Step 1: Store nodes with index
        index_map = {}
        temp = head
        i = 0
        
        while temp:
            index_map[i] = temp
            temp = temp.next
            i += 1
        
        size = i
        
        # Step 2: Find index to remove
        remove_index = size - n
        prev_index = remove_index - 1
        
        # Step 3: If deleting head
        if remove_index == 0:
            return head.next
        
        # Step 4: Delete non-head node
        prev_node = index_map[prev_index]
        curr_node = index_map[remove_index]
        
        prev_node.next = curr_node.next
        curr_node.next = None
        
        return head
# ============== Optimal Aproach (Fast and Slow Pointer) ================

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        slow,fast = head,head
        
        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:

            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head

Time Complexity - O(N)
Space Complexity - O(1)

