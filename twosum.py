class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_occur = {}
        for idx,num in enumerate(nums):
            diff = target - num
            if diff in prev_occur:
                return [prev_occur[diff],idx]
            else:
                prev_occur[num] = idx
        return []

    

sol = Solution()
print(sol.twoSum([1,4,6,9]))