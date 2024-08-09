#3099. Harshad Number

class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        res=0
        div=x
        while(x!=0):
            remainder=x%10
            res+=remainder
            x=x//10
        if div%res==0:
            return res
        else:
            return -1
