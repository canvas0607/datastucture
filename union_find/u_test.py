from union_find.union_find1 import UnionFind
from union_find.union_find2 import UnionFind as UF2
from union_find.union_find3 import UnionFind as UF3
from union_find.union_find4 import UnionFind as UF4
import random


def test(size, times):
    u1 = UnionFind(size)
    u2 = UnionFind(size)
    u3 = UF2(size)
    u4 = UF3(size)
    u5 = UF4(size)

    time_cast(u1, 'union_elementsv2', times)
    #time_cast(u2, "union_elements",times)
    time_cast(u3, 'union_elementsv2', times)
    time_cast(u4, 'union_elementsv2', times)
    time_cast(u5, 'union_elementsv2', times)
    print('---------------------------')


def time_cast(union, fun, times):
    import time
    import random
    # start = time.time()
    attr = union.__getattribute__(fun)
    for i in range(times):
        attr(random.randint(0, union.size - 1), random.randint(0, union.size - 1))

    start = time.time()
    for _ in range(times):
        union.is_conn(random.randint(0, union.size - 1), random.randint(0, union.size - 1))

    end = time.time()

    over_time = end - start
    print("{} casts {} second|size:{} times:{}".format(union, over_time, union.size, times))


test(1000000, 1000000)
