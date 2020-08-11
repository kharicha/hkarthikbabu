
#Given an array of integers, find if the array contains any duplicates.
# Example 1:
# Input: [1,2,3,1]
# Output: true
#
# Example 2:
# Input: [1,2,3,4]
# Output: false

class Solution:
    def containsDuplicate(
        self, nums: List[int]
    ) -> bool:
        return len(set(nums)) < len(nums)

containsDuplicate([1,2,3,1])