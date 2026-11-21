class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxLength = 0
        l, r = 0, 0
        while r < len(s):
            if s[r] in seen:
                seen.remove(s[l])
                l += 1
            else:
                seen.add(s[r])
                length = r - l + 1
                maxLength = max(maxLength, length)
                r += 1
        return maxLength