#1281. Subtract the Product and Sum of Digits of an Integer

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mul=1
        sum=0
        while(n>0):
            x= n%10
            mul*=x
            sum+=x
            n=n//10
        return mul-sum