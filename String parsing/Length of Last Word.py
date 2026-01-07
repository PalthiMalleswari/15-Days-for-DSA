#  Problem - https://leetcode.com/problems/length-of-last-word/description/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        strip_s = s.strip()
        n = len(strip_s) 
        i = n-1
        while i >= 0 :
            
            if strip_s[i].isspace():
                return n-1-i
            i -= 1
        return n

Time Complexity - O(N)
Space Complexity - O(1)
