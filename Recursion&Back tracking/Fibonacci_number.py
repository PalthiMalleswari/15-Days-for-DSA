# Problem - https://leetcode.com/problems/fibonacci-number/description/

class Solution:
    def fib(self, n: int) -> int:
        dp = [-1]*(n+1)
        def fibb(n):
            if n in (0,1):
                return n
            if dp[n] != -1:
                return dp[n]
            dp[n]=fibb(n-1)+fibb(n-2)
            return dp[n]
        return fibb(n)

Time Complexity - O(N)
Space Complexity - O(N) stack space
