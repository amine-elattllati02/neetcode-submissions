class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLength = 0
        for n in nums:
            sub = []
            if n-1 not in numSet:
                sub.append(n)
                while n + 1 in numSet:
                    sub.append(n+1)
                    n += 1
                maxLength = max(maxLength, len(sub))
        return maxLength
