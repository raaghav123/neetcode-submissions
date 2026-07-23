class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final_arr = []
        for i in range(len(nums)):
            val1 = 1
            val2 = 1
            for j in range(i+1 , len(nums)):
                val1 = val1*nums[j]
            for k in nums[:i]:
                val2 = val2 * k
            final_arr.append(val1 * val2)
        return final_arr

        