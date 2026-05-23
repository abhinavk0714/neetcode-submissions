class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        # init prefix hashmap with 0 subarray mapped to 1 count
        prefixSums = {0:1}
        
        for n in nums:
            # add n to curSum
            curSum += n
            # find diff 
            diff = curSum - k

            # if this diff exists in our hashmap, add to res
            res += prefixSums.get(diff, 0)
            # update hashmap with counts of prefixSums
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)

        return res
