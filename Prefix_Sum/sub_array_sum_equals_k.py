#  Problem - https://leetcode.com/problems/subarray-sum-equals-k/description/

#================= Brute Force ==========================

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        n = len(nums)
        ans = 0
        for i in range(n):
            s = 0
            for j in range(i,n):
                s += nums[j]
                if s==k:
                    ans += 1
        return ans
      
  # Time Complexity - O(N^2)
  # Space Complexity - O(1)

# ================ Prefix Sum Approach ==================
        pf_s = [0]*(n)
        for i in range(n):

            pf_s[i] = pf_s[i-1]+nums[i]

        hash_map = {}
        for ps in pf_s:

            if ps == k:
                ans += 1

            need = ps-k
            
            if need in hash_map:
                
                ans += hash_map[need]

            hash_map[ps] = 1+hash_map.get(ps,0)
        return ans

    #  Time Complexity - O(N)
    #  Space Complexity - O(N)

# ============== Similar Practice Problems ============================

Same as (with a slight modification)
https://leetcode.com/problems/contiguous-array/description/
https://leetcode.com/problems/subarray-sum-equals-k/description/
https://leetcode.com/problems/subarrays-with-k-different-integers/description/
https://leetcode.com/problems/count-number-of-nice-subarrays/description/
https://leetcode.com/problems/binary-subarrays-with-sum/description/
https://leetcode.com/problems/subarray-product-less-than-k/description/
https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description/
  
