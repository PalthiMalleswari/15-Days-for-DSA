#  Problem - https://leetcode.com/problems/first-unique-character-in-a-string/description/

#  Intial Approach

class Solution:
    def firstUniqChar(self, s: str) -> int:
        mapp = {}

        for ch in s:
            mapp[ch] = mapp.get(ch,0)+1
            
        freq = {}
        for ch in mapp.keys():
            if mapp[ch] == 1:
                freq[ch] = s.find(ch)
        
        if not freq:
            return -1
        else:
            return min(freq.values())
  Time Complexity - O(N(frequency calculation)+N(find index of unique ocurence ele)+N(minimum index))
  Space Complexity - O(N(mapp)+N(freq))

#  Optimized Approach

class Solution:
    def firstUniqChar(self, s: str) -> int:
        mapp = {}

        for ch in s:
            mapp[ch] = mapp.get(ch,0)+1
            
        for ele in s:
            if mapp[ele] == 1:
                return s.find(ele)
        return -1

Time Complexity = O(2N) = ~O(N)
Space Complexity - O(26) (We only store all english lower letters)

# Efficient Approach / Most Commonly Used Method


class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        freq = [0]*26

        for ch in s:
            freq[ord(ch)-ord("a")] += 1
        for i,ch in enumerate(s):
            if freq[ord(ch)-ord("a")] == 1:
                return i
        return -1
Time Complexity -> ~O(N)
Space Complexity -> O(26)


