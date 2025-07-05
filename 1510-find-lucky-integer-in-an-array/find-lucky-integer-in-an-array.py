import collections
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = collections.Counter(arr)
        lucky_num = -1
        for num,freq in counts.items():
            if num == freq:
                lucky_num = max(lucky_num,num)
        return lucky_num