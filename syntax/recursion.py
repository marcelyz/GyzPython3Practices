# 递归(recursion)


class BinaryTree:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


# 二叉树的递归遍历
def preorder(root):
    # 先序遍历
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)


def inorder(root):
    # 中序遍历
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


def postorder(root):
    # 后序遍历
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)

# 栈遍历


def list_sum(nums):
    # 递归求数组的和
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + list_sum(nums[1:])


if __name__ == "__main__":
    print(list_sum([1, 3, 5, 7, 9]))

    root_test = BinaryTree(1)
    root_test.left = BinaryTree(2)
    root_test.right = BinaryTree(3)
    root_test.left.left = BinaryTree(4)
    root_test.left.right = BinaryTree(5)
    print("Preorder traversal of binary tree is")
    preorder(root_test)

    print("Inorder traversal of binary tree is")
    inorder(root_test)

    print("Postorder traversal of binary tree is")
    postorder(root_test)