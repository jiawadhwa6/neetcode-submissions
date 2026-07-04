class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for i in s:
            if (i.isalpha() or i.isdigit()):
                st += i.lower()
        print(st)
        if (st == st[::-1]):
            return True
        else:
            return False
        