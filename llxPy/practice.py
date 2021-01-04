# 练习用的py文件

# 二分查找
import math
def twoSearch(arr,l,r,x): # 递归实现
    mid = math.floor(l + (r - l) / 2) # 保留中间(向下取整)
    print(l," ",r," ",mid," ",arr[mid])
    if r >= 1:
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return twoSearch(arr,mid + 1,r,x)
        else:
            return twoSearch(arr,l,mid - 1,x)
    else:
        return -1
array = [1,2,3,4,5,9,10,13]
res = twoSearch(array,0,len(array) - 1,9)
print(res)
