from helper.print_tree import pretty_print


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVL:
    def __init__(self):
        self.root = None

    def left_rotate(self, node):
        """
        左旋转情况,请保证这个时候node一定是右倾斜的情况
        :param node:
        :return:
        """

        root = node.right
        node.right = root.left
        root.left = node
        root.height = self.set_height(root)
        node.height = self.set_height(node)
        return root

    def right_rotate(self, node):
        """
        右旋转情况,请保证这个时候node一定是左倾斜的情况
        :param node:
        :return:
        """
        root = node.left
        node.left = root.right
        root.right = node
        root.height = self.set_height(root)
        node.height = self.set_height(node)
        return root

    def get_factor(self, node):
        if node.right is None and node.left is None:
            return 0
        else:
            if node.right is None:
                return node.left.height
            elif node.left is None:
                return 0 - node.right.height
            else:
                return node.left.height - node.right.height

    def set_height(self, node):
        if node is None:
            return 0
        if node.right is None and node.left is None:
            return 1
        right_height = self.set_height(node.right)
        left_height = self.set_height(node.left)
        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1

    def add(self, data):
        self.root = self._add(self.root, data)

    def _add(self, node, data):
        if node is None:
            return Node(data)

        if node.data == data:
            return node
        try:
            if node.data > data:
                node.left = self._add(node.left, data)
            else:
                node.right = self._add(node.right, data)
        except Exception:
            x =node
            y =1
            raise Exception

        node.height = self.set_height(node)

        factor = self.get_factor(node)

        # L情况
        if factor > 1:
            left_child_factor = self.get_factor(node.left)
            if left_child_factor > 0:
                # LL的情况
                node = self.right_rotate(node)
            if left_child_factor < 0:
                # LR 的情况
                node.left = self.left_rotate(node.left)
                node = self.right_rotate(node)
        # R 情况
        elif factor < -1:
            right_child_factor = self.get_factor(node.right)
            # RR情况
            if right_child_factor < 0:
                node = self.left_rotate(node)
            if right_child_factor > 0:
                node.right = self.right_rotate(node.right)
                node = self.left_rotate(node)
        return node

    def __iter__(self):
        l = list()
        if self.root is not None:
            l.append(self.root)
        while len(l) > 0:
            node = l.pop(0)
            if node.left:
                l.append(node.left)
            if node.right:
                l.append(node.right)
            yield node

    def remove(self, data):
        self.root = self._remove(self.root, data)

    def _remove(self, root, data):
        if root is None:
            return None
        if root.data == data:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                ret_node = root.right
            elif root.right is None:
                ret_node = root.left
            else:
                min_node = self._find_min(root.right)
                # bug _remove_min的时候并没有平衡
                # right = self._remove_min(root.right)
                right = self._remove(root.right, min_node.data)
                min_node.right = right
                min_node.left = root.left

                root.left = None
                root.right = None
                ret_node = min_node
                # return min_node
        elif root.data > data:
            root.left = self._remove(root.left, data)
            ret_node = root
        else:
            root.right = self._remove(root.right, data)

            ret_node = root

        if ret_node is None:
            return None
        ret_node.height = self.set_height(ret_node)
        factor = self.get_factor(ret_node)
        # L情况
        if factor > 1:
            left_child_factor = self.get_factor(ret_node.left)
            if left_child_factor > 0:
                # LL的情况
                ret_node = self.right_rotate(ret_node)
            if left_child_factor < 0:
                # LR 的情况
                ret_node.left = self.left_rotate(ret_node.left)
                ret_node = self.right_rotate(ret_node)
        # R 情况
        elif factor < -1:
            right_child_factor = self.get_factor(ret_node.right)
            # RR情况
            if right_child_factor < 0:
                ret_node = self.left_rotate(ret_node)
            if right_child_factor > 0:
                ret_node.right = self.right_rotate(ret_node.right)
                ret_node = self.left_rotate(ret_node)

        # 对所有的node判断翻转
        return ret_node

    def _find_min(self, root):
        """
        找到节点中的最小值
        :param root:
        :return:
        """
        if root.left is None:
            return root
        return self._find_min(root.left)

    def remove_min(self, node):
        min_node = self._find_min(node)
        self._remove_min(node)
        return min_node

    def _remove_min(self, root):
        """
        删除最小元素
        :param root:
        :return:
        """
        if root.left is None:
            return root.right
        root.left = self._remove_min(root.left)
        return root

    def __contains__(self, item):
        res = self._find(self.root, item)
        if res is None:
            return False
        else:
            return True

    def _find(self, root, data):
        """
        从某个节点开始,寻找这个值是否存在于节点之中
        :param root:
        :param data:
        :return:
        """
        if root is None:
            return None
        if root.data == data:
            return root
        if root.data > data:
            return self._find(root.left, data)
        else:
            return self._find(root.right, data)


if __name__ == "__main__":

    l = [i for i in range(9)]
    # l = reversed(l)

    t = AVL()
    for i in l:
        t.add(i)
        # pretty_print(t)

    print(2 in t)
    # for i in t:
    #     print(t.get_factor(i))
    pretty_print(t)

    t.remove(5)
    t.remove(2)
    t.remove(0)
    t.remove(1)
    pretty_print(t)
    x = 1
