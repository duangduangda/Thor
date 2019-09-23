# coding:utf-8

class Solution:
    def removeElement1(self, nums, val: int) -> int:
        """使用了额外的空间"""
        if not nums:
            return 0
        result = {}
        for num in nums:
            if num in result:
                pass
            else:
                result[num] = -1    
        return len(result)


    def removeElement(self, nums,val) -> int:
        """使用线性表的逆序循环"""
        j = len(nums)
        for i in range(j-1, -1, -1):
            print(nums)
            if nums[i] == val:
                nums.pop(i)
        return len(nums)


    def removeElement2(self, nums, val:int) -> int:
        """将不相等的数据迁移"""
        if not nums or len(nums) == 0:
            return 0
        j = 0
        for i,num in enumerate(nums):
            if num != val:
                nums[j]= num
                j += 1
        return j


def main():
    val = 3
    nums =[3,2,2,3]
    s = Solution()
    print(s.removeElement(nums,val))
    val = 2
    nums = [0,1,2,2,3,0,4,2]
    print(s.removeElement(nums,val))


if __name__ == '__main__':
    main()