
#349. Intersection of Two Arrays

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        list=[]
        nums1=set(nums1)
        
        for i in nums2:
            if i in nums1:
                list.append(i)
                nums1.remove(i)
        return list
