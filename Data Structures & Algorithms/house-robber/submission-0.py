class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp1 = rob1
            rob1 = rob2
            rob2 = max(n + temp1, rob2)

        return rob2