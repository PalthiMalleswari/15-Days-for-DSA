# Problem - https://leetcode.com/problems/power-of-two/description/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n<=0:
            return False
        bi = bin(n)
        cnt = 0
        
        for i in range(2,len(bi)):
            if bi[i] == "1":
                cnt += 1
 
            if cnt >= 2:
                return False
        
        return True

Time Complexity - O(N)
Space complexity - O(1)


#======== Logarithmic Solution ======================

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (math.log2(n) % 1 == 0)

#  See Different Ways of Doing This !!
https://leetcode.com/problems/power-of-two/solutions/7059233/one-simple-trick-beats-100-by-la_castill-6lvh/
