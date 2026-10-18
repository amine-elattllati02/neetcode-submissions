class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        repSet = set()
        maxLen = 0
        for r in range(len(s)):
            while s[r] in repSet:
                repSet.remove(s[l])
                l += 1
            repSet.add(s[r])
            maxLen = max(maxLen, r - l + 1)
        return maxLen