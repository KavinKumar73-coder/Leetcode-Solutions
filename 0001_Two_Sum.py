class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j]==target:
                    return [i,j]

                  
                  
                  
# time complexity :O(n2)
# space complextiy :O(1)
