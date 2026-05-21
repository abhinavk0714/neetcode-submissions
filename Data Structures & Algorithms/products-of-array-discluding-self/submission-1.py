class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len((nums)) # create an array of 1s the size of the given array

        prefix = 1 # start at 1 for edge cases of array
        for i in range(len(nums)): # start at front of array, assign prefix values
            res[i] = prefix # compute prefixes as we iterate through the array
            prefix *= nums[i]

        postfix = 1 # start at 1 for edge cases of array
        for i in range(len(nums) - 1, -1, -1): # start at end of array to the front
            res[i] *= postfix # mulitply postfix val onto prefix val already in array
            postfix *= nums[i]

        return res