class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = nums[0]  # Initialize curSum with the first element of the array

        for n in nums[1:]:  # Start the loop from the second element
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub