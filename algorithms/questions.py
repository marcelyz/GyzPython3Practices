import copy
import random


class Solution:
    def quick_sort(self, nums, lo, hi):
        """
        :param nums:list[int]
        :param lo: int, low,0
        :param hi: int, high,len(nums)
        :return:
        分治和递归
        """
        if lo < hi:
            p = self.partition(nums, lo, hi)
            self.quick_sort(nums, lo, p)
            self.quick_sort(nums, p+1, hi)
            return

    @staticmethod
    def partition(nums, lo, hi):
        """
        :param nums:list
        :param lo: int, low
        :param hi: int, high
        :return: int, pivot_index
        """
        i = lo - 1
        pivot = nums[hi-1]
        for j in range(lo, hi):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1], nums[hi-1] = nums[hi-1], nums[i+1]
        return i+1

    def merge_sort(self, nums):
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
            return self.merged(left, right)

    @staticmethod
    def merged(left, right):
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

    @staticmethod
    def max_sub_array(nums):
        """
        :param nums:List[int]
        :return: int, List[int]
        在线处理:O(n)
        """
        length = len(nums)
        if length == 1 or length == 0:
            return sum(nums), nums
        else:
            max_sum = 0
            this_sum = 0
            max_sum_array = []
            this_sum_array = []
            for i in range(length):
                this_sum += nums[i]
                this_sum_array.append(nums[i])
                if this_sum > max_sum:
                    max_sum = this_sum
                    max_sum_array = copy.deepcopy(this_sum_array)  # 要用深拷贝，不然maxArray会随着thisArray的变化而变化
                elif this_sum < 0:
                    this_sum = 0
                    this_sum_array = []
                else:
                    continue
        if max_sum == 0:  # 如果数组里全是负数和0的话，是另外一种做法
            return max(nums), [max(nums)]
        else:
            return max_sum, max_sum_array

    @staticmethod
    def find_median_sorted_arrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
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

    @staticmethod
    def find_second_max_num(nums):
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

    @staticmethod
    def house_rob(nums):
        rob, no_rob, rob1, no_rob1 = 0, 0, 0, 0
        for num in nums:
            rob1 = num + no_rob
            no_rob1 = max(no_rob, rob)
            rob, no_rob = rob1, no_rob1
        return max(rob, no_rob)

    @staticmethod
    def two_sum(nums, target):
        t_result = []
        nums_index_dict = {}
        for i in range(len(nums)):
            if target-nums[i] in nums_index_dict:
                t_result.append((target-nums[i], nums[i]))
            nums_index_dict[nums[i]] = i
        return t_result

    @staticmethod
    def find_nums_min_and_max(nums):  # O(1.5N)
        """
        :param nums: list(int)
        :return: list(min, max)
        双元素法: 1.5N次比较
        """
        size = len(nums)
        if size == 0:
            return list()
        elif size == 1:
            return [nums[0], nums[0]]
        elif size == 2:
            return [nums[0], nums[1]] if nums[0] < nums[1] else [nums[1], nums[0]]
        else:
            t_max = t_min = nums[0]
            i = 1
            j = size - 1
            while i <= j:
                if nums[i] > nums[j]:
                    if nums[i] > t_max:
                        t_max = nums[i]
                    if nums[j] < t_min:
                        t_min = nums[j]
                    i += 1
                    j -= 1
                else:
                    if nums[i] < t_min:
                        t_min = nums[i]
                    if nums[j] > t_max:
                        t_max = nums[j]
                    i += 1
                    j -= 1
            return [t_min, t_max]

    @staticmethod
    def stock_max_profit(prices):
        """
        :param prices:[(date,price),(),()...]
        :return: [buy_date, sell_date, max_profit]
        """
        size = len(prices)
        if size == 0:
            return list()
        elif size == 1:
            return [prices[0][0], prices[0][0], prices[0][1]]
        else:
            min_price = prices[0][1]
            min_date = prices[0][0]
            max_profit = 0
            buy_date = prices[0][0]
            sell_date = prices[0][0]
            for data in prices[1:]:
                if data[1] - min_price > max_profit:
                    max_profit = data[1] - min_price
                    buy_date = min_date
                    sell_date = data[0]
                if data[1] < min_price:
                    min_price = data[1]
                    min_date = data[0]
            return [buy_date, sell_date, max_profit]

    # todo 不完善
    @staticmethod
    def min_window(s_string, t_string):
        if t_string not in s_string:
            assert t_string not in s_string
        else:
            left = 0
            right = len(s_string)
            while left < right:
                if t_string in s_string[left+1:right]:
                    left += 1
                if t_string in s_string[left:right-1]:
                    right -= 1
            return s_string[left:right]

    @staticmethod
    def is_binary_search_tree(root):
        pass


if __name__ == "__main__":
    nums_test1 = random.sample(range(-5, 5), 10)
    nums_test2 = random.sample(range(-5, 5), 8)
    print("nums_test1:", nums_test1)
    print("nums_test2:", nums_test2)

    # 最大子列和
    # print("max_sub_array:", Solution().max_sub_array(nums_test1))
    #
    # 快速排序
    # Solution().quick_sort(nums_test1, 0, len(nums_test1))
    # print("quick_sort:", nums_test1)
    #
    # 归并排序
    # print("merge_sort:", Solution().merge_sort(nums_test1))
    #
    # 两个有序数组的中位数
    # num_median = Solution().find_median_sorted_arrays(nums_test1, nums_test2)
    # print("median of two sorted arrays:", num_median)
    #
    # 数组中第二大的数
    # num_second_max = Solution().find_second_max_num(nums_test1)
    # print("num_second_max", num_second_max)
    #
    # 抢房子
    # house_rob_result = Solution().house_rob(nums_test1)
    # print("house_rob_result", house_rob_result)
    #
    # two sum
    # target_sum = 5
    # two_sum_result = Solution().two_sum(nums_test1, target_sum)
    # print("two_sum_result", two_sum_result)

    # 数组中的最大值最小值，1.5N次比较(新氧)
    # min_max = Solution().find_nums_min_and_max(nums_test1)
    # print("find_nums_min_and_max:", min_max)

    # 股票利益最大化问题(新氧)
    # stocks = [("2019-07-01", 1), ("2019-07-02", 3), ("2019-07-04", 5), ("2019-07-05", 1), ("2019-07-09", 10)]
    # print(Solution().stock_max_profit(stocks))

    # 最小覆盖子串（双指针+滑动窗口）
    S = "ADOBECODEBANC"
    T = "ABC"
    print(Solution().min_window(S, T))

    # 二叉搜索树(zhihu)
    pass

