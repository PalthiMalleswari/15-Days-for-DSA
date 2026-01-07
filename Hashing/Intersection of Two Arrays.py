# Problem - https://leetcode.com/problems/intersection-of-two-arrays/description/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapp = {}

        for num in nums1:
            mapp[num] = mapp.get(num,0)+1
        
        ans = set()
        for n2 in nums2:

            if n2 in mapp:
                ans.add(n2)
        return list(ans)

Time Complexity - O(N1+N2)
Space Complexity -O(N)
