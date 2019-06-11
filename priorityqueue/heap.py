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

class MaxHeap:

    def __init__(self,capacity=None):
        if capacity is None:
            """
            由于二叉堆是完全二叉树,所以可以用list来表示,然后用层序遍历以此给定下表
            """
            self.l = list()
        else:
            print('123123123')
            self.l = capacity
            self._heapify()

    def size(self):
        """
        获取堆中元素个数,由于已经用list来表示堆的逻辑结构了,所以直接返回list的长度
        :return:
        """
        return len(self.l)

    def is_empty(self):
        """
        同size函数 返回list是否为空
        :return:
        """
        return len(self.l) == 0

    def parent(self,index):
        """
        获取父节点的索引,按照上面的公式,此时使用根节点为0的方案
        所以计算式为 (i-1)/2
        :param index:
        :return:
        """
        if index == 0:
            raise IndexError("该节点没有父节点")
        return (index - 1)//2

    def left_child(self,index):
        """
        同parent 获取左节点的个数,注意有最大值限制
        :param index:
        :return:
        """
        res = index * 2 + 1
        if len(self.l) <= res:
            raise NoChildError
        return index * 2 + 1

    def right_child(self,index):
        res = index * 2 + 2
        if len(self.l) <= res:
            raise NoChildError
        return res

    def _swap(self,i,j):
        if(i < 0 or i >= self.size() or j < 0 or j >= self.size()):
            raise IndexError('交换的索引不合法')
        j_value = self.l[j]
        #把j的值为i 把i的值为j
        self.l[j] = self.l[i]
        self.l[i] = j_value

    def _sift_up(self,index):
        """
        上浮元素
        :return:
        """
        while (index > 0) and (self.l[index] > self.l[self.parent(index)]):
            """
            如果元素没有到最上面(索引为0的位置),并且比父节点大,那么他就要不断的向上移动  
            """
            self._swap(index,self.parent(index))
            index = self.parent(index)

    def find_max(self):
        return self.l[0]

    def pop(self):
        if len(self.l) == 0:
            raise IndexError('没有值')
        value = self.l[0]
        self._swap(0,len(self.l) - 1)
        del self.l[len(self.l) - 1]
        if len(self.l) > 1:
            #如果数值长度大于1 交换
            self._sift_down_v2(0)
        return value

    def _sift_down_v2(self,index):
        #如果左孩子有值,就可以循环,试想,如果左孩子的值比index还大
        #那么其实就表示没有左右孩子了，因为右孩子比左还要大
        try:
            while self.left_child(index) < len(self.l):
                max_value_index = self.left_child(index)
                try:
                    #判断是否有右节点,如果有右节点,比较左右大小
                    right_index = self.right_child(index)
                    if self.l[right_index] > self.l[max_value_index]:
                        max_value_index = right_index
                except NoChildError:
                    pass
                if self.l[max_value_index] > self.l[index]:
                    self._swap(max_value_index,index)
                    index = max_value_index
                else:
                    break
        except NoChildError:
            pass

    def _sift_down(self,index):
        """
        下沉元素
        循环条件,移动到最后了就不下沉了
        :param index:
        :return:
        """
        while index < (len(self.l) - 1):
            try:
                left_child_index = self.left_child(index)
            except NoChildError:
                left_child_index = None
            try:
                right_child_index = self.right_child(index)
            except NoChildError:
                right_child_index = None

            #首先判断是否是最后一个元素
            if (not left_child_index) and (not right_child_index):
                break
                #如果左右有一个为空,那么久直接比较左右了
            elif not left_child_index:
                if self.l[right_child_index] > self.l[index]:
                    self._swap(right_child_index,index)
                    index = right_child_index
                else:
                    break
            elif not right_child_index:
                if self.l[left_child_index] > self.l[index]:
                    self._swap(left_child_index,index)
                    index = left_child_index
                else:
                    break
            else:
                #都不为空,和大的进行交换
                left_value = self.l[left_child_index]
                right_value = self.l[right_child_index]
                if left_value > right_value:
                    if left_value > self.l[index]:
                        self._swap(left_child_index,index)
                        index = left_child_index
                    else:
                        break
                else:
                    if right_value > self.l[index]:
                        self._swap(right_child_index,index)
                        index = right_child_index
                    else:
                        break

    def add(self,data):
        """
        添加元素之后,上浮元素即可
        :param data:
        :return:
        """
        self.l.append(data)
        self._sift_up(len(self.l) - 1)

    #取出最大的元素,替换为新值
    def replace(self,value):
        """
        把元素最大元素先替换为新元素,然后做一个sift_down即可
        :param value:
        :return:
        """
        res = self.l[0]
        self.l[0] = value
        self._sift_down(0)
        return res

    def _heapify(self):
        """
        把任意数组整理成堆的形状,传统的方式就是遍历数组,然后每个add
        但是可以用Heapify去直接操作整理数组

        # 从最后一个非叶子节点,然后开始sift_down
        # 非叶子节点等于多少? 其实就是最后一个索引的父节点
        # 好处? 抛弃了一半的节点 复杂度 logn

        :return:
        """
        #1. 找到最后一个非叶子节点
        last_node = self.parent(len(self.l) -1)
        #2. 从租后一个非叶子节点开始下沉操作

        for i in range(last_node + 1,-1,-1):
            self._sift_down(i)

class MyList:
    def __init__(self):
        self.l = list()

    def add(self,value):
        #插入数据 然后排序
        self.l.append(value)
        self.l.sort()

    def pop(self):
        return self.l.pop()

def check(h):
    sorted_l = list()
    for i in range(num):
        try:
            sorted_l.append(h.pop())
        except Exception:
            print(i)
    for i in range(num -1):
        if sorted_l[i] < sorted_l[i + 1]:
            raise Exception('测试错误位置为{}的数比他后面的位置的数小'.format(str(i)))
num = 2 ** 22 - 1
num = 10 **6
def test_heapify():
    global num
    l = [random.random() for _ in range(num)]
    h = MaxHeap(l)

def test(cls):
    """
    测试用例,测试100w个数,插入和取出,每次取出的数都比下一次取出的数大
    :return:
    """
    global num
    l = [random.random() for _ in range(num)]
    h = cls()
    for i in range(num):
        h.add(l[i])

def heap_test():
    test(MaxHeap)
def heapify_test():
    test_heapify()
def list_test():
    test(MyList)
import time
def count(fun):
    start_time = time.time()
    fun()
    end_time = time.time()
    print("函数{}共计耗时{}".format(fun.__name__,end_time-start_time))



if __name__ == "__main__":
    l = [2,3,4,1,4,6,7,8,10,45,89,12,1,3,7,8,11,23]
    #l = [2,3,23]
    h = MaxHeap(capacity=l)
    #for i in l:
    #    h.add(i) y = h.pop() y = h.pop()

    count(heap_test)
    count(heapify_test)
    #count(list_test)

    #y = h.pop() #y = h.pop()
    x = 1
