"""
并查集 把元素分类,判断元素是否连接, 如果元素的父节点指向了另一个元素的父节点就可以判断为连接

合并操作,就是就让父节点指向合并方的父节点,复杂度就是树的高度

解决性能就是降低树的高度

可以在合并的时候,先判断两个节点的高度,让低高度的去指向高高度的元素

#以 size 优化并查集
#以 rank优化并查集
# 路径压缩 把父节点压缩到父节点的父节点上面 把所有的节点压缩到路径上面的根节点
# 可以递归的调用高级的路径压缩或者循环
高级的压缩后了的时间复杂度是 log*n 相当于 O(1)
"""
class UnionFind:
    def __init__(self,size):
        self.size = size
        self.elements = []
        self.sz = []
        self.gen()

    def gen(self):
        for i in range(self.size):
            self.elements.append(i)
            self.sz.append(1)

    def find_parent(self,i):
        """
        find node parent
        :param i:
        :return:
        """
        while i != self.elements[i]:
            i = self.elements[i]
        return i

    def union_elements(self,q,p):
        q_parent = self.find_parent(q)
        p_parent = self.find_parent(p)
        if q_parent == p_parent:
            return True
        else:
            self.elements[q_parent] = p_parent
            self.sz[p_parent] += self.sz[q_parent]
            return True

    def union_elementsv2(self,q,p):
        q_parent = self.find_parent(q)
        p_parent = self.find_parent(p)
        if q_parent == p_parent:
            return True
        else:
            """
            这个版本先比较树的深度再去合并，注意合并的方向
            被合并了之后,元素增加,那么增加他相应的sz
            """
            if self.sz[q_parent] < self.sz[p_parent]:
                self.elements[q_parent] = p_parent
                self.sz[p_parent] += self.sz[q_parent]
            else:
                self.elements[p_parent] = q_parent
                self.sz[q_parent] += self.sz[p_parent]
            return True

    def is_conn(self,q,p):
        q_parent = self.find_parent(q)
        p_parent = self.find_parent(p)
        return q_parent == p_parent


if __name__ == "__main__":
    u = UnionFind(10)

    print(u.is_conn(0,9))
    print(u.is_conn(0,8))
    (u.union_elements(0,9))
    (u.union_elements(1,8))
    (u.union_elements(8,9))
    print(u.is_conn(0,8))


