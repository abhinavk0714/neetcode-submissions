class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # first sort the array O(nlogn) time complexity
        res = [] # init result array to be returned

        for i, a in enumerate(nums):

            if i > 0 and a == nums[i - 1]: # checks for duplicate values
                continue

            l, r = i + 1, len(nums) - 1 # init pointers
            while l < r:
                threeSum = a + nums[l] + nums[r] # check if threeSum gives 0
                if threeSum > 0: # if greater than 0, move right pointer left
                    r -= 1
                elif threeSum < 0: # if less than 0, move left pointer right
                    l += 1
                else: # if equal to zero, add the 3 indexes that give us the solution to res
                    res.append([a, nums[l], nums[r]])
                    l += 1 # only need to update left pointer
                    while nums[l] == nums[l - 1] and l < r: # only need to update left pointer since
                        l += 1                              # the recursion updates the other ones
        
        return res
