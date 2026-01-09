#  Problem - https://leetcode.com/problems/permutations-ii/

# Naive Approach

#  Don't pick dublicate elements after taking same value again

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        perm,ans = [],[]
        visited = []
        nums.sort()

        def generate_perms():

            if len(perm) == n:
                ans.append(perm[:])
                return
            else:
                i = 0
                while i < n:

                    if i in visited:
                        i += 1
                        continue
                    perm.append(nums[i])
                    visited.append(i)
                    generate_perms()
                    perm.pop()
                    visited.pop()

                    if i+1 < n and nums[i] == nums[i+1]:

                        while i+1 < n and nums[i] == nums[i+1]:
                            
                            i += 1
                    i+=1

        generate_perms()
        return ans

      
#  ============== Other Intuite Way ===============

 # Intuation Is

  """

             []
     /    |    \
   1      1     2
 (i=0)  (i=1)  (i=2)

So the rule is:

If this value is the same as the previous value, and the previous one was NOT used in this branch, skip it.

That is exactly what this line enforces:

if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
    continue
"""
        nums.sort()
        n = len(nums)
        res = []
        perm = []
        visited = [False] * n

        def backtrack():
            if len(perm) == n:
                res.append(perm[:])
                return

            for i in range(n):

                # Rule 1 — cannot reuse same index
                if visited[i]:
                    continue

                # Rule 2 — skip duplicate values at same tree level, which shouldn't be visited already,
                #  If current index's value equals to previous val but previous is already visited means, curret element is a new element 
                if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue

                visited[i] = True
                perm.append(nums[i])
                backtrack()
                perm.pop()
                visited[i] = False

        backtrack()
        return res
