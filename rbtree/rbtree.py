# 红黑树其实是2 3树的表示
# 红色节点表示 和黑色平级 在左边
# 节点初始化的时候是红色,表示希望去融合新节点和 2 3树一样
# 2 3树中不会把节点加在空节点里面 而是去融合

# 红黑树中的性质
#
#
#
#

RED = True
BLACK = False


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        # 初始化的时候,把颜色指定为红色,红色表示去融合,2 3树的所有节点都是先融合再变形
        self.color = RED


class RBTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def add(self, val):
        self.root = self._add(self.root, val)
        # 保持根节点永远是黑色
        self.root.color = BLACK

    def _add(self, node, val):
        if node is None:
            self.size += 1
            return Node(val)

        if node.val > val:
            node.left = self._add(node.left, val)
        elif node.val < val:
            node.right = self._add(node.right, val)

        if(self._is_red(node.right) and not self._is_red(node.left)):
            node = self._left_rotate(node)

        if (self._is_red(node.left) and self._is_red(node.left.left)):
            node = self._right_rotate(node)

        if(self._is_red(node.right) and  self._is_red(node.left)):
            node = self._flip_colors(node)


        return node

    def _is_red(self,node):
        if node is None:
            return BLACK
        return node.color == RED
    #当融合的时候, 2 3树种 插入的元素比原来的元素要大
    # 而且红色节点在node的右边,这样不符合性质
    #那么就进行会把两个元素互换位置,对应红黑的里面的左旋转

    #   x（r） ->| node(b) | -->|node(b) x(r) | --> | node(r) x(b) |
    def _left_rotate(self,node):
        """
        node                x
       /    \             /  \
      T1    x   --->   node  T3
           / \          /  \
          T2 T3        T1  T2

        :param node:
        :return:
        """
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = RED
        return x

    def _flip_colors(self,node):
        node.color = RED
        node.left.color = BLACK
        node.right.color = BLACK
        return node

    def _right_rotate(self,node):
        """

        当发生  12 ->|32 44|时 会变成  |12 32 44|-->然后会变成

                32
               /  \        -->然后翻转颜色 然后向上做融合
            12(R)  44(R)


            --------------------------
           node             x
           /  \            / \
          x   T2  -->     y  node
         / \                 /  \
        y  T1               T1  T2
       :param node:
        :return:
        """

        x = node.left
        t1 = x.right

        node.left = t1
        x.right = node

        x.color = node.color
        node.color= RED

        return x




if __name__ == "__main__":
    import random
    t = RBTree()
    for i in range(5):
        t.add(random.random())

    x = 1
