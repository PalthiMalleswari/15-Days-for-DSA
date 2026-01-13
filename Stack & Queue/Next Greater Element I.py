# Problem - https://leetcode.com/problems/next-greater-element-i/description/

#============== Brute Force Apporach ==============

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        n1 = len(nums1)
        n2 = len(nums2)
        ans = []
        mapp = {}

        for idx,ele in enumerate(nums2):
            mapp[ele] = idx

        for ele in nums1:
            found = False
            for i in range(mapp[ele],n2):
                if ele<nums2[i]:
                    ans.append(nums2[i]) 
                    found = True
                    break
            if not found:
                ans.append(-1)
        return ans
      
Time Complexity - O(N*M)
Space Complexity - O(N) // Hash Map

# ========= Slitly Space Optimized but lower Time =====================

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        n1 = len(nums1)
        n2 = len(nums2)
        ans = []
        
        for ele in nums1:

            found = False
            nq = -1
            for i in range(n2):

                if nums2[i]==ele:
                    found = True

                elif found:
                    if nums2[i] > ele:
                        nq = nums2[i]
                        break
            ans.append(nq)
            
        return ans
Time Complexity - O(N*M)
Space Complexity - O(1)

# ======= Optimized Monotonic Stack =====================

- Monotonically Decreasing Stack Solution

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
      
        mapp = {}
        stack = []

        for ele in nums2:

            while stack and ele > stack[-1]:
                mapp[stack.pop()] = ele
            
            stack.append(ele)
        return [ mapp.get(ele,-1) for ele in nums1]

Time Complexity - O(N+M)
Space Complexity - O(N)

            
