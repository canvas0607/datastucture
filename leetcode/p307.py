class SegmentTree:
    """
    data是用于存放数据的
    tree是用于存储要查询的业务的线段树
    """

    def __init__(self, data):
        self.data = data
        self.tree = [None for _ in range(len(self.data) * 4)]
        self.build_tree()

    def get_size(self):
        return len(self.data)

    def build_tree(self):
        self._build_tree(0, 0, len(self.data) - 1)

    def find(self, l, r):
        """
        判断边界范围
        :param l:
        :param r:
        :return:
        """
        if l < 0:
            raise IndexError('边界不能为0')
        if l > r:
            raise IndexError('左边界不能大于右边界')
        if r > (len(self.data) - 1):
            raise IndexError('超出边界范围')
        # 在以根节点的线段树开始搜索区间
        return self._find(0, 0, self.get_size() - 1, l, r)

    def _find(self, tree_index, tree_l, tree_r, l, r):
        if tree_l == l and tree_r == r:
            return self.tree[tree_index]
        tree_mid = self._get_mid(tree_l, tree_r)
        if l > tree_mid:
            """
            去右边递归
            """
            return self._find(self._right_index(tree_index), tree_mid + 1, tree_r, l, r)
        elif r <= tree_mid:
            """
            去左边递归
            """
            return self._find(self._left_index(tree_index), tree_l, tree_mid, l, r)
        else:
            """
            去两边递归
            """
            left_res = self._find(self._left_index(tree_index), tree_l, tree_mid, l, tree_mid)
            right_res = self._find(self._right_index(tree_index), tree_mid + 1, tree_r, tree_mid + 1, r)

            return self._merge(left_res, right_res)

    def _build_tree(self, index, l, r):
        """
        创建树 里面放入元素
        index 是在哪个位置放入元素
        l r是放入元素的data的界限
        :param index:
        :return:
        """
        if l == r:
            # 如有只有一个元素,则可以认为已经到达子元素
            self.tree[index] = self.data[l]
            return
        # 获取中间节点值
        mid = self._get_mid(l, r)
        left_index = self._left_index(index)
        right_index = self._right_index(index)
        self._build_tree(left_index, l, mid)
        self._build_tree(right_index, mid + 1, r)
        self.tree[index] = self._merge(self.tree[left_index], self.tree[right_index])

    def update(self, index, val):
        self.data[index] = val
        self._update(0, 0, self.get_size() - 1, index, val)

    def _update(self, tree_index, tree_l, tree_r, index, val):
        """
        递归更新操作
        :param tree_index:
        :param tree_l:
        :param tree_r:
        :param index:
        :param val:
        :return:
        """
        if tree_l == tree_r:
            self.tree[tree_index] = self.data[index]
            return
        left_index = self._left_index(tree_index)
        right_index = self._right_index(tree_index)

        mid = self._get_mid(tree_l, tree_r)
        if index > mid:
            self._update(right_index, mid + 1, tree_r, index, val)
        else:
            self._update(left_index, tree_l, mid, index, val)

        self.tree[tree_index] = self._merge(self.tree[left_index], self.tree[right_index])

    def _get_mid(self, l, r):
        return (l + r) // 2

    def _left_index(self, index):
        return index * 2 + 1

    def _right_index(self, index):
        return index * 2 + 2

    def _merge(self, left, right):
        return left + right









class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.data = nums
        self.nums = SegmentTree(self.data)

    def _size(self):
        return len(self.data)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        self.nums.update(i,val)


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.nums.find(i,j)

if __name__ =="__main__":

    nums = [1, 3, 5]
    n = NumArray(nums)

    print(n.sumRange(0,2))
    n.update(1,2)
    print(n.sumRange(0,2))
    """
    :excepti
    sumRange(0, 2) -> 9
    update(1, 2)
    sumRange(0, 2) -> 8
    """
