# hash表牺牲了数据的顺序性 知道了元素的后一个元素是什么 提高了性能
# 算法思路分析 牺牲某些维护的特性 或者增加一些空间 就能提高性能
# 集合 映射的数据结构

# 有序集合 有序映射 -->平衡树

# 无序集合 无序映射 -->哈希表


# hash表的地址冲突解决方案 (链地址法 )可以使用链表和tree来解决

# tree是要求数据具有可比较性

# 更多处理hash冲突的处理方式,

# 1. 开放地址法 --> 线性探测 |平方探测法 |二次哈希
# 2. 再哈希法
# 3. coalesced hashing


# 更多的数据结构 图结构 --> 邻接表 邻接矩阵

# 双端队列 随机队列 最大最小队列

# 双向链表 循环链表

# 跳跃表 后缀数组

# K-D树 splay 树 B树
from avl.avl_test import AVL


class MyHash:
    def __init__(self):
        self.init_size = 2
        # 初始化数组来作为桶
        self.buckets = [AVL() for _ in range(self.init_size)]
        # 动态的计算桶冲突,增加空间
        self.upper_tol = 2
        self.low_tol = 1
        self.size = 0

    def _get_rating(self):
        return self.size/self.init_size

    def put(self, val):
        bucket_num = self._get_bucket_num(val)
        tree = self.buckets[bucket_num]
        tree.add(val)
        self.size += 1
        if self._get_rating() > self.upper_tol:
            self.init_size *= self.init_size
            new_buckets = [AVL() for _ in range(self.init_size)]
            for bucket in self.buckets:
                for val in bucket:
                    bucket_num = self._get_bucket_num(val.data)
                    tmp_tree = new_buckets[bucket_num]
                    tmp_tree.add(val.data)
            self.buckets = new_buckets

    def _get_bucket_num(self, val):
        hash_val = abs(hash(val))
        bucket_num = hash_val % self.init_size
        return bucket_num

    def find(self, val):
        bucket_num = self._get_bucket_num(val)
        tree = self.buckets[bucket_num]
        return val in tree


if __name__ == "__main__":
    h = MyHash()
    print(h.put(1))
    print(h.put(2))
    print(h.put(3))
    print(h.put(4))
    print(h.put(5))
    print(h.put(55))
    x= 1
