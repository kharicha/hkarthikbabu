#Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
#Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

nums = [1,1,2] >>> 2
nums = [0,0,1,1,1,2,2,3,3,4] >>> 5

def remove_duplicates(nums):
    i = 0
    while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            del nums[i]
        else:
            i += 1
    return len(nums)



print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]))

def remove_duplicates(nums):
    nums = set(nums)
    return len(nums)
print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]))
