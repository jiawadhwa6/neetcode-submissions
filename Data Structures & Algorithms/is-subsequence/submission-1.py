class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s=="":
            return True

        tp = 0
        sp = 0

        while sp<len(s) and tp<len(t):
            
            if s[sp]== t[tp]:
                sp += 1
                tp +=1
                if sp==len(s):
                    return True
            else:
                tp+=1
        return False
            
        