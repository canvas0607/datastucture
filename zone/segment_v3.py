
class SegTree:
    def __init__(self,data):

        self.data = data
        self.size = len(self.data)
        #初始化一个满二叉树出来
        self.l = [None for _ in range(4*self.size)]
        self._gen_tree(0,0,self.size - 1)

    def update(self,index,value):
        self.data[index] = value
        self._update(index)

    def _update_v2(self,index,l,r,tree_l,tree_r):
        """
        递归更新
        :param index:
        :return:
        """
        if tree_r == tree_l:
            self.l[tree_r] = self.data[index]
            return


    def _update_v1(self,index):
        """
        循环更新
        :param index:
        :return:
        """
        while True:
            left_child = self._left_child(parent)
            right_child = self._right_child(parent)
            self.l[parent] = self._merge(self.l[left_child],self.l[right_child])
            parent = self._parent(parent)

    def _gen_tree(self,index,l,r):
        #递归到底的情况,就是只有一个数据
        if l == r:
            self.l[index] = self.data[l]
            return

        middle = self._get_middle(l,r)
        left_child = self._left_child(index)
        right_child = self._right_child(index)
        self._gen_tree(left_child,l,middle)
        self._gen_tree(right_child,middle+1,r)
        self.l[index] = self._merge(self.l[left_child],self.l[right_child])

    def _merge(self,left_lists,right_lists):
        l = []
        if not isinstance(left_lists,int):
            for i in left_lists:
                l.append(i)
        else:
            l.append(left_lists)

        if not isinstance(right_lists,int):
            for i in right_lists:
                l.append(i)
        else:
            l.append(right_lists)
        return l

    def _get_middle(self,l,r):
        return (l + r)//2

    #获取左子树
    def _left_child(self,index):
        self._check_range(index)
        return 2 * index + 1
    #获取右子树
    def _right_child(self,index):
        self._check_range(index)
        return 2 * index + 2

    #获取父节点
    def _parent(self,index):
        self._check_range(index)
        if index == 0:
            return index
        return (index - 1)//2

    def _check_range(self,index):
        """
        检查index是否超出合法范围
        :param index:
        :return:
        """
        if index < 0 or index > 4 * self.size:
            raise IndexError

if __name__ == "__main__":
    s = SegTree([1,2,3,4,5,6,7,8,9])
    x = 1