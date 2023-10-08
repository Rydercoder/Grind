
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero_index = 0

        # Iterate through the list and move non-zero elements to the front.
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[non_zero_index] = nums[non_zero_index], nums[i]
                non_zero_index += 1


               