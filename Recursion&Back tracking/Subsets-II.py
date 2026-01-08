# Problem - https://leetcode.com/problems/subsets-ii/

# Intial Approach

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        ans = []
        seen = set()
        n = len(nums)

        def subset_2(ind,cur_res):

            if ind<0:
                if tuple(cur_res) not in seen:
                    ans.append(copy.copy(cur_res))
                    seen.add(copy.copy(tuple(cur_res)))
                return
                    
            cur_res.append(copy.copy(nums[ind]))
            subset_2(ind-1,cur_res)
            cur_res.pop()
            subset_2(ind-1,cur_res)
        
        subset_2(n-1,[])
        return ans

Time Complexity -> O(2^N)
Space Complexity -> O(2^N) Stack space + Subseq storing

#====================  Smartly Skip Duplicates After Sorting ====================

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        ans = []
        subarr = []
        n = len(nums)

        def subset_ii(ind):

            if ind == n:
                ans.append(subarr[:])
                return
            
            subarr.append(nums[ind])
            subset_ii(ind+1)
            subarr.pop()

            # This will points to last occurence of current ele
            #  We Can skip this ele as we've already added it 
            while ind+1< n and nums[ind] == nums[ind+1]:
                ind += 1
            subset_ii(ind+1)

        subset_ii(0)
        return ans


Time Complexity -> ~O(2^N)
Space Complexity -> O(2^N) Stack space + Subseq storing
