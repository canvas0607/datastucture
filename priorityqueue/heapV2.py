#优先队列中

#普通线性结构 入队操作 O(1) 出队操作O(n)-->需要扫描所有元素

# 顺序线性结构 入队操作 O(n)-->在入队时需要排序  出队操作O(1)只用弹出即可

# 都是有O(n)的时间复杂度

# 堆

# 二叉堆 -->完全二叉树  --> 父节点一定大于子节点-->根节点最大 -->称为最大堆

# 完全二叉树可以层序用数组来表示, 左节点的索引是父索引的2倍,右索引是2倍+1,父亲是节点的索引除以2(向下取整)
#所以就不用建立二叉树了 直接用数组和索引来表示他的结构
#习惯把第一个数放在数组的索引1

#如果第一个数的索引是0 那么 左节点是 2*i+1 右 2*i+2 父 (i-1)/2

#入队操作 sift_up 把数据插入到最后，然后依次去比较父元素大小,然后循环对调,知道满足父元素比子元素大

# 出队操作 sift_down 把第一个元素(根节点)输出,把最后一个元素移动到根节点，调整根节点,向下调
# 然然后和他最大的子节点循环交换

#由于堆是完全二叉树,所以不会退化成链表 所以他的时间复杂度一定是O(logn)

#经典问题: 在100w(n)个元素中选出前 100(m)个元素
#1. 传统思想 先排序 在取前100 复杂度 nlogn
#2. 使用本队列 复杂度 nlogm

#3. 题目 374

#堆的其他话题 D叉堆

from queue import PriorityQueue
import random
class NoChildError(Exception):
    pass
# from collections import namedtuple
# Node = namedtuple('Node', ['data', 'left', 'right'])

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class MaxHeap:

    def __init__(self,capacity=None):
        if capacity is None:
            """
            由于二叉堆是完全二叉树,所以可以用list来表示,然后用层序遍历以此给定下表
            """
            self.l = list()
        else:
            self.l = capacity
        self.size = 0
        self.root = None
        for i in self.l:
            self._gen_tree(i)

    def heap(self,data):
        node = self._gen_tree(data)
        x = 1

    def find_last(self):
        l = list(self)
        for i in range(len(l)):
            if l[i] is None:
                return l[i - 1]

    def _gen_tree(self,item):
        """
        从左至右去生成一个
        """
        if self.root is None:
            self.root = Node(item)
        else:
            queue = list()
            queue.append(self.root)
            while len(queue) > 0:
                node = queue.pop(0)
                if not node.left:
                    new_node = Node(item)
                    node.left = new_node
                    node.left.parent = node
                    return new_node
                else:
                    queue.append(node.left)
                if not node.right:
                    new_node = Node(item)
                    node.right = Node(new_node)
                    node.right.parent = node
                    return new_node
                else:
                    queue.append(node.right)

    def floor_iter(self, node):
        # 层序遍历
        bucket = list()
        bucket.append(node)
        while len(bucket) > 0:
            node = bucket.pop()
            yield node
            if node.left:
                bucket.append(node.left)
            if node.right:
                bucket.append(node.right)

    def __iter__(self):
        return self.floor_iter(self.root)



if __name__ == "__main__":
    l = [2,3,4,1]
    #l = [2,3,23]
    h = MaxHeap(capacity=l)

    from helper.print_tree import pretty_print
    # print(list(h))
    pretty_print(list(h))
    h.heap(9)
    x = h.find_last()
    pretty_print(list(h))
