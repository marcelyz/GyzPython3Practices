# 递归(recursion)


class BinaryTree:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


# 二叉树的递归遍历
def preorder_recursion(root):  # 先序遍历
    if root:
        print(root.val)
        preorder_recursion(root.left)
        preorder_recursion(root.right)


def inorder_recursion(root):  # 中序遍历
    if root:
        inorder_recursion(root.left)
        print(root.val)
        inorder_recursion(root.right)


def postorder_recursion(root):  # 后序遍历
    if root:
        postorder_recursion(root.left)
        postorder_recursion(root.right)
        print(root.val)


# 二叉树的栈遍历
def preorder_stack(root):
    node_stack = [root]
    while len(node_stack) > 0:
        node = node_stack.pop()
        if node is not None:
            print(node.val)
        if node.right is not None:
            node_stack.append(node.right)
        if node.left is not None:
            node_stack.append(node.left)


def inorder_stack(root):
    node_stack = []
    node = root
    while True:
        if node is not None:
            node_stack.append(node)
            node = node.left
        elif node_stack:
            node = node_stack.pop()
            print(node.val)
            node = node.right
        else:
            break


def postorder_stack(root):
    def peek(stack):
        if len(stack) > 0:
            return stack[-1]
        return None
    node_stack = []
    while True:
        while root:
            if root.right is not None:
                node_stack.append(root.right)
            node_stack.append(root)
            root = root.left
        root = node_stack.pop()
        if root.right is not None and peek(node_stack) == root.right:
            node_stack.pop()
            node_stack.append(root)
            root = root.right
        else:
            print(root.val)
            root = None
        if len(node_stack) <= 0:
            break


def list_sum(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + list_sum(nums[1:])


if __name__ == "__main__":
    # 递归求数组的和
    print(list_sum([1, 3, 5, 7, 9]))

    # 二叉树的递归遍历
    root_test = BinaryTree(1)
    root_test.left = BinaryTree(2)
    root_test.right = BinaryTree(3)
    root_test.left.left = BinaryTree(4)
    root_test.left.right = BinaryTree(5)
    print("preorder_recursion traversal of binary tree is")
    preorder_recursion(root_test)
    print("inorder_recursion traversal of binary tree is")
    inorder_recursion(root_test)
    print("postorder_recursion traversal of binary tree is")
    postorder_recursion(root_test)
    # 二叉树的栈遍历
    print("preorder_stack traversal of binary tree is")
    preorder_stack(root_test)
    print("inorder_stack traversal of binary tree is")
    inorder_stack(root_test)
    print("postorder_stack traversal of binary tree is")
    postorder_stack(root_test)

