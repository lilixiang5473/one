# 算法练习文件

# 两数之和
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
# class Solution:
#     def twoSum(self,nums,target):
#         hashtable = dict() # 哈希方法实现
#         # 变成可枚举的格式(key,value)
#         for i,num in enumerate(nums):
#             if target - num in hashtable:
#                 return [hashtable[target - num],i]
#             hashtable[nums[i]] = i
#         return []

# test = Solution()
# print(test.twoSum([0,1,3,7,10,12],12))

# 寻找两个正序数组的中位数
# 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。
# 用log(m+n)实现算法(二分查找)
class Solution(object):
    def findMidArr(self, nums1, nums2):
        if len(nums1) > len(nums2):
            return self.findMidArr(nums2,nums1)
        infinty = 2**40
        m,n = len(nums1),len(nums2)
        left,right,ansi = 0,m,-1
        median1,median2 = 0,0
        while left <= right:
            i = (left + right) // 2 # 整数除法
            j = (m + n + 1) // 2 - i

            # nums_im1, nums_i, nums_jm1, nums_j 分别表示 nums1[i-1], nums1[i], nums2[j-1], nums2[j]
            nums_im1 = (-infinty if i == 0 else nums1[i - 1])
            nums_i = (infinty if i == m else nums1[i])
            nums_jm1 = (-infinty if j == 0 else nums2[j - 1])
            nums_j = (infinty if j == n else nums2[j])

            print("i:",i)
            print("nums_im1:",nums_im1)
            print("nums_i:",nums_i)
            print("j:",j)
            print("nums_jm1:",nums_jm1)
            print("nums_j:",nums_j)

            if nums_im1 <= nums_j:
                ansi = i
                median1, median2 = max(nums_im1, nums_jm1), min(nums_i, nums_j)
                left = i + 1
            else:
                right = i - 1
        
        return (median1 + median2) / 2 if (m + n) % 2 == 0 else median1

test = Solution()
print(test.findMidArr([1,2],[3,4]))
