#trie 用于存储单词并且查找单词

# trie的速度只和单词的长度有关

# trie 其实是一个多叉树 每个边指向一个英文字符

# trie下面存储一个或多个单词

# trie的结束的节点要使用一个标识来表明这个是一个单词

#如下 可以存储多个单词 cat|can  也可以重复的有panda|pan
# leetcode 208 211
#可以做map操作，比如统计词频等

# other topics ||||
# remove word
# compressed Trie
# ternary search trie
# suffix trie
# KMP BOYER-Moore Rabin-Karp
# compressed file(file is word)
# regex engine
# compile
# DNA
"""

    root
  /  |    \
a    c    p
|    |    |
c    a    a
|    |\   |
t    t n  n
          |
          d
          |
          a
"""



class Node:
    def __init__(self):
        """
        node has two attribute,is_word indicate this is a end of a word
        (if a node is not a leaf,but it can be is words end),next must be a map
        contains like 26 character etc..,and it points next node location
        :param value:
        """
        self.is_word = False
        self.next = dict()

class Trie:
    """
    1. add, when add a word, it add its character to the node. when its done,set the node is_word true

    2. contains --> iterate the word,gen every character

    3. has root
    """
    def __init__(self):
        self.root = Node()

    def insert(self,word):
        self._add(self.root,word)

    def _add(self,node,word):
        for i in range(len(word)):
            w = word[i]
            if node.next.get(w,None):
                node = node.next.get(w)
            else:
                new_node = Node()
                node.next[w] = new_node
                node = new_node

            if i == len(word) - 1:
                node.is_word = True

    def search(self,word):
        return self._contatins(self.root,word)

    def _contatins(self,node,word):
        for i in range(len(word)):
            w = word[i]
            if w in node.next.keys():
                if i == len(word) - 1:
                    return node.next[w].is_word
                else:
                    node = node.next[w]
                    continue
            else:
                return False

    def startsWith(self,prefix):
        node = self.root
        for i in range(len(prefix)):
            w = prefix[i]
            if w in node.next.keys():
                if i == len(prefix) - 1:
                    return True
                else:
                    node = node.next[w]
                    continue
            else:
                return False


if __name__ == "__main__":
    t = Trie()
    t.add('cat')
    t.add("panda")

    print(t.contains('cat'))
    print(t.contains('act'))
    print(t.contains('pan'))
    print(t.contains('panda'))
    print(t.prefix('pan'))
    x = 1