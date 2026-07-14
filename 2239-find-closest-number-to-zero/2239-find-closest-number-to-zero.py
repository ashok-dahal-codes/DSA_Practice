class Solution(object):
    def findClosestNumber(self, nums):
        #assume the answer is the first element
        ans = nums[0]
        for num in nums:
            if abs(num) < abs (ans):
                ans = num
            elif abs(num) == abs(ans):
                if num > ans:
                    ans = num
        return ans 
        
        