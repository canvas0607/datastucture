from priorityqueue.heap import MaxHeap
#使用优先队列来进行排名
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = dict()
        for i in nums:
            if i not in count.keys():
                count[i] = 1
            else:
                count[i] += 1
        q = MaxHeap()
        for key,v in count.items():
            s = Score(key,v)
            size = q.size()
            if size < k:
                q.add(s)
            else:
                min_value = q.find_max()
                if min_value.value < v:
                    q.pop()
                    q.add(s)

        new_l = []
        for i in range(k):
            s = q.pop()
            new_l.append(s.key)
        return new_l



class Score:
    def __init__(self,key,value):
        self.key = key
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value > other.value

    def __gt__(self, other):
        return self.value < other.value

if __name__ == "__main__":
    nums = [4,1,-1,2,-1,2,3]
    k = 2

    s = Solution()
    res = s.topKFrequent(nums,k)
    print(res)
