class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        


        if len(s) != len(t):
            return False

        CountS, CountT = {}, {}
        for i in range(len(s)):
            CountT[s[i]] = 1 + CountT.get(s[i], 0)
            CountS[t[i]] = 1 + CountS.get(t[i], 0)
        for c in CountT:
            if CountT[c] != CountS.get(c, 0):
                return False
        return True