class LinkedNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None

    def __repr__(self):
        result = ""
        node = self
        while node:
            result += str(node.val)
            node = node.next
            if node:
                result += " -> "
        return result


class LinkedList(LinkedNode):
    # 从list创建linked list
    @classmethod
    def from_list(cls, lst: list):
        linked_list_head = None
        for i in range(len(lst)-1, -1, -1):
            node = cls(lst[i])
            node.next = linked_list_head
            linked_list_head = node
        return linked_list_head

    # 从list创建linked loop list
    @classmethod
    def from_loop_list(cls, lst: list, cycle_index: int):
        linked_cycle_list_head = None
        loop_node_head = None
        last_node = None
        for i in range(len(lst)-1, -1, -1):
            node = cls(lst[i])
            if i == len(lst)-1:
                last_node = node
            node.next = linked_cycle_list_head
            linked_cycle_list_head = node
            if i == cycle_index:
                loop_node_head = linked_cycle_list_head
        last_node.next = loop_node_head
        return linked_cycle_list_head

    # 链表反转(循环+变量交换)
    @staticmethod
    def reverse_linked_list(p_head: LinkedNode):
        if not p_head or not p_head.next:
            return p_head
        reverse_p_head = None
        while p_head:
            next_node = p_head.next
            p_head.next = reverse_p_head
            reverse_p_head = p_head
            p_head = next_node
        return reverse_p_head

    # 合并两个有序链表(非递归)
    @staticmethod
    def merge_2_linked_list(p_head1: LinkedNode, p_head2: LinkedNode):
        result_p_head = moved_p = LinkedNode(-1)  # 初始化一个-1的链表节点；且申明2个指针，一个用来移动比较，一个用来返回最终的结果
        while p_head1 and p_head2:
            if p_head1.val > p_head2.val:
                moved_p.next = p_head2
                p_head2 = p_head2.next
            else:
                moved_p.next = p_head1
                p_head1 = p_head1.next
            moved_p = moved_p.next
        if p_head1:
            moved_p.next = p_head1
        if p_head2:
            moved_p.next = p_head2
        return result_p_head.next

    # 判断链表是否有环；如果有，返回环的长度(快慢指针)
    @staticmethod
    def detect_loop(p_head: LinkedNode):
        if p_head is None or p_head.next is None:
            return 0
        slow = p_head.next
        fast = p_head.next.next
        while slow and slow.next and fast and fast.next and fast.next.next:
            if slow == fast:
                count = 1
                slow = slow.next
                while slow != fast:
                    count += 1
                    slow = slow.next
                return count
            slow = slow.next
            fast = fast.next.next
        return 0


class Solution:
    # 大数加法(循环+进位)
    @staticmethod
    def big_num_add(big_num1: str, big_num2: str):
        if len(big_num1) < len(big_num2):
            big_num1, big_num2 = big_num2, big_num1
        n1 = len(big_num1)
        n2 = len(big_num2)
        diff = n1 - n2
        result = ""
        carry = 0
        # 列竖式计算过程
        for i in range(n2-1, -1, -1):
            n_sum = int(big_num1[i+diff]) + int(big_num2[i]) + carry
            carry = n_sum // 10
            result += str(n_sum % 10)
        for i in range(n1-n2-1, -1, -1):
            n_sum = int(big_num1[i]) + carry
            carry = n_sum // 10
            result += str(n_sum % 10)
        if carry:
            result += str(carry)
        return result[::-1]

    # 快速排序(分治+递归)
    @staticmethod
    def partition(nums_list: list, lo: int, hi: int):
        threshold = lo - 1
        pivot = nums_list[hi-1]
        for i in range(lo, hi):
            if nums_list[i] < pivot:
                threshold += 1
                nums_list[i], nums_list[threshold] = nums_list[threshold], nums_list[i]
        nums_list[threshold+1], nums_list[hi-1] = nums_list[hi-1], nums_list[threshold+1]
        return threshold+1

    def quick_sort(self, nums_list: list, lo: int, hi: int):
        if lo < hi:
            pivot = self.partition(nums_list, lo, hi)
            self.quick_sort(nums_list, lo, pivot)
            self.quick_sort(nums_list, pivot+1, hi)
            return

    # 第k大数(类快排思想)
    def find_k_max(self, num_list: list, lo: int, hi: int, k: int):
        pivot = self.partition(num_list, lo, hi)
        if pivot < k-1:
            return self.find_k_max(num_list, pivot, hi, k)  # 注意加return !!!
        elif pivot > k-1:
            return self.find_k_max(num_list, lo, pivot, k)  # 注意加return !!!
        else:
            return num_list[pivot]

    # todo: 第k大数(类堆排序思想)
    def find_k_max_heap(self, num_list: list, lo: int, hi: int, k: int):
        pass


if __name__ == "__main__":
    solution = Solution()

    # 大数加法
    # print(solution.big_num_add("12345", "987654321"))

    # 快排
    # nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    # solution.quick_sort(nums, 0, len(nums))
    # print(nums)

    # # 第k大数
    # nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    # print(solution.find_k_max(nums, 0, len(nums), 6))

    # 链表反转
    # a = LinkedList.from_list([3, 4, 5, 6, 7])
    # print(a)
    # b = LinkedList.reverse_linked_list(a)
    # print(b)

    # 合并两个有序链表
    # a = LinkedList.from_list([1, 3, 5, 7, 9])
    # b = LinkedList.from_list([2, 4, 6, 8, 10])
    # print(LinkedList.merge_2_linked_list(a, b))

    # 判断链表是否有环；如果有，返回环的长度
    a = LinkedList.from_loop_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 5)
    for i in range(13):  # 打印有环链表
        print(a.val)
        a = a.next
    print("链表的环的长度为", LinkedList.detect_loop(a))