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
        pass
