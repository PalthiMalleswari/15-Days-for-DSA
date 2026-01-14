#  Problem - https://leetcode.com/problems/search-insert-position/description/
# Rerence - https://leetcode.com/problems/search-insert-position/solutions/5361984/video-return-middle-or-left-pointer-by-n-dj1y/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        l,r = 0,n-1

        while l<=r:

            mid = (l+r)//2

            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                r = mid-1
            elif nums[mid]<target:
                l = mid+1
                
        return l

Time Complexity - O(log N)
Space Complexity - O(1)

# ======== Other Way ==========

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        l,r = 0,n-1

        while l<r:

            mid = (l+r)//2

            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                r = mid
            elif nums[mid]<target:
                l = mid+1
                
        return l if nums[l] >= target else l+1 
