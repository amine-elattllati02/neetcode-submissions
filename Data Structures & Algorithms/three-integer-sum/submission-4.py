class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                add = nums[l] + nums[r]
                if nums[i] + add < 0:
                    l += 1
                elif nums[i] + add > 0:
                    r -= 1
                else:
                    res.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
                    while (l < r and nums[l] == nums[l - 1]):
                        l += 1
                    while (l < r and nums[r] == nums[r + 1]):
                        r -= 1
        return res