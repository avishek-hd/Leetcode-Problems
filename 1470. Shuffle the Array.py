#1470. Shuffle the Array

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res=[]
        for i,j in zip(nums[:n], nums[n:]):
            res.append(i)
            res.append(j)
        return res