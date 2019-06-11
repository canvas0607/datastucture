class Node:
    def __init__(self, value=None, l=None, r=None, left=None, right=None):
        self.value = value
        self.l = l
        self.r = r
        self.left = left
        self.right = right


class NumArray:
    def __init__(self, nums):
        self.data = nums

        def gen_tree(l, r):
            if l == r:
                return Node(value=self.data[l], l=l, r=r)
            node = Node(l=l, r=r)
            mid = self._mid(l, r)
            left_child = gen_tree(l, mid)
            right_child = gen_tree(mid + 1, r)
            node.left = left_child
            node.right = right_child
            node.value = left_child.value + right_child.value
            return node

        self.root = gen_tree(0, (len(self.data) - 1))
        # def _gen_tree(self, l, r):
        #     if l == r:
        #         return Node(value=self.data[l], l=l, r=r)
        #     node = Node(l=l, r=r)
        #     mid = self._mid(l, r)
        #     left_child = self._gen_tree(l, mid)
        #     right_child = self._gen_tree(mid + 1, r)
        #     node.left = left_child
        #     node.right = right_child
        #     node.value = self._merge(node.left, node.right)
        #     return node

    def _merge(self, left, right):
        return left.value + right.value

    def _mid(self, l, r):
        """
        计算mid值
        :param l:
        :param r:
        :return:
        """
        return (l + r) // 2

    def update(self, i, val):
        """
        数据的更新操作
        :param index:
        :param value:
        :return:
        """
        self.data[i] = val
        self.root = self._update(self.root, i)

    def _update(self, node, index):
        """
        更新区域内的一个值
        :param node:
        :param index:
        :param value:
        :return:
        """
        if node.l == node.r == index:
            node.value = self.data[index]
            return node

        mid = self._mid(node.l, node.r)

        # 在左边去更新
        if index <= mid:
            node.left = self._update(node.left, index)
        else:
            node.right = self._update(node.right, index)

        node.value = self._merge(node.left, node.right)
        return node

    def sumRange(self, i, j):
        return self._find(self.root, i, j)

    def _find(self, node, i, j):
        """
        如果node的区间和i,j相等 则直接返回值
        :param node:
        :param i:
        :param j:
        :return:
        """
        if node.l == i and node.r == j:
            return node.value

        mid = self._mid(node.l, node.r)

        if mid >= i:
            """
            去左边查找
            """
            return self._find(node.left, i, j)
        elif mid < i:
            return self._find(node.right, i, j)
        else:

            left = self._find(node.left, i, mid)
            right = self._find(node.right, mid + 1, j)
            return left + right