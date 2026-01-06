#  Problem - https://leetcode.com/problems/majority-element/
#  Solution - https://leetcode.com/problems/majority-element/solutions/3676530/3-methods-beats-100-c-java-python-beginn-5cy0

# Intial Approach

  n = len(nums)
  freq = {}

  for ele in nums:
      freq[ele] = freq.get(ele,0) + 1

  for ele in freq:
      if freq[ele] > n/2:
          return ele 

Time Complexity - O(N)
Space Complexity - O(N)

#============ Moore's Voting Algorithm ===========
"""
Algorithm:

Initialize two variables: count and candidate. Set count to 0 and candidate to an arbitrary value.
Iterate through the array nums:
a. If count is 0, assign the current element as the new candidate and increment count by 1.
b. If the current element is the same as the candidate, increment count by 1.
c. If the current element is different from the candidate, decrement count by 1.
After the iteration, the candidate variable will hold the majority element.
"""  
  cnt,cand = 0,inf

  for ele in nums:
      if cnt == 0:
          cand = ele

      if ele == cand:
          cnt += 1
      else:
          cnt -= 1
  return cand

Time Complexity - O(N)
Space Complexity - O(1)
