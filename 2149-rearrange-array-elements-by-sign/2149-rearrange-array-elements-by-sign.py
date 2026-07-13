class Solution(object):
    def rearrangeArray(self, nums):
        n = len(nums)
        result = [0] * n
        PosIndex, NegIndex = [0,1]
        for i in range(0,n):
            if nums[i] >= 0:
                result[PosIndex] = nums[i]
                PosIndex += 2
            else:
                result[NegIndex] = nums[i]
                NegIndex += 2
        return result
