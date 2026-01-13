 # Problem - https://leetcode.com/problems/valid-parentheses/description/

# ====== Intial Approach ================

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        mapp ={

            ')':'(',
            '}':'{',
            ']':'['
        }

        for ch in s:

            if ch in ('(','{','['):
                stack.append(ch)

            elif ch in (']',')','}'):

                if not stack:
                    return False

                top = stack[-1]
                if top == mapp[ch]:
                    stack.pop()
                else:
                    return False

        if not stack:
            return True
            
        return False
      
Time Complexity - O(N)
Space Complexity - O(N) // Stack Space

# ========== Slitely Modified Solution ==================
class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        mapp ={

            ')':'(',
            '}':'{',
            ']':'['
        }

        for ch in s:

            if ch in mapp.values():
                stack.append(ch)

            elif ch in mapp.keys():

                if not stack or mapp[ch] != stack.pop():
                    return False

        return not stack

# =========== Other Way  ==================

class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for i in range(len(s)):
            if st:
                last = st[-1]
                if self.is_pair(last, s[i]):
                    st.pop()
                    continue
            st.append(s[i])
        
        return not st
    
    def is_pair(self, last, cur):
        if last == "(" and cur == ")" or last == "{" and cur == "}" or last == "[" and cur == "]":
            return True
        return False


