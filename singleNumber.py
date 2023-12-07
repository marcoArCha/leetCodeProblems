# 136.Given a non-empty array of integers nums, every element appears twice 
# except for one. Find that single one.
#You must implement a solution with a linear runtime 
# complexity and use only constant extra space.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        Set = set()
        for element in nums:
            if element not in Set:
                Set.add(element)
            else:
                Set.remove(element)
        single = Set.pop()
        return single