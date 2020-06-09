from typing import List


class Solution:
    # 大数加法(循环+进位)
    @staticmethod
    def big_num_add(big_num1: str, big_num2: str) -> str:
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
    def partition(nums_list: list, lo: int, hi: int) -> int:
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
        if pivot == k-1:
            return num_list[pivot]
        elif pivot < k-1:
            return self.find_k_max(num_list, pivot, hi, k)  # 注意加return !!!
        else:
            return self.find_k_max(num_list, lo, pivot, k)  # 注意加return !!!

    # todo: 第k大数(最小堆)
    def find_k_max_using_min_heap(self, num_list: list, lo: int, hi: int, k: int):
        pass


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
            if len(result) > 100:  # 防止有环链表导致死循环
                break
            if node:
                result += " -> "
        return result


class LinkedList(LinkedNode):
    # 从list创建linked list
    @classmethod
    def from_list(cls, lst: list) -> LinkedNode:
        linked_list_head = None
        for i in range(len(lst)-1, -1, -1):
            node = cls(lst[i])
            node.next = linked_list_head
            linked_list_head = node
        return linked_list_head

    # 从list创建linked loop list
    @classmethod
    def from_loop_list(cls, lst: list, cycle_index: int) -> LinkedNode:
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
    def reverse_linked_list(l_head: LinkedNode) -> LinkedNode:
        if not l_head or not l_head.next:
            return l_head
        reverse_l_head = None
        while l_head:
            next_node = l_head.next
            l_head.next = reverse_l_head
            reverse_l_head = l_head
            l_head = next_node
        return reverse_l_head

    # 合并两个有序链表(非递归)
    @staticmethod
    def merge_2_linked_list(l_head1: LinkedNode, l_head2: LinkedNode) -> LinkedNode:
        result_l_head = moved_p = LinkedNode(-1)  # 初始化一个-1的链表节点；且申明2个指针，一个用来移动比较，一个用来返回最终的结果
        while l_head1 and l_head2:
            if l_head1.val > l_head2.val:
                moved_p.next = l_head2
                l_head2 = l_head2.next
            else:
                moved_p.next = l_head1
                l_head1 = l_head1.next
            moved_p = moved_p.next
        if l_head1:
            moved_p.next = l_head1
        if l_head2:
            moved_p.next = l_head2
        return result_l_head.next

    # 合并两个有序链表(递归)
    @staticmethod
    def merge_2_linked_list_recursion(l_head1: LinkedNode, l_head2: LinkedNode) -> LinkedNode:
        if l_head1 is None:
            return l_head2
        if l_head2 is None:
            return l_head1
        if l_head1.val < l_head2.val:
            result_l_head = l_head1
            result_l_head.next = LinkedList.merge_2_linked_list_recursion(l_head1.next, l_head2)
        else:
            result_l_head = l_head2
            result_l_head.next = LinkedList.merge_2_linked_list_recursion(l_head1, l_head2.next)
        return result_l_head

    # 合并k个有序链表(类归并思想)
    @staticmethod
    def merge_k_linked_list(l_head_list: List[LinkedNode]) -> LinkedNode:
        length = len(l_head_list)
        if length == 0:
            assert "input error"
        if length == 1:
            return l_head_list[0]
        middle = length // 2
        left = LinkedList.merge_k_linked_list(l_head_list[:middle])
        right = LinkedList.merge_k_linked_list(l_head_list[middle:])
        return LinkedList.merge_2_linked_list(left, right)

    # todo 合并k个有序链表(最小堆)
    @staticmethod
    def merge_k_linked_list_using_min_heap(l_head_list: List[LinkedNode]) -> LinkedNode:
        pass

    # 判断链表是否有环；如果有，返回环的长度(快慢指针)
    @staticmethod
    def detect_loop(l_head: LinkedNode) -> int:
        if l_head is None or l_head.next is None:
            return 0
        slow = l_head.next
        fast = l_head.next.next
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


class BinaryTree:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

    # 二叉树z型遍历(双栈法)
    @staticmethod
    def zigzag_traversal(t_head):
        ltr_flag = True  # the flag of left to right
        current_stack = [t_head]
        next_stack = []
        while len(current_stack) > 0:
            node = current_stack.pop()
            print(node.val, end=" ")
            if ltr_flag:
                if node.left:
                    next_stack.append(node.left)
                if node.right:
                    next_stack.append(node.right)
            else:
                if node.right:
                    next_stack.append(node.right)
                if node.left:
                    next_stack.append(node.left)
            if len(current_stack) == 0:
                ltr_flag = not ltr_flag
                next_stack, current_stack = current_stack, next_stack

    # 二叉树最大深度(递归)
    @staticmethod
    def max_tree_depth(t_head):
        if t_head is None:
            return 0
        left_depth = BinaryTree.max_tree_depth(t_head.left)
        right_depth = BinaryTree.max_tree_depth(t_head.right)
        if left_depth > right_depth:
            return left_depth + 1
        else:
            return right_depth + 1

    # 二叉树最小深度(递归)
    @staticmethod
    def min_tree_depth(t_head):
        if t_head is None:
            return 0
        left_depth = BinaryTree.min_tree_depth(t_head.left)
        right_depth = BinaryTree.min_tree_depth(t_head.right)
        if left_depth > right_depth:
            return right_depth + 1
        else:
            return left_depth + 1

    # 是否是二叉搜索树(递归)
    @staticmethod
    def is_binary_search_tree(t_head):
        if t_head is None:
            return True
        if t_head.val > t_head.left.val:
            return False
        if t_head.val < t_head.right.val:
            return False
        return BinaryTree.is_binary_search_tree(t_head.left) and BinaryTree.is_binary_search_tree(t_head.right)

    # 是否是相同的树(递归)
    @staticmethod
    def is_same_tree(t_head1, t_head2):
        if t_head1 is None or t_head2 is None:
            return t_head1 is None and t_head2 is None
        if t_head1.val != t_head2.val:
            return False
        return BinaryTree.is_same_tree(t_head1.left, t_head2.left) and BinaryTree.is_same_tree(t_head1.right,
                                                                                               t_head2.right)

    # 子树结构: t_head1是否是t_head2的子树(递归)
    @staticmethod
    def is_sub_tree(t_head1, t_head2):
        if t_head1 is None or t_head2 is None:
            return t_head1 is None and t_head2 is None
        if BinaryTree.is_same_tree(t_head1, t_head2):
            return True
        return BinaryTree.is_sub_tree(t_head1, t_head2.left) or BinaryTree.is_sub_tree(t_head1, t_head2.right)


if __name__ == "__main__":
    solution = Solution()

    print("大数加法")
    a = "12345"
    b = "987654321"
    print("{0} + {1} = {2}".format(a, b, solution.big_num_add(a, b)))
    print("-"*100)

    print("快排")
    nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("origin: ", nums)
    solution.quick_sort(nums, 0, len(nums))
    print("sorted", nums)
    print("-" * 100)

    print("第k大数")
    nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("origin: ", nums)
    k = 6
    print("the {0}th max number".format(k), solution.find_k_max(nums, 0, len(nums), k))
    print("-" * 100)

    # ====================================== 链表相关 ======================================
    print("链表反转")
    a = LinkedList.from_list([3, 4, 5, 6, 7])
    print("origin: ", a)
    b = LinkedList.reverse_linked_list(a)
    print("reversed: ", b)
    print("-" * 100)

    print("合并两个有序链表")
    a = LinkedList.from_list([1, 3, 5, 7, 9])
    b = LinkedList.from_list([2, 4, 6, 8, 10])
    print("linked_list a: ", a)
    print("linked_list b: ", b)
    print("非递归合并", LinkedList.merge_2_linked_list(a, b))
    a = LinkedList.from_list([1, 3, 5, 7, 9])
    b = LinkedList.from_list([2, 4, 6, 8, 10])
    print("递归版合并", LinkedList.merge_2_linked_list_recursion(a, b))
    print("-" * 100)

    print("合并k个有序链表")
    a = LinkedList.from_list([1, 3, 5, 7, 9])
    b = LinkedList.from_list([2, 4, 6, 8, 10])
    c = LinkedList.from_list([0, 3, 6, 9, 110])
    print("linked_list a: ", a)
    print("linked_list b: ", b)
    print("linked_list c: ", c)
    abc = [a, b, c]
    print("归并版合并：", LinkedList.merge_k_linked_list(abc))
    print("-" * 100)

    print("判断链表是否有环；如果有，返回环的长度")
    a = LinkedList.from_loop_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 5)
    print("linked_list a: ", a)
    print("链表的环的长度为", LinkedList.detect_loop(a))
    print("-" * 100)

    # ====================================== 树相关 ======================================
    t = BinaryTree(1)
    t.left = BinaryTree(2)
    t.right = BinaryTree(3)
    t.left.left = BinaryTree(4)
    t.left.right = BinaryTree(5)

    print("二叉树z型遍历")
    BinaryTree.zigzag_traversal(t)
    print()
    print("-" * 100)

    print("二叉树最大深度")
    print(BinaryTree.max_tree_depth(t))
    print("-" * 100)

    print("二叉树最小深度")
    print(BinaryTree.min_tree_depth(t))
    print("-" * 100)

    print("是否是二叉搜索树")
    print(BinaryTree.is_binary_search_tree(t))
    print("-" * 100)

    t2 = BinaryTree(-1)
    t2.left = BinaryTree(0)
    t2.right = t

    print("t 是否是 t2 的子树结构")
    print(BinaryTree.is_sub_tree(t, t2))
    print("-" * 100)
