#  Problem - https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_1 = {}
        hash_2 = {}

        for ch in s:
            hash_1[ch] = hash_1.get(ch,0)+1
        
        for ch in t:
            hash_2[ch] = hash_2.get(ch,0)+1

        return hash_1 == hash_2
N1 -> len(s) N2 -> len(t)

Time Complexity - O(N1+N2)
Space Complexity - O(N1+N2)
