class Node:
    def __init__(self, value=0):
        self.next = dict()
        self.is_word = False
        self.val = value


class MapSum:
    def __init__(self):
        self.root = Node()

    def insert(self, key, val):
        self._insert(self.root, key, val)

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        return self._sum(self.root, prefix)

    def _sum(self, node, prefix):
        """
        遍历到最下面了 返回
        :param node:
        :param prefix:
        :return:
        """
        for k in prefix:
            if not node.next.get(k, None):
                return 0
            node = node.next[k]



        value = self._sum_value(node)

        return value

    def _sum_value(self, node):

        value = node.val
        for n in node.next.keys():
            value += self._sum_value(node.next[n])

        return value

    def _insert(self, node, key, val):
        for i in range(len(key)):
            if i == len(key) - 1:
                if node.next.get(key[i], None):
                    node.next[key[i]].val = val
                    return
                n = Node(val)
                n.is_word = True
                node.next[key[i]] = n
            else:
                if node.next.get(key[i], None):
                    node = node.next[key[i]]
                    continue
                else:
                    n = Node()
                    node.next[key[i]] = n
                    node = n


if __name__ == "__main__":
    x = MapSum()
    x.insert("apple", 3)
    x.insert("app", 2)
    print(x.sum('apple'))

    c = 1
