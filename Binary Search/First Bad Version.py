# Problem - https://leetcode.com/problems/first-bad-version/description/

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,r = 1,n
        ans = -1
        while l<=r:
            mid = (l+r)//2

            if isBadVersion(mid):
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans

Time Complexity - O(logN)
Space Complexity - O(1)


# ============ Other Way ! =================

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,r = 1,n
        while l<r:
            mid = (l+r)//2

            if isBadVersion(mid):
                r = mid
            else:
                l = mid+1
        return l
Time Complexity - O(logN)
Space Complexity - O(1)
