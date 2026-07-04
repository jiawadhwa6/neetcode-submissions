class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd={}
        td={}
        if len(s) != len(t):
            return False
        for i in range (0,len(s)):
            sd[s[i]] = 1+ sd.get(s[i],0)
            td[t[i]] = 1+ td.get(t[i],0) # 0 is default thing 
        if sd == td:   # to return if value is not found
            return True
        return False

        