'''
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous sub-array whose length is equal to k that has the maximum average value and return this value. 
Any answer with a calculation error less than 10-5 will be accepted.
'''

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        currSum = maxSum = sum(nums[:k])

        for i in range (k, len(nums)):
            currSum += nums[i] - nums[i - k]
            maxSum = max(maxSum, currSum)

        return maxSum / k
    
