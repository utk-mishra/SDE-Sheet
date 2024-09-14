class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        countone = 0
        counttwo = 0
        for i in range(len(nums)):
            if nums[i]==1:
                countone+=1
            elif nums[i]==2:
                counttwo+=1
            else:
                continue
        countzero=len(nums)-countone-counttwo
        for i in range(countzero):
            nums[i]=0
        for i in range(countzero,countzero+countone):
            nums[i]=1
        for i in range(countzero+countone,len(nums)):
            nums[i]=2
        
        
        #nums = [0]*(len(nums)-countone-counttwo)+[1]*countone+[2]*counttwo
        print(nums)
        #print(res)
        #nums=res