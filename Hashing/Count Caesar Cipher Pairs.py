#  Problem - https://leetcode.com/problems/count-caesar-cipher-pairs/description/

#  Intial TLE Approach

class Solution:
    def countPairs(self, words: List[str]) -> int:

        n = len(words)
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                res = self.is_similar(words[i],words[j])
                if res:
                    ans += 1
        return ans

    def is_similar(self,s1,s2):

        if s1 == s2:
            return True
        
        char_ar = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        
        n2 = len(s1)

        for i in range(26):
            chose = ''
            for j in range(n2):
                new_index = (ord(s1[j]) - ord('a') + i) % 26
                chose += char_ar[new_index]
        
            if chose == s2:
                return True
        
        return False
#  Refer chat gpt explanation - https://chatgpt.com/c/69635d68-b6f0-8324-b5e9-a3ee9298e308

Time Complexity - O(N^2+length of word*26)
Space Complexity - O(N)


#  Optimized Approach
class Solution:
    def countPairs(self, words: List[str]) -> int:

        patterns = {}
        ans = 0
        for word in words:
            can_form = [0]*len(word)
            base = ord(word[0])

            for i in range(len(word)):
                can_form[i] = str((ord(word[i])-base+26)%26)

            pattern = "".join(can_form)
            ans += patterns.get(pattern,0)
            patterns[pattern] = patterns.get(pattern,0)+1

        return ans

Time Complexity - O(N*M(average length of words))
Space Complexity - O(N)
