
# 定义函数
def minimum(x, y):

    #  获取最大的数
    if x > y:
        greater = x
    else:
        greater = y
    
    lcm = None

    while(True):
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1

    return lcm


arr = []
for i in range(50):
    if i % 7 == 0 and i != 0:
        arr.append(i)

for item in arr:
    lcm = minimum(item, 50)
    if minimum(item, 50): 
        print(item, minimum(item, 50),int(minimum(item, 50) / item))
