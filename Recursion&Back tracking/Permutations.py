# Problem - https://leetcode.com/problems/permutations/description/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        subseq = []
        ans = []
        n = len(nums)

        def get_subseq():

            if len(subseq) == n:
                ans.append(subseq[:])
            else:
                
                for i in range(n):
                    if nums[i] in subseq:
                        continue
                    subseq.append(nums[i])
                    get_subseq()
                    subseq.pop()
        get_subseq()
        return ans

Time Complexity - O(N*N!)
Space Complexity - O(N) (for stack space and result storage)

# ============ Other Way ===================
# Refernce - https://leetcode.com/problems/permutations/solutions/6141581/video-simple-backtracking-solution-by-ni-9anh/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums[:]]
        
        res = []

        for _ in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for p in perms:
                p.append(n)
            
            res.extend(perms)
            nums.append(n)
        
        return res

Time Complexity - O(N*N!)
Space Complexity - O(N) (for stack space and result storage)
