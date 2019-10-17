# 递归(recursion)

def list_sum(nums_list):
    if len(nums_list) == 1:
        return nums_list[0]
    else:
        return nums_list[0] + nums_list[1:]