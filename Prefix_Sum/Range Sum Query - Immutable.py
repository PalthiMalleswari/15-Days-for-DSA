# Problem - https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        
        n= len(nums)
        self.pref_sum = [0]*n
        for i in range(n):
            self.pref_sum[i] = self.pref_sum[i-1]+nums[i]

    def sumRange(self, left: int, right: int) -> int:

        if left == 0:
            return self.pref_sum[right]
        else:
            return self.pref_sum[right]-self.pref_sum[left-1]        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

Time Complexity of sumRange is O(1)
Space Complexity - O(N)
