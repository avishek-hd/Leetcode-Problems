#2798. Number of Employees Who Met the Target
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        n=0
        for i in hours:
            if i>=target:
                n+=1
        return n