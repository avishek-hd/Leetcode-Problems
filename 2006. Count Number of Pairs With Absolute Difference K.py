#2006. Count Number of Pairs With Absolute Difference K

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        n=len(nums)
        c=0
        for i in range(n-1):
            for j in range(i+1,n):
                if abs(nums[j]-nums[i])==k:
                    c+=1
        return c