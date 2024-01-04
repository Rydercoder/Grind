class Solution(object):
    def isAnagram(self, s, t):
        
        
       
        
        if len(s) != len(t):
            return False
        
        hashmaS = {}
        hashmaT = {}
        
        for i in range(len(s)):
            hashmaS[s[i]] = 1 + hashmaS.get(s[i], 0)
            hashmaT[t[i]] = 1 + hashmaT.get(t[i], 0)
            
        for c in hashmaS:
            if hashmaS[c] != hashmaT.get(c, 0):
                return False
                
        return True
