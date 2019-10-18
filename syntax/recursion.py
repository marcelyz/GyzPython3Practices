# 递归(recursion)

def list_sum(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + list_sum(nums[1:])

print(list_sum([1,3,5,7,9]))