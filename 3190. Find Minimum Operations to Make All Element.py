#3190. Find Minimum Operations to Make All Elements Divisible by Three

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        oper=0
        for i in nums:
            if(i%3==0):
                continue
            else:
                oper+=1
        
        return oper
