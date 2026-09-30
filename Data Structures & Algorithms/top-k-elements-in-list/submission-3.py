class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap: defaultdict[int,int]=defaultdict(int)
        count=1
        for n in nums:
            if n in hmap:
                hmap[n]=hmap[n]+1
            else:
                hmap[n]=count
        ls=[]
        sorted_nums=sorted(hmap.items(),key= lambda x:x[1],reverse=True)
        for i in range(k):
            ls.append(sorted_nums[i][0])
        return ls