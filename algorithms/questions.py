import copy
class Solution:
    def quick_sort(self,nums,lo,hi):
        """
        :param nums:list[int]
        :param lo: int, low,0
        :param hi: int, high,len(nums)
        :return:
        分治和递归
        """
        if lo < hi:
            p = self.partition(nums,lo,hi)
            self.quick_sort(nums,lo,p)
            self.quick_sort(nums,p+1,hi)
            return
    def partition(self,nums,lo,hi):
        """
        :param nums:list
        :param lo: int, low
        :param hi: int, high
        :return: int, pivot_index
        """
        i = lo - 1
        pivot = nums[hi-1]
        for j in range(lo,hi):
            if nums[j] < pivot:
                i += 1
                nums[i],nums[j] = nums[j],nums[i]
        nums[i+1],nums[hi-1] = nums[hi-1],nums[i+1]
        return i+1

    def merge_sort(self,nums):
        """
        :param nums: list[int]
        :return: list[int]
        分治和递归
        """
        length = len(nums)
        if length == 0 or length == 1:
            return nums
        else:
            middle = length // 2
            left = self.merge_sort(nums[:middle])
            right = self.merge_sort(nums[middle:])
            return self.merged(left,right)
    def merged(self,left,right):
        """
        :param left: list[int]
        :param right: list[int]
        :return: list[int]
        """
        merged = []
        while left and right:
            if left[0] < right[0]:
                min_num = left.pop(0)
            else:
                min_num = right.pop(0)
            merged.append(min_num)
        merged.extend(left)
        merged.extend(right)
        return merged

    def max_sub_array(self,nums):
        """
        :param nums:List[int]
        :return: int, List[int]
        在线处理:O(n)
        """
        length = len(nums)
        if length == 1 or length == 0:
            return sum(nums), nums
        else:
            max_sum = 0;this_sum = 0
            max_sum_array = [];this_sum_array = []
            for i in range(length):
                this_sum += nums[i]
                this_sum_array.append(nums[i])
                if this_sum > max_sum:
                    max_sum = this_sum
                    max_sum_array = copy.deepcopy(this_sum_array)#要用深拷贝，不然maxArray会随着thisArray的变化而变化
                elif this_sum < 0:
                    this_sum = 0
                    this_sum_array = []
                else:
                    continue
        if max_sum == 0:#如果数组里全是负数和0的话，是另外一种做法
            return max(nums), [max(nums)]
        else:
            return max_sum,max_sum_array

    def find_median_sorted_arrays(self, nums1, nums2):
        """
        :type nums1,nums2: List[int]
        :rtype: int/float
        二分法：O(log(min(m,n)))
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            raise ValueError
        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and nums2[j - 1] > nums1[i]:
                # i 的值太小， 增加它
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                # i 的值过大， 减小它
                imax = i - 1
            else:
                # i 的值正合适
                if i == 0:
                    max_of_left = nums2[j - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])
                if (m + n) % 2 == 1:
                    return max_of_left
                if i == m:
                    min_of_right = nums2[j]
                else:
                    min_of_right = min(nums1[i], nums2[j])
                return (max_of_left + min_of_right) / 2.0

    def find_seconde_max_num(self, nums):
        if len(nums) < 2:
            return None
        if nums[0] < nums[1]:
            max_num = nums[1]
            second_max_num = nums[0]
        else:
            max_num = nums[0]
            second_max_num = nums[1]
        if len(nums) == 2:
            return second_max_num
        else:
            for num in nums[2:]:
                if num > max_num:
                    second_max_num = max_num
                    max_num = num
                elif num > second_max_num:
                    second_max_num = num
                else:
                    continue
        return second_max_num

    def house_rob(self, nums):
        rob, no_rob, rob1, no_rob1 = 0, 0, 0, 0
        for num in nums:
            rob1 = num + no_rob
            no_rob1 = max(no_rob, rob)
            rob, no_rob = rob1, no_rob1
        return max(rob, no_rob)

    def two_sum(self, nums, target):
        result = []
        nums_index_dict = {}
        for i in range(len(nums)):
            if target-nums[i] in nums_index_dict:
                result.append((target-nums[i], nums[i]))
            nums_index_dict[nums[i]] = i
        return result

# nums = [-2,1,-3,4,-1,2,1,-5,4]
# print(Solution().max_sub_array(nums))

# Solution().quick_sort(nums,0,len(nums))
# print(nums)

# print(Solution().merge_sort(nums))

nums1 = [0,1, 2, 3]
nums2 = [4,5,6,7,8,9]
result = Solution().find_median_sorted_arrays(nums1,nums2)
print(result)

# nums = [1,2,3,4,5,-1]
# result = Solution().find_seconde_max_num(nums)
# print(result)

# nums = [1,2,3,4,5,-1]
# result = Solution().house_rob(nums)
# print(result)

# nums = [1,2,3,4,5,-1]
# result = Solution().two_sum(nums,5)
# print(result)