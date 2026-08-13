class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float("infinity")
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                window = nums[i:j]
                if sum(window) >= target:
                    min_length = min(min_length , len(window))
                    break
        if min_length == float("infinity"):
            return 0
        else:
            return min_length