#  Problem - https://leetcode.com/problems/combination-sum/description/

# Intial Approach

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        n = len(candidates)
        comb = []
        res = []

        def generate_comb(ind,need):

            if need==0:
                res.append(comb[:])
                return
            if ind >= n:
                return

            if candidates[ind] <= need:
                comb.append(candidates[ind])
                generate_comb(ind,need-candidates[ind])
                ele = comb.pop()
            
            generate_comb(ind+1,need)
        
        generate_comb(0,target)
        return res

  Time Complexity - O(2^N) //Each Element have two possibilities either take or not_take
  Space Complexity - O(N)
