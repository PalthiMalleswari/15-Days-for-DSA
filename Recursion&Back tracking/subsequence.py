# Problem - https://leetcode.com/problems/subsets/description/

# ========= Back Tracking Approach =================

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []

        def get_subseq(ind,cur_ans):

            if ind < 0:
                ans.append(copy.copy(cur_ans))  # Be Aware Pythons Immutability Nature !!!
                return

            # pick
            cur_ans.append(copy.copy(nums[ind])) # Be Aware Pythons Immutability Nature !!!
 
            get_subseq(ind-1,cur_ans)
            # not_pick
            cur_ans.pop()
            get_subseq(ind-1,cur_ans)

        n = len(nums)   
        get_subseq(n-1,[])
        return ans

Time Complexity - O(2^N)
Space Complexity - O(No of susequences)

# Similar Problems

https://leetcode.com/problems/subsets/solutions/27281/a-general-approach-to-backtracking-quest-0ea5/
