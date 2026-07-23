class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in range(len(nums)):
            if nums[num] not in d:
                d[nums[num]] = 1
            else:
                d[nums[num]] += 1

        sorted_arr = list(sorted(d.items() , key = lambda x : x[1] , reverse = True))
        final_arr = []
        for key , value in sorted_arr[:k]:
            final_arr.append(key)
        return final_arr
            