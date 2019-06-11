class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.data = nums
        self.nums = []
        self._gen_nums(0)

    def _size(self):
        return len(self.data)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        self.data[i] = val
        self._gen_nums(i)

    def _gen_nums(self,l):
        for i in range(l,self._size()):
            if i == 0:
                try:
                    self.nums[i] = self.data[i]
                except Exception:
                    self.nums.append(self.data[i])
            else:
                sum = self.nums[i - 1] + self.data[i]
                try:
                    self.nums[i] = sum
                except Exception:
                    self.nums.append(sum)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i - 1 < 0:
            return self.nums[j]
        return self.nums[j] - self.nums[i-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

if __name__ == "__main__":
    data = [1,2,3,4,5,6]
    n = NumArray(data)

    #print(n.sumRange(0,2))
    print(n.sumRange(3,5))
    n.update(3,0)
    print(n.sumRange(3,5))
    x = 1
