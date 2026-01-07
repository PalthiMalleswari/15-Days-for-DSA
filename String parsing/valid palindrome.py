#  Problem - https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip()
        if len(s) == 0:
            return True

        st = []
        for ch in s:
            
            if ch.isalnum():
                st.append(ch.lower())

        return True if st == st[::-1] else False

Time Complexity - O(N)
Space Complexity - O(N)



#  Other Way

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        left = 0 
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True
