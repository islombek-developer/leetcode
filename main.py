class Solution:
    def twoSum(self, nums, target: int) :
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]

        return []

salom=Solution()
d=salom.twoSum([2,7,11,15],9)
print(d)
