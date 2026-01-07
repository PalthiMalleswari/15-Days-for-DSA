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
