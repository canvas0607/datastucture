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



class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        self._add(self.root,word)


    def _add(self,node,word):
        for i in range(len(word)):
            w = word[i]
            w = w.lower()
            if node.next.get(w,None):
                node = node.next.get(w)
            else:
                new_node = Node()
                node.next[w] = new_node
                node = new_node

            if i == len(word) - 1:
                node.is_word = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self._search(self.root,word,0)

    def _search(self,node,word,index):
        if index == len(word):
            return node.is_word
        c = word[index].lower()
        if c != '.':
            if not node.next.get(c,None):
                return False
            else:
                return self._search(node.next[c],word,index+1)
        else:
            for k in node.next.keys():
                if self._search(node.next[k],word,index+1):
                    return True
            return False
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

if __name__ == "__main__":
    w = WordDictionary()

    for word in ['bad',"WordDictionary","addWord","addWord","addWord","search","search","search","search"]:
        w.addWord(word)


    print(w.search('....'))
    x = 1