class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ''
        for c in s:
            if self.isAlphanumeric(c):
                newS += c.lower()
        l, r = 0, len(newS) - 1
        while l <= r:
            if newS[l] != newS[r]:
                return False
            l += 1
            r -= 1
        return True
            
    def isAlphanumeric(self, c):
        return(
            ord('A')<= ord(c) <= ord('Z') or
            ord('a')<= ord(c) <= ord('z') or 
            ord('0')<= ord(c) <= ord('9')
        )