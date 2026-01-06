#  Problem - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        n = len(nums)
        mp = {0:-1}
        s = 0
        for i in range(n):

            s += nums[i]
            if s%k in mp:
                if i-mp[s%k] >= 2:
                    return True
            else:
                mp[s%k] = i

        return False
            
Time Complexity - O(N)
Space Complexity - O(1)


# ======= Explanation =========================
=> Step 1: Introduce prefix sums (key move)

   S[i] = nums[0] + nums[1] + ... + nums[i]
   Then the sum of subarray i+1 .. j is: S[j] - S[i]

=> Step 2: When is a number divisible by k?
  A number is divisible by k iff its remainder when divided by k is 0.
  So we want: (S[j] - S[i]) % k == 0

=> Step 3: Use modulo arithmetic (this is the core insight)
  From modulo rules:
  (S[j] - S[i]) % k == 0
  ⇔ S[j] % k == S[i] % k

=============== What this means intuitively =======================
If two prefix sums leave the same remainder when divided by k,
then the numbers between them sum to a multiple of k.
====================================================================

=> Why we store s % k in the map
  mp = {0: -1}
  stores:
  remainder → earliest index where this remainder appeared

  As you iterate:: 
  s += nums[i]
  rem = s % k
  You check: if rem in mp:


=> This means:
  “I’ve seen another prefix sum earlier with the same remainder.”
  So the subarray between those two indices has sum divisible by k.

=> Why mp = {0: -1} is needed
  
  This handles cases like:
  nums = [2, 4]
  k = 6
  
  Prefix sum at index 1 = 6
  6 % 6 = 0
  
  By mapping 0 → -1, we allow:
  i - (-1) = 2  ✅ length ≥ 2
  if {0:1} then i-(1) = 0 which is not correct, hence 0 -> -1
  So subarrays starting from index 0 are correctly detected.


=> Final honest takeaway

  We use S % k not as a trick, but because:
  (A - B) divisible by k ⇔ A % k == B % k
  The hashmap remembers where each remainder first occurred
  This turns a brute-force O(n²) problem into O(n)


# =========== Try Out Similar Problems =====================
https://leetcode.com/problems/continuous-subarray-sum/solutions/5276981/prefix-sum-hashmap-patterns-7-problems-b-6794/
