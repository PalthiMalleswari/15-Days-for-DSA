# Problem - https://leetcode.com/problems/string-to-integer-atoi/description/
# Solution Reference - https://leetcode.com/problems/string-to-integer-atoi/solutions/6924378/video-on-time-and-o1-space-by-niits-8h92/

#  Intial Approach

class Solution:
    def myAtoi(self, s: str) -> int:

        
        strp_s = s.strip()
        n = len(strp_s)
        ans = []

        if not strp_s:
            return 0
        
        sign = strp_s[0]
        
        if sign not in ('+','-') and not sign.isdigit():
            return 0
        
        if sign.isdigit():
            i = 0
            sign = '+'
        else:
            i = 1

        for j in range(i,n) :

            if not strp_s[j].isdigit():
                break
            else:
                ans.append(strp_s[j])

        final = sign+"".join(ans)

        def to_int32(x: int) -> int:
            INT_MIN = -2**31
            INT_MAX = 2**31 - 1
            return max(INT_MIN, min(INT_MAX, x))
        
        if final in ('+','-'):
            return 0
        else:
            return to_int32(int(final))

  Time Complexity -> ~O(N)
  Space Complexity -> O(N)


# ========== Other Iterative Approach ==================

class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        
        # Constants for 32-bit signed integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        i = 0
        n = len(s)
        
        # Step 1: Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1
        
        # Check if we've reached the end
        if i == n:
            return 0
        
        # Step 2: Check for sign
        sign = 1
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1
        
        # Step 3: Read digits and convert
        res = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            res = res * 10 + digit
            
            if sign * res <= INT_MIN:
                return INT_MIN
            if sign * res >= INT_MAX:
                return INT_MAX
            
            i += 1
        
        # Step 4: Apply sign and return
        return res * sign

Time Complexity - O(N)
Space Complexity - O(1)
