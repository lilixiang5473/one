# 基础学习的py文件 TODO:代表重要

# 等待用户按输入框 2.x:raw_input 3.x:input \n:换行显示 TODO:
input("等待按下 enter 键执行下文\n")

# # py代码格式严格
# if True:
#     print("llx是天才!")
# else:
#     print("llx是天才2!")

# # \ 代表换行
# total = 1 + \
#         2 + \
#         3
# print(total)

# # 换行不影响赋值
# days = ['Monday', 'Tuesday', 'Wednesday',
#         'Thursday', 'Friday']
# print(days)

# # 引号代表字符串
# word = "word"
# print(word)

# x = "a"
# y = "b"

# print (x)
# print (y)
# print (x,y)

# # if elif else 语句
# if True : 
#    print(1) 
# elif False :  
#    print(2)
# else : 
#    print(3)

# # 整型
# counter = 100
# # 浮点型
# miles = 1000.0
# # 字符串
# name = "llx"

# print (counter)
# print (miles)
# print (name)

# # 多个变量赋值
# a = b = c = 1
# print(a,b,c)

# # del:删除定义,后面再使用该变量报错
# val1 = 1
# val2 = 10
# print(val1,val2)
# del val1
# print(val2)

# # 字符串索引 TODO:截取结果也是字符串
# str = 'abcdef World!'
# print (str)           # 输出完整字符串
# print (str[0])        # 输出字符串中的第一个字符
# print (str[1:4])      # 输出字符串中第2个至第4-1个的字符串
# print (str[2:])       # 输出从第3个字符开始的字符串
# print (str * 2)       # 输出字符串两次
# print (str[2:4] * 2)  # 输出截取字符串两次
# print (str + "TEST")  # 输出连接的字符串
# print (str[0:5:2])    # 截取下标0-(5-1)之间长为2的首字母(abcde中的ace,长度不到2的也取首字母)

# 数组索引 TODO:截取结果也是数组(返回head至foot-1下标的值的数组)
# arr = ["a","b","c","d","e","f"]
# print(arr[-1]) # f,从末尾向前截取
# print(arr[2:4]) # ["c","d"] 2-(4-1)

# 元组 TODO:数据类型,类似于List(列表),元组用"()"标识,内部用逗号隔开,元组不能二次赋值(只读列表)
# yuanzu = ("name",100,False)
# yuanzu[2] = "string" # 不合法,元组不让修改内部值(只读)
# arr = [1,2,3]
# arr[2] = 4; # 合法的,数组允许修改里面的值
# print(arr)
# print(yuanzu) # 整个列表
# print(yuanzu[0]) # name

# 字典(类似于js中的对象) TODO:是除列表外最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。
# dict = {}
# dict['one'] = "This is one"
# dict[2] = "This is two"
# tinydict = {'name': 'runoob','code':6734, 'dept': 'sales'}
# print(dict['one'])          # 输出键为'one' 的值
# print(dict[2])              # 输出键为 2 的值
# print(tinydict)             # 输出完整的字典
# print(tinydict.keys())      # 输出所有键(数组)
# print(tinydict.values())    # 输出所有值(数组)

# TODO:数据类型转换
# 1.int 整数
# strInt = "123"
# print(strInt)
# print(int(strInt)) # int能转换string类型的number,number,a bytes-like object
# 2.long 长整数
# strLong = "123"
# print(strLong)
# print(int(strLong))
# 3.float 浮点数,默认小数点后面一位
# strFloat = "123.2300"
# print(strFloat)
# print(float(strFloat))
# 4.complex 复数
# strComplex = "123"
# print(strComplex)
# print(complex(strComplex)) # 返回(123+0j),带复数的值
# 5.str 字符串
# strStr = 123
# print(strStr)
# print(str(strStr))
# print(type(str(strStr))) # 判断类型方法1
# print(isinstance(str(strStr),str)) # 判断类型方法2
# 6.repr 表达式字符串,类似于js的JSON.stringify,也属于str类型
# strRepr = {"name":"llx"}
# print(strRepr)
# print(str(strRepr))
# print(type(str(strRepr))) # 判断类型方法1
# print(isinstance(str(strRepr),str)) # 判断类型方法2
# 7.eval 将字符串转化为公式计算出来,返回一个对象,一般是int类型,与js的eval一样
# strEval = "5 * 6"
# print(strEval)
# print(eval(strEval))
# print(type(eval(strEval)))
# print(isinstance(eval(strEval),int))
# 8.tuple 将序列转为元组,返回元组类型(只读列表)
# strTuple = "2,3,5"
# print(strTuple)
# print(tuple(strTuple)) # 返回集合("2",",","3",",","5")
# print(type(tuple(strTuple)))
# print(isinstance(tuple(strTuple),tuple))
# 9.list 将序列转为列表(数组)
# strList = "list,123"
# print(strList)
# print(list(strList)) # 返回列表['l','i','s','t',',','1','2','3']
# print(type(list(strList)))
# print(isinstance(list(strList),list))
# 10.set 可变集合(可写可读)
# strSet = "set,123"
# print(strSet)
# print(set(strSet)) # 返回集合{'s','2','3','t','e',',','1'}
# print(list(set(strSet))) # [...]
# print(tuple(set(strSet))) # (...)
# print(type(set(strSet)))
# 11.dict(s) 字典(js对象,key-value形式),s必须是序列集合
# strDict = { "key":"value", "name":"llx" }
# strDict["key"] = "hello world"
# print(strDict)
# print(type(strDict))
# print(dict(strDict))
# print(type(dict(strDict)))
# 12.frozenset 不可变集合(不是元组)
# strFro = { "key":"value", "name":"llx" }
# print(frozenset(strFro)) # 返回包裹所有key的集合
# print(frozenset(("name","list",123)))
# 13.chr ASCII码转为一个字符
# strChr = 97 # a的ASCII码
# print(strChr)
# print(type(strChr))
# print(chr(strChr))
# print(type(chr(strChr)))
# print(chr(10000))
# 14.ord 字符转为ASCII码
# print(ord("a")) # 97
# 15.hex 整数转为16进制字符串
# print(hex(100))
# print(type(hex(100)))
# 16.oct 整数转为8进制字符串
# print(oct(100))
# print(type(oct(100)))

# 算数运算符 TODO:
# print(0.1 + 0.2) # python和js都存在精度问题
# print(10.2323232323 - 20.2323232323) # 返回浮点数 10.0
# print(10 * 20)
# print(10 / 2) # 返回浮点数5.0
# print(10 % 2) # 返回整数0
# print(10 ** 2) # 10的2次方,类似于js中的Math.pow(10,2)
# print(9 // 2) # 除完向下取整
# 比较运算符 TODO:
# print(10 == 20)
# print(10 != 20)
# print(10 > 20)
# print(10 < 20)
# print(10 >= 20)
# print(10 <= 20)
# 赋值运算符 TODO:
# num = 0
# print(num)
# num += 10
# print(num)
# num -= 5
# print(num)
# num *= 4
# print(num)
# num /= 2
# print(num)
# num %= 4
# print(num)
# num **= 3
# print(num)
# print(num / 3)
# num //= 3
# print(num)
# 位运算符 TODO:转为二进制来计算
# a = 60
# b = 13
# print(a&b) # 12,都为1结果才为1
# print(a|b) # 61,有一个为1结果就为1
# print(a&b) # 49,异或,不同结果才为1
# print(~a) # -61,取反,结果为-x-1
# print(~b) # -14,取反,结果为-x-1
# print(b<<2) # 52,左移两位
# print(b>>2) # 3,右移两位
# 逻辑运算符 TODO:
# a = 10
# b = 20
# print(a and b) # a并且b,a为true返回b的值,20
# print(a or b) # a或者b,a为true返回a的值,10
# print(not(a and b)) # 取反
# 成员运算符 TODO:
# a = 10
# b = 20
# list = [1, 2, 3, 4, 5 ];
# print(a in list) # in 是否存在
# print(a not in list) # not in 是否不存在
# 身份运算符 TODO:
# a = 10
# b = a
# print(a == b)
# print(a is b) # 同上作用,判断引用
# print(a is not b) # 同上相反功能

# 条件与循环语句 TODO:(注:python中没有do...while...循环,先执行再判断)

# a = 1
# while a < 7:
#     if(a % 2 == 0):
#         print(a,"is even") # 偶数
#     elif(a % 2 == 1):
#         print(a,"is odd") # 奇数
#     else:
#         print("error")
#     a += 1

# for letter in 'Python':     # 第一个实例
#    print('当前字母 :',letter)

# fruits = ['banana', 'apple', 'mango']
# for fruit in fruits:        # 第二个实例
#    print('当前水果 :',fruit)

# 双for循环遍历 + if条件语句判断
# for num in range(10,20): # TODO:range获取范围方法,获取10-19的数,循环遍历
#     for i in range(2,num): # 根据因子迭代
#       if num%i == 0:      # 确定第一个因子
#         j=num/i          # 计算第二个因子
#         print('%d 等于 %d * %d' % (num,i,j))
#         break            # 跳出当层循环
#     else:                  # 循环的 else 部分
#         print(num, '是一个质数')

# for letter in 'Python':     # break第一个实例
#    if letter == 'h':
#       break
#    print('当前字母 :',letter)
  
# var = 10                    # break第二个实例
# while var > 0:              
#    print('当前变量值 :',var)
#    var = var -1
#    if var == 5:   # 当变量 var 等于 5 时退出循环
#       break

# for letter in 'Python':     # continue第一个实例
#    if letter == 'h':
#       continue
#    print('当前字母 :',letter)
 
# var = 10                    # continue第二个实例
# while var > 0:              
#    var = var -1
#    if var == 5:
#       continue
#    print('当前变量值 :',var)

# i = 1
# while i < 5:
#     print(i,"less than 5")
#     i = i + 1
# else:
#     print(i,"not less than 5")

# for letter in 'Python':
#     # print('当前字母',letter)
#     if letter == 'h':
#         pass # pass 占位块,基本没啥作用,类似于插入一个位置
#         print('这是 pass 块')
#     print('当前字母 :',letter)

# fruits = ['banana', 'apple',  'mango']
# for index in range(len(fruits)):
#     print('当前水果 :',fruits[index])

# math模块(js中的Math),cmath模块(计算复数,方法同math) TODO:
# import math # TODO:必须import引入,不是python全局的变量
# print(math) # log math模块
# print(dir(math)) # log math的模块路径
# abs:绝对值
# fabs:绝对值(返回浮点数)
# ceil:向上取整
# floor:向下取整
# cmp:比较大小返回-1 0 1
# exp:e的几次方
# log:默认以e为底,两个参数,第二个参数为底,第一个参数为值
# log10:以10为底的幂数
# max:最大值
# min:最小值
# modf:返回整数和小数部分(集合,都是浮点数)
# pow:几次方
# round:四舍五入
# sqrt:开平方

# 随机数函数 TODO:
# import random
# print(range(10)) # 0-9
# print(random.random()) # 随机[0-1)的值
# print(random.choice(range(10))) # 0-9随机挑选一个整数
# print(random.randrange(100, 1000, 1)) # 输出 100 <= number < 1000 间的任意值
# print(random.randrange(100, 1000, 2)) # 输出 100 <= number < 1000 间的偶数
# print(random.randrange(100, 1000, 3)) # 输出 100 <= number < 1000 间的递增间隔为3的值
# # random.seed,种子方法,不常用,改变随机值的取值
# arr = [1,2,3,4,5]
# print(arr)
# random.shuffle(arr) # 改变原数组,乱序排序
# print(arr)
# print(random.uniform(5, 10)) # 区间5-10,随机生成一个实数

# 三角函数 TODO:
# import math
# print(math.acos(0.64)) # 反余弦值
# print(math.asin(0.64)) # 反正弦值
# print(math.atan(0.64)) # 反正切值
# print(math.cos(0.64)) # 余弦值
# print(math.sin(0.64)) # 正弦值
# print(math.tan(0.64)) # 正切值
# print(math.radians(90)) # 角度转为弧度
# print(math.degrees(1.571)) # 弧度转为角度

# 数学常量 TODO:
# import math
# print(math.pi)
# print(math.e)

# 字符的方法 TODO: s%:字符 %d:整数 c%:ASCII %u:无符号整型 %o:八进制 %x:16进制 %X:16进制大写 %f:浮点数
# print("我叫 %s 今年 %d 岁" % ("李立翔",25))

# 三字符代表多行
# para_str = """

# f-string
# x = 1
# print(f'{x+1}')
# print(f'{x+1=}') # =写括号里面代表展示运算过程

# TODO:重要的字符方法
# print("llx llx llx".capitalize()) # 首字母大写
# print("L".center(10,"s")) # 字符剧中,返回第一个参数长度的字符,不够的地方填充第二个参数
# print("llxlx".count("l",0,1)) # 某个字符(串)出现的次数,第二个为区间起始,第三个为区间结束
# print("llxllx".startswith("ll")) # 是否以某个字符开头,参数2为区间开始,参数3为区间结束
# print("llxlx".endswith("lx")) # 是否以某个字符(串)为结尾,参数2为区间开始,参数3为区间结束
# print("llxlx".find("lx")) # 找某个字符(串)是否存在,第二个参数区间开始,第三个参数区间结束
# print("llxlx".index("lx",2)) # 找某个字符第一次出现的下标,第二个参数区间开始,第三个参数区间结束
# print(" asdads213".isalnum()) # 字符串是否全是字母或者数字(不能有字符)
# print("你好q".isalpha()) # 字符串是否全是字母或者汉字(不能有数字和字符)
# print("123123123".isdigit()) # 是否全是数字
# print("ttt sss".islower()) # 是否全为小写
# print("ttt SSS".isupper()) # 是否全为大写
# print("123123".isnumeric()) # 是否全为数字
# print("    ".isspace()) # 是否全空白
# print("Title Test".istitle()) # 是否是标题化(每个单词首字母大写)
# print("l".join("22334455")) # 对一个序列每个元素插入前面的字符,最后合并为一个字符串
# print(len("llxllx")) # 返回字符串的长度
# print("llx123".ljust(50,"*")) # 返回一个长度的字符串,不足长度就后面填充新字符
# print("llx123".rjust(50,"*")) # 返回一个长度的字符串,不足长度就前面填充新字符
# print("LLXSSSSSS".lower()) # 返回小写字符串
# print("llxssssss".upper()) # 返回大写字符串
# print("LL   Lxxx   SSSS  XLL".strip("L")) # 截掉两边的空格或者指定字符,包括重复
# print("LL   Lxxx   SSSS".lstrip("L")) # 截掉最左边的空格或者指定字符,包括重复
# print("LL   Lxxx   SSSS  XLL".rstrip("L")) # 截掉最右边的空格或者指定字符,包括重复
# # TODO:translate用来执行翻译表,maketrans制作的就是翻译表
# makeObj = str.maketrans("lx","bs") # 转换字符,替换长度要一样,l变b,x变s
# print("llxllxasd".translate(makeObj)) # translate执行替换,全局替换
# print(max("ll123xllxasd")) # 返回str中ASCII码最大的字符
# print(min("ll123xllxasd")) # 返回str中ASCII码最小的字符
# replaceStr = "this is string example....wow!!!"
# print(replaceStr.replace("is","was",3)) # 替换全部的字符,第三个参数自定义替换次数
# print("llxllx".rfind("ll")) # 从右边开始找,返回下标
# print("llx llx".split()) # 默认以空格分隔,参数1自定义分割字符,参数2分隔次数
# print("llx \n llx \n".splitlines(True)) # 是否保留换行符,默认不保留
# print("llX".swapcase()) # 大小写互转
# print(str.title("llx llx hello")) # 制作标题话内容,每个单词首字母大写
# print("llxllx".zfill(50)) # 右对齐,前面填充0
# print("2323".isdecimal()) # 校验字符串是否只含有十进制字符(数字,类似于isnumeric)

# TODO:重要的列表(数组)方法
# print(len([1,2,3])) # 获取数组长度
# print([1,2,3] + [4,5,6]) # 数组拼接
# print([1,2,3] * 4) # 重复拼接几个数组
# print(3 in [1,2,3]) # 判断是否存在
# for x in [1,2,3]: # 迭代
#     print(x)
# print([[1,2,3],['a','b','c']][1][1]) # 多维数组
# print(max([1,2,3])) # 返回数组最大值
# print(min([1,2,3])) # 返回数组最小值
# arr = [{"name":"llx"},{"age":18}]
# print(arr)
# print(arr[0]['name'])
# arr.append({"key":"value"}) # append后面插入,修改原数组
# print(arr)
# print(arr.count({"key":"value"})) # 判断出现次数,直接判断深层的值
# print(list(range(5)))
# arr.extend(list(range(5))) # extends 后面一次性插入多个序列值,修改原数组
# print(arr)
# print(arr.index(4)) # 找数组中某个值第一次出现的下标,不存在报错:x not in list
# arr.insert(0,-1) # 某个下标插入某个值或者对象
# print(arr)
# arr.pop() # 删除某个下标的值,默认最后一个
# print(arr)
# arr.remove({"key":"value"}) # 删除第一次匹配的某个值
# print(arr)
# arr.reverse() # 反转数组,改变原数组
# print(arr)
# # TODO:比较重要的方法sort排序
# arr2 = [{"key":3},{"key":1},{"key":4},{"key":2}]
# print(arr2)
# def takeKey(ele):
#     return ele["key"]
# arr2.sort(key=takeKey) # 排序,默认正序,只能比较同一类型的数据,reverse=True倒序,key=func自定义根据什么属性来排序
# print(arr2)
# arr.clear() # 清空列表
# print(arr)
# arr4 = arr2.copy() # 复制列表
# print(arr4)
# print(arr2 is arr4) # False,两个不是一个引用

# TODO:重要的元组(只读列表)方法,如果只有一个值,元组类型为值的类型
# print(type(('Google', 'Runoob', 1997, 2000)))
# print(type((50)))
# print(type((1,2,3))) # 多个值就是元组类型
# print(type(("llx")))
# print((1,2,3) + ("llx","233")) # 元组不能修改,但是可以拼接
# tup1 = (1,2,3)
# del tup1 # 删除元组
# print(len((1,2,3))) # length
# print((1,2,3) * 4) # 复制
# print(3 in (1,2,3)) # True,是否存在
# 截取元组某部分和数组的方法一样,正数从头,负数从尾
# print(max((1,2,3))) # 3 获取元组最大值
# print(min((1,2,3))) # 1 获取元组最小值
# print(tuple([1,2,3])) # (1,2,3) 转为元组
# print(tuple({1,2,3})) #同上
# print(tuple({"key1":"1","key2":"2"})) # ('key1','key2') 获取键为元组内容

# TODO:重要的字典(对象)方法
# dict1 = {"key1":1,"key2":2}
# del dict1["key1"]
# print(dict1) # {"key2":2}
# print(str({1,2,3})) # 展示字符的字典,包括'{}'
# dict1 = {1,2,3}
# print(dict1)
# dict1.clear()
# print(dict1) # set(),清空字典的全部内容
# dict1 = {1,2,3}
# dict2 = dict1.copy() # 深拷贝
# dict3 = dict1
# print(dict2 is dict1) # False
# print(dict3 is dict1) # True
# print(1 in {1,2,3}) # True
# print(1 in {"1":1,"2":2}) # False
# print("1" in {"1":1,"2":2}) # True
# dict1 = {"1":1,"2":2,"3":3}
# print(dict1.items()) # 以列表返回可遍历的(键, 值) 元组数组
# print(dict1.keys()) # 以列表返回所有的key
# dict1.setdefault("4",4) # 设置key,value,默认设置None
# print(dict1)
# dict2 = {"5":5,"6":6}
# dict1.update(dict2) # 只能插入key value形式的值
# print(dict1) # 将dict2的值全部插入到dict1中
# print(dict1.values()) # 返回一个迭代器,包裹着列表形式的值
# print(dict1.pop("5")) # 相当于del,返回值是删除的key对应的value
# print(dict1)
# print(dict1.popitem()) # 删除最后的一对键值对,返回值是元组形式的该键值对
# print(dict1)

# TODO:重要的集合方法(set === {1,2,3})
# print(set({1}) is {1}) # False
# set1 = {1,2,3}
# print(set1.pop()) # 1,删除第一个数,返回值是第一个值,改变原集合
# print(set1) # {2,3}
# set1.add(4) # 插入4这个元素
# print(set1) 
# set1.remove(2) # 删除2这个元素,与discard效果一样
# print(set1)
# set1.discard(4) # 删除4这个元素
# print(set1)
# print(len(set1)) # 返回集合的长度
# set1.clear() # 清空集合
# print(set1)
# print(1 in set1) # 判断是否存在 False
# set1.add(6)
# print(set1)
# set2 = set1.copy() # 拷贝集合
# print(set2)
# set2.add(7)
# print(set2)
# print(set2.difference(set1)) # 返回两个集合的差集(相同的过滤掉)
# set2.difference_update(set1) # 直接过滤掉原集合的相同值
# print(set2) # {7}
# print({6,7,8,9,10}.intersection({6,8})) # 返回集合的交集
# set3 = {6,7,8,9,10}
# set4 = {2,3,4,5,6,7}
# set3.intersection_update(set4) # 修改原集合,保留相同值(过滤掉不同的值)
# print(set3)
# print({1,2,3}.isdisjoint({4,5,6})) # 是否存在相同值,不存在返回True,存在相同返回False
# print({1,2}.issubset({1,2,3})) # 判断前是否是后的子集,是返回True
# print({1,2,3}.issuperset({1,2})) # 判断后是否是前的子集,是返回True
# set5 = {"apple","banana","orange"} # 字符内容随机移除,纯数字按顺序移除
# set5.pop()
# print(set5)
# print({1,2,3,4,5}.symmetric_difference({4,5,6,7,8})) # 返回两个集合不同值的集合
# set6 = {1,2,3,4,5}
# set6.symmetric_difference_update({4,5,6,7,8}) # 后的不同值插入到前里面
# print(set6)
# print({1,2,3,4,5}.union({4,5,6,7,8})) # 返回两个集合的并集,过滤重复的
# set7 = {1,2,4}
# set7.update({3}) # 修改原值,相当于插入一个值
# print(set7)

# 迭代器与生成器 TODO:TODO:TODO:(Python最强大功能之一,非常重要)
# 迭代器有两个基本的方法：iter() 和 next()。
# import sys         # 引入 sys 模块
# print(sys.path) # 文件路径和环境变量等配置文件路径
# print(sys.argv[0]) # py文件名
# list = [1,2,3,4]
# it = iter(list) # iter创建迭代器对象
# for x in it:
#     print(x,end=' ')
# while True:
#     try:
#         print (next(it))
#     except StopIteration: # 捕获异常
#         sys.exit() # 中断py文件的执行(后面的都不会执行)
# print('hello world')
# 迭代器与类(面向对象) TODO:类的迭代器需要定义两个方法__iter__()与__next__()
# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self
 
#   def __next__(self):
#     x = self.a
#     self.a += 1
#     return x
# myclass = MyNumbers()
# myiter = iter(myclass)
# print('a :',myclass.a)
# print('x :',next(myiter))
# print('a :',myclass.a)
# print('x :',next(myiter))
# print('a :',myclass.a)
# print('x :',next(myiter))
# print('a :',myclass.a)
# print('x :',next(myiter))
# print('a :',myclass.a)
# print('x :',next(myiter))
# print('a :',myclass.a)
# StopIteration TODO:异常,防止出现无限循环
# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self
#   def __next__(self):
#     if self.a <= 20:
#       x = self.a
#       self.a += 1
#       return x
#     else:
#       raise StopIteration # raise相当于sys.exit()作用,停止后面语句并且抛出异常
# myclass = MyNumbers()
# myiter = iter(myclass)
# for x in myiter:
#   print(x) # 输入1-20
# 生成器:generator函数(使用yield的函数) TODO:生成器是返回一个迭代器的函数(生成器相当于一个迭代器)
# 斐波那契数列:
# (普通循环实现)
# a,b = 0,1
# while b < 100: 
#     print(b,end=',') # end:以''内的符号分割内容
#     a,b = b,a+b
# (yield实现)
# import sys
# def fibonacci(n): # 生成器函数 - 斐波那契
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a # 此处等待,外部执行一次next,这里通过一次
#         a, b = b, a + b
#         counter += 1
# f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
# while True:
#     try:
#         print (next(f), end=" ")
#     except StopIteration:
#         sys.exit()

# 函数: TODO:TODO:def定义函数名
# def testFunc(i):
#     print(i)
# testFunc("llx")
# TODO:注:基本数据类型是不可变数据类型(包括元组),引用类型一般是可变类型
# TODO:注:函数参数是不可变类型时,函数内部修改参数是新生成一个变量,不影响外部值
# TODO:注:函数参数是可变类型时,函数内部修改参数是修改变量本身,外部值也会受影响
# a = 1 # 不可变类型
# print('a ',a)
# def changeNum(num):
#     num = 2
#     print('num ',num)
# changeNum(a)
# print('a ',a)
# b = [1,2,3] # 可变类型
# print('b ',b)
# def changeArr(arr):
#     arr.reverse()
#     print('arr ',arr)
# changeArr(b)
# print('b ',b)
# TODO:说明
# 函数def的时候有参数,就是必需参数,不传参报错
# 关键字参数:调用是参数是变量,并且参数名和函数的参数名相同,可以赋值,顺序不影响传参的混乱(相当于js的结构赋值)
# 不定长参数 TODO:相当于参数结构赋值(js中的参数...rest的作用)
# def printinfo( arg1, *vartuple ): # 1.*以元组获取
#    print ("输出: ")
#    print (arg1)
#    print (vartuple) # 元组集合(不能修改内部值)
#    for x in vartuple:
#        print(x)
# printinfo( 70, 60, 50 )
# def printinfo( arg1, **vardict ): # 2.**以字典获取key:value形式的参数
#     print ("输出: ")
#     print (arg1)
#     print (vardict)
# printinfo(1, a=2,b=3)
# 匿名函数 TODO:不需要def定义函数
# sum = lambda a,b:a+b # :前为参数,:后为返回值
# print(sum(10,20))
# def f(a, b, /, c, d, *, e, f): # /占位后面那个参数不能用关键字形参 *占位后面那个必须使用关键字参数形式(a=20)
#     print(a, b, c, d, e, f)
# f(10, 20, 30, d=40, e=50, f=60)

# 查看地址 TODO:id()方法查看内存地址
# a = 1
# b = [1,2,3]
# print(id(a))
# print(id(b))

# 数据结构 TODO:一些特殊方法
# 列表后入先出比先入先出性能高,先入先出需要修改后面所有元素的位置
# 列表推导式 TODO:TODO:TODO:取巧方法
# vec = [2, 4, 6]
# print([3*x for x in vec]) # [6,12,18],全部乘3
# print([[x, x**2] for x in vec]) # 获取二维列表 [x,x*x]
# print([3*x for x in vec if x > 3])  # for in 取变量, if取条件
# vec1 = [2, 4, 6]
# vec2 = [4, 3, -9]
# print([x*y for x in vec1 for y in vec2 if x > 3]) # 可以添加多个条件,每个都相乘,x取>3的
# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
# print([[row[i] for row in matrix] for i in range(4)]) # 3x4矩阵变成4x3矩阵
# print([[row[i] for row in matrix] for i in range(3)]) # 3x4矩阵变成3x3矩阵
# print([[row[i] for row in matrix for i in range(3)]]) # 3x4矩阵变成1x9矩阵
# print([[row[i] for row in matrix for i in range(3)] for x in range(3)]) # 3x4矩阵变成3x9矩阵(并且是三个相同的矩阵)

# 模块 TODO:import引入模块(包括python自带模块和第三方)
# import sys # 系统模块
# for i in sys.argv:
#    print(i)
# import test # 额外有个test.py文件,里面有个print_func方法,一个参数
# test.print_func('llx')
# import fibo # 计算斐波那契数列的模块
# print(dir(fibo)) # 获取模块内定义的所有名称,用字符串列表返回
# print(__name__)
# if __name__ == '__main__': # __name__ 能判断是当前文件运行,还是引入模块在运行
#     print('程序自身在运行')
# else:
#     print('我来自另一模块')
# fibo.fib(1000)
# print(fibo.fib2(1000))
# from fibo import fib,fib2 # 引入其中的某些模块
# fib(1000)
# print(fib2(1000))
# 包 TODO:TODO:
# 包是一种管理 Python 模块命名空间的形式，采用"点模块名称"。
# 比如一个模块的名称是 A.B， 那么他表示一个包 A中的子模块 B 。

# 读和写文件(写爬虫上传文件啥的,需要写文件) TODO:TODO:TODO:(参数1文件路径,参数2读写追加等操作,具体看文档)
f = open('test.txt','r',encoding='utf-8') #如果文件不是uft-8编码方式，读取文件可能报错
print(f.read()) #返回一个字符串，读取文件所有内容
f = open('test.txt','w',encoding='utf-8') # 写文件
f.write("LLX是天才1\n")
f.close()
f = open('test.txt','a',encoding='utf-8') # 追加文件内容
f.write("LLX是天才2")
f.close()
readF = open('test.txt','r',encoding='utf-8')
read = readF.read() # 读文件
readF.close()
print(read)

# OS操作 TODO:TODO:TODO:系统OS操作
# import os # 引入OS操作模块
# retval = os.getcwd() # getcwd获取当前路径
# print(retval)
# os.chdir("/") # chdir修改当前工作目录(修改终端)
# retval = os.getcwd()
# print(retval)
# os.chflags(path, flags) 设置路径的标记为数字标记,只有unix可以使用,被标记的文件使得它不能被重命名和删除
# TODO:os.chmod() 修改文件或者目录的权限
# import stat # 引入文件状态模块
# 建立组id位,这个文件会被记录锁定(即该文件不能写)
# print("锁定文件:不能写")
# os.chmod("test.txt", stat.S_IXGRP)
# TODO:stat.S_IWUSR:设置文件的所有者的写权限。不同的是 stat.S_IWOTH:其它有写权限(所有者可能还是没写权限)
# print("所有者都可以写该文件")
# os.chmod("test.txt", stat.S_IWUSR)
# os.chown(path, uid, gid) 更改文件所有者
# os.chroot(path) 更改当前进程的根目录
# os.close(fd) 关闭指定文件的描述符fd
# f = os.open('test.txt',os.O_RDWR|os.O_CREAT)
# print("文件描述符fd:",os.dup(f))
# pathOK = os.access("test.txt", os.F_OK) # os.F_OK判断路径是否存在
# print("pathOK:",pathOK)
# readOK = os.access("test.txt", os.R_OK) # os.R_OK判断路径是否可读
# print("readOK:",readOK)
# writeOK = os.access("test.txt", os.W_OK) # os.W_OK判断路径是否可写
# print("writeOK:",writeOK)
# xOK = os.access("test.txt", os.X_OK) # os.X_OK判断路径是否可执行
# print("xOK:",xOK)
# TODO:剩下的OS语法照着文档写

# try...catch...(捕获异常)TODO:TODO:TODO:
# while True:
#     try:
#         x = int(input("请输入一个数字: "))
#         break
#     except (KeyboardInterrupt): # 键盘事件Error
#         print("报错")
#         break
#     except ValueError:
#         print("您输入的不是数字，请再次尝试输入！")
#     else: # 没有异常执行的语句
#         print("else")
#     finally: # 不管有没有异常都执行的语句
#         print("finally")
# try:
#     print(x)
# except (NameError):
#     print("x未定义")
# TODO:raise抛出异常
# x = 10
# if x > 5:
#     raise Exception('x 不能大于 5。x 的值为: {}'.format(x))
# try:
#     raise NameError('HiThere')
# except NameError:
#     print('An exception flew by!')
#     raise

# 面向对象(类 继承 多态)TODO:TODO:TODO:TODO:TODO:

# TODO:类的一些专有方法(除了前两个,其他都不常用)
# __init__ : 构造函数，在生成对象时调用
# __del__ : 析构函数，释放对象时使用
# __repr__ : 打印，转换
# __setitem__ : 按照索引赋值
# __getitem__: 按照索引获取值
# __len__: 获得长度
# __cmp__: 比较运算
# __call__: 函数调用
# __add__: 加运算
# __sub__: 减运算
# __mul__: 乘运算
# __truediv__: 除运算
# __mod__: 求余运算
# __pow__: 乘方

# class Test: # 基类
#     i = 12345 # 直接定义属性,相当于self.i = 12345
#     __myI = 233 # 定义私有变量,不能在类的外部直接获取
#     def __init__(self): # __init__类似于js的constructor方法
#         self.arr = []
#     def f(self,num1,num2): # 定义类的一些方法
#         self.i = 0
#         self.num1 = num1
#         self.num2 = num2
#         print("self:",self)
#         print(Test)
#         print(self.__class__)
#         print(self.__class__ is Test) # 同一个类
#         self.__myI = 322
#         print(self.__myI) # 私有变量只能内部获取/修改
#         return self.i
# test = Test()
# print(test.i)
# print(test.f(1,2))
# print(test.i)
# print(test.num1) # 执行方法定义的,原本是没有的
# print(test.num2) # 执行方法定义的,原本是没有的
# # 报错,无法获取到 # print(test.__myI)

# class SonClass(Test): # 派生类,继承于基类(单继承)
#     def __init__(self):
#         Test.__init__(self)
#     def f(self,str): # 相同名称方法重写
#         self.str = str
#         return self.str
# son = SonClass()
# print(son.i)
# print(son.f("llx"))
# print(son.str)

# class NewClass:
#     b = 999
#     def __init__(self):
#         self.c = "c"

# class MoreClass(Test,NewClass): # 派生类,多继承
#     def __init__(self):
#         Test.__init__(self)
#         NewClass.__init__(self)
#         self.__selfF()
#     def __selfF(self): # 定义私有方法
#         print("定义私有方法")

# more = MoreClass()
# print(more.i)
# print(more.b)
# print(more.c)

# 命名空间:
# 内置名称:比如abs,char还有异常名称等。
# 全局名称:模块中定义的名称,记录模块的变量,包括函数、类、其他导入的模块,模块级的变量和常量
# 局部名称:函数中定义的名称，记录了函数的变量，包括函数的参数和局部定义的变量。（类中定义的也是）
# 内置包括全局,全局包括局部
# 查找顺序由小到大:在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内置中找

# 作用域:作用域是可以直接访问到命名空间的正文区域
# if True: # 不同于js,没有let块级作用域,所以外部可以访问到语句内的变量,相当于没有变量提升的var
#     msg = "hello world"
# print(msg)

# TODO:global 和 nonlocal关键字

# num = 1
# def fun1():
#     global num  # global 声明全局变量
#     print(num) # 1
#     num = 123
#     print(num) # 123
# fun1()
# print(num) # 123

# 闭包作用域
# def outer():
#     num = 10
#     def inner():
#         nonlocal num   # nonlocal 声明闭包变量,外层非全局作用域
#         # global num # 此处替换成global全局就可以访问到num
#         num = 100
#         print(num) # 100
#     inner()
#     print(num) # 100
# outer()

# 易错情况
# a = 10
# def test(a):
#     a = a + 1 # 报错,全局变量不能在方法里面直接修改,需要传参,并且修改的变量不影响全局变量
#     print(a)
# test(a)
# print(a)

# TODO:TODO:TODO:Python3 标准库概览(自带的库)
# os 操作系统库(上面有)
# sys 命令行参数(上面有)
# glob 文件通配符
# import glob
# print(glob.glob('*.py')) # 搜索当前目录全部的.py结尾的文件名称放入列表返回
# re 字符串正则匹配库(下文练习)
# import re
# # 查询全部以f打头的字母
# print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
# math 数学(上面有)
# urlopen 网络通信(TODO:TODO:TODO:爬虫和这个有关)
# from urllib.request import urlopen
# res = urlopen("http://www.baidu.com")
# f = open('test.txt','w',encoding='utf-8') # 写文件
# f.write(str(res.read().decode('utf-8'))) # decode utf-8转为可解析的中文
# f.close()
# print(res.read())
# smtplib 发送电子邮件(TODO:TODO:TODO:写后端肯定要用,需要邮件服务器,基于SMTP协议)
# import smtplib
# server = smtplib.SMTP()
# server.sendmail('jy547311291@sina.com')
# server.quit()
# 或者下面的方式
# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
# sender = 'from@runoob.com'
# receivers = ['429240967@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
# # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
# message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
# message['From'] = Header("菜鸟教程", 'utf-8')     # 发送者
# message['To'] =  Header("测试", 'utf-8')          # 接收者
# subject = 'Python SMTP 邮件测试'
# message['Subject'] = Header(subject, 'utf-8')
# try:
#     smtpObj = smtplib.SMTP('localhost')
#     smtpObj.sendmail(sender, receivers, message.as_string())
#     print ("邮件发送成功")
# except smtplib.SMTPException:
#     print ("Error: 无法发送邮件")
# date 日期(TODO:TODO:TODO:必用)
# from datetime import date
# now = date.today() # 当前年月日
# print(now)
# # print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
# birthday = date(1964, 7, 31)
# age = now - birthday
# print(age.days)
# time 时间(TODO:TODO:TODO:必用)
# import time
# print(time.time())
# zlib 数据压缩
# import zlib
# s = b'witch which has which witches wrist watch' # b打头表示二进制流
# print(len(s)) # 41
# t = zlib.compress(s)
# print(t)
# print(len(t)) # 37
# s = zlib.decompress(t)
# print(s)
# print(len(s))
# Timer 性能度量 TODO:TODO:TODO:性能优化工具
# from timeit import Timer
# print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()) # 取中间变量
# print(Timer('a,b = b,a', 'a=1; b=2').timeit()) # 性能比上面的高,直接调换两个变量值
# doctest 测试模块 TODO:TODO:TODO:提高开发质量
# def multiply(a, b):
#     """
#     >>> multiply(4, 3)
#     12
#     >>> multiply('a', 3)
#     'aaa'
#     """
#     return a * b
# def average(values):
#     """
#     >>> print(average([20, 30, 70]))
#     40.0
#     """
#     return sum(values) / len(values)
# if __name__=='__main__':
#     import doctest
#     doctest.testmod(verbose=True)

# 海伦公式: p半周长,s = (p * (p - a) * (p - b) * (p - c)) ** 0.5  相当于根号下
# a,b,c = 10,8,9
# p = (10 + 8 + 9) / 2
# s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
# print(s) # 34.19......

# 随机数生成
# import random
# print(random.randint(0,9)) # 0-9的随机整数

# 日历
# import calendar
# # 输入指定年月
# yy = int(input("输入年份: "))
# mm = int(input("输入月份: "))
# # 显示日历
# print(calendar.month(yy,mm))

# lambda 相当于表达式的含义 TODO:
# sorted 方法排序
# kv 相当于元组形式输出内容
# def dictionairy():  
#     # 声明字典
#     key_value ={}     
#     # 初始化
#     key_value[2] = 56       
#     key_value[1] = 2 
#     key_value[5] = 12 
#     key_value[4] = 24
#     key_value[6] = 18      
#     key_value[3] = 323 
#     print ("按值(value)排序:")   
#     print(sorted(key_value.items(), key = lambda kv:(kv[1], kv[0])))     
   
# def main(): 
#     dictionairy()             
      
# if __name__=="__main__":       
#     main()

# 将字符串的时间转换为时间戳 TODO:
# import time
# a1 = "2019-5-10 23:40:00"
# # 先转换为时间数组
# timeArray = time.strptime(a1, "%Y-%m-%d %H:%M:%S")
# # 转换为时间戳
# timeStamp = int(time.mktime(timeArray)) # 秒取整
# print(timeStamp)

# 将时间戳转换为指定格式日期 TODO:
# import time
# # 获得当前时间时间戳
# now = int(time.time())
# #转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
# timeArray = time.localtime(now)
# otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
# print(otherStyleTime)

# 正则表达式(re模块) TODO:TODO:TODO:
import re
# pattern正则表达式 string匹配内容 flags标志符(什么操作)

# re.match(pattern, string, flags=0) # match只匹配开始
# print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配

# re.search(pattern, string, flags=0) # search匹配全局
# print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.search('com', 'www.runoob.com').span())  # 不在起始位置匹配

# re.sub(pattern, repl, string, count=0, flags=0) # 检索替换 TODO:
# pattern : 正则中的模式字符串。
# repl : 替换的字符串，也可为一个函数。
# string : 要被查找替换的原始字符串。
# count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
# flags : 编译时用的匹配模式，数字形式。
# phone = "2004-959-559 # 这是一个电话号码"
# # 删除注释
# num = re.sub('#.*$', "", phone)
# print ("电话号码 : ", num)
# # 移除非数字的内容
# num = re.sub('\D', "", phone)
# print ("电话号码 : ", num)

# line = "Cats are smarter than dogs"
# searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
# print ("searchObj.group() : ", searchObj.group())
# print ("searchObj.group(1) : ", searchObj.group(1))
# print ("searchObj.group(2) : ", searchObj.group(2))

# # 将匹配的数字乘于 2
# def double(matched):
#     value = int(matched.group('value'))
#     return str(value * 2)
# s = 'A23G4HFD567'
# print(re.sub('(?P<value>\d+)', double, s)) # 用方法替换变量,数字变成两倍

# re.compile(pattern[, flags]) 编译正则表达式,用于match和search使用
# pattern = re.compile(r'\d+')                    # 用于匹配至少一个数字
# m = pattern.match('one12twothree34four')        # 查找头部，没有匹配
# print(m)
# m = pattern.match('one12twothree34four', 2, 10) # 从'e'的位置开始匹配，没有匹配
# print(m)
# m = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好匹配
# print(m.span()) # (3,5)
# print(m.group(0)) # 12

# re.findall(pattern, string, flags=0) 或 pattern.findall(string[, pos[, endpos]]) 查看所有匹配项
# result1 = re.findall(r'\d+','runoob 123 google 456')
# pattern = re.compile(r'\d+')   # 查找数字
# result2 = pattern.findall('runoob 123 google 456')
# result3 = pattern.findall('run88oob123google456', 0, 10)
# print(result1)
# print(result2)
# print(result3)

# re.finditer(pattern, string, flags=0) 查看所有匹配项,迭代器返回
# it = re.finditer(r"\d+","12a32bc43jf3") 
# print(it)
# for match in it: 
#     print (match.group() )

# re.split(pattern, string[, maxsplit=0, flags=0]) split方法按照能够匹配的子串将字符串分割后返回列表
# print(re.split('\W+', 'runoob, runoob, runoob.'))
# print(re.split('(\W+)', ' runoob, runoob, runoob.'))
# print(re.split('\W+', ' runoob, runoob, runoob.', 1)) # 分割一次

# CGI处理模块(处理get post请求等方法的参数) TODO:TODO:TODO:TODO:TODO:(后端接口处理,去文档看和apache服务器一起使用的demo)
# import cgi, cgitb 
# # 创建 FieldStorage 的实例化
# form = cgi.FieldStorage() 
# # 获取数据
# site_name = form.getvalue('name')
# site_url  = form.getvalue('url')
# print ("Content-type:text/html")
# print ()
# print ("<html>")
# print ("<head>")
# print ("<meta charset=\"utf-8\">")
# print ("<title>菜鸟教程 CGI 测试实例</title>")
# print ("</head>")
# print ("<body>")
# print ("<h2>%s官网：%s</h2>" % (site_name, site_url))
# print ("</body>")
# print ("</html>")

# http.cookies模块,获取请求中携带的cookie信息,用法看文档(请求携带Set-Cookie字段)
# import http.cookies

# mysql-connector python连接数据库mysql驱动插件,下面有更好的 TODO:TODO:TODO:
# python -m pip install mysql-connector安装
# import mysql.connector
# mydb = mysql.connector.connect( # 连接数据库
#   host="localhost",       # 数据库主机地址
#   user="yourusername",    # 数据库用户名
#   passwd="yourpassword"   # 数据库密码
# )
# print(mydb)
# 创建数据库
# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE runoob_db")
# 输出所有的数据库列表
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#   print(x)
# 创建表
# mycursor.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")
# 输出表
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#   print(x)
# 创建主键(创建id,唯一标识)
# mycursor.execute("ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
# 将上面合二为一,创建表和主键
# mycursor.execute("CREATE TABLE sites (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), url VARCHAR(255))")
# 插入数据(多条)
# sql = "INSERT INTO sites (name, url) VALUES (%s, %s)" # sql语句(两个变量name,url,都是str类型)
# val = [ # 插入的(key,value)
#   ('Google', 'https://www.google.com'),
#   ('Github', 'https://www.github.com'),
#   ('Taobao', 'https://www.taobao.com'),
#   ('stackoverflow', 'https://www.stackoverflow.com/')
# ]
# mycursor.execute(sql, val) # 执行插入语句
# mydb.commit()    # 数据表内容有更新，必须使用到该语句
# print(mycursor.rowcount, "记录插入成功。")
# print(mycursor.lastrowid) # 查看最新一条插入的数据的id
# 查询数据
# mycursor.execute("SELECT * FROM sites")
# mycursor.execute("SELECT name, url FROM sites") # 执行字段数据读取
# myresult = mycursor.fetchall()     # fetchall() 获取所有记录
# myresult = mycursor.fetchone() # 获取一条数据(默认正序第一条)
# for x in myresult:
#   print(x)
# mycursor.execute("SELECT * FROM sites WHERE name ='RUNOOB'") # 查找表中name为RUNOOB的那条
# 排序查询 ORDER BY
# mycursor.execute("SELECT * FROM sites ORDER BY name DESC") # DESC倒序查询name的字段列表
# 限制长度 LIMIT 起始 OFFSET
# mycursor.execute("SELECT * FROM sites LIMIT 3 OFFSET 1") # 查的内容限制长度为3,从第二条开始查
# 删除记录
# sql = "DELETE FROM sites WHERE name = 'stackoverflow'" # 删除name为stackoverflow的条
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, " 条记录删除")
# 更新数据
# sql = "UPDATE sites SET name = 'llxNew' WHERE name = 'llxOld'" # 更新llxOld为llxNew
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, " 条记录被修改")
# 删除表
# sql = "DROP TABLE IF EXISTS sites"  # 删除数据表 sites
# mycursor.execute(sql)

# PyMySQL Python3与mysql连接的驱动(比上面的好) TODO:TODO:TODO:TODO:TODO:
# pip3 install PyMySQL 安装PyMySQL
# import pymysql
# # 打开数据库连接 参1数据库地址,参2用户名,参3密码,参4数据库名称 TODO:
# db = pymysql.connect("localhost","testuser","test123","TESTDB")
# # 使用 cursor() 方法创建一个游标对象(标记对象) cursor
# cursor = db.cursor()
# # 使用 execute()  方法执行 SQL 查询 
# cursor.execute("SELECT VERSION()")
# # 使用 fetchone() 方法获取单条数据(同上面的用法)
# data = cursor.fetchone()
# print ("Database version : %s " % data)
# # 创建表 TODO:
# # 使用 execute() 方法执行 SQL，如果表存在则删除
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# # 使用预处理语句创建表
# sql = """CREATE TABLE EMPLOYEE (
#          FIRST_NAME  CHAR(20) NOT NULL, # 头名
#          LAST_NAME  CHAR(20), # 尾名
#          AGE INT,
#          SEX CHAR(1),
#          INCOME FLOAT )"""
# cursor.execute(sql)
# # 插入语句 TODO:
# # SQL 插入语句
# sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#          LAST_NAME, AGE, SEX, INCOME)
#          VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
# try:
#    # 执行sql语句
#    cursor.execute(sql)
#    # 提交到数据库执行
#    db.commit()
# except:
#    # 如果发生错误则回滚
#    db.rollback()
# # 查询操作 TODO:
# sql = "SELECT * FROM EMPLOYEE \ WHERE INCOME > %s" % (1000) # 查询收入大于1000的
# try:
#    # 执行SQL语句
#    cursor.execute(sql)
#    # 获取所有记录列表
#    results = cursor.fetchall()
#    for row in results:
#       fname = row[0]
#       lname = row[1]
#       age = row[2]
#       sex = row[3]
#       income = row[4]
#        # 打印结果
#       print ("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
#              (fname, lname, age, sex, income ))
# except:
#    print ("Error: unable to fetch data")
# # 更新操作 TODO:
# # SQL 更新语句
# sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M') # 更新 老一岁,条件为所有的男生(M)
# try:
#    # 执行SQL语句
#    cursor.execute(sql)
#    # 提交到数据库执行
#    db.commit()
# except:
#    # 发生错误时回滚
#    db.rollback()
# # 删除操作 TODO:
# # SQL 删除语句
# sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20) # 删除年龄大于20的
# try:
#    # 执行SQL语句
#    cursor.execute(sql)
#    # 提交修改
#    db.commit()
# except:
#    # 发生错误时回滚
#    db.rollback()
# # 关闭数据库连接
# db.close()
# 数据库db的API中有数据库操作的异常(类如Error等,看文档)

# time.sleep相当于js的setTimeout的作用,延迟器 TODO:
# import time
# print("Start : %s" % time.ctime())
# time.sleep( 5 )
# print("End : %s" % time.ctime())

# Python多线程 TODO:TODO:TODO:TODO:TODO:
# 线程在python相当于多个异步,或者并发处理
# 线程可以分为:
# 内核线程：由操作系统内核创建和撤销。
# 用户线程：不需要内核支持而在用户程序中实现的线程。
# Python3 线程中常用的两个模块为：
# _thread
# threading(推荐使用)

# 语法: _thread.start_new_thread ( function, args[, kwargs] )
# function - 线程函数。
# args - 传递给线程函数的参数,他必须是个tuple类型。
# kwargs - 可选参数。

# 普通的多线程案例
# import _thread
# import time
# # 为线程定义一个函数
# def print_time( threadName, delay):
#    count = 0
#    while count < 5:
#       time.sleep(delay) # 延迟下面的执行,setTimeout的作用
#       print(count)
#       count += 1
#       print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
# # 创建两个线程
# try:
#    _thread.start_new_thread( print_time, ("Thread-1", 2, ) ) # 延迟两秒执行一次
#    _thread.start_new_thread( print_time, ("Thread-2", 4, ) ) # 延迟四秒执行一次
# except:
#    print ("Error: 无法启动线程")
# while 1:
#    pass

# 线程模块 threading(线程类Thread) TODO:TODO:TODO:TODO:TODO:
# import threading
# import time
# class myThread (threading.Thread): # 继承线程类,自己写一个新的进程类
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self) # 初始化线程类的方法
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#     def run(self): # 执行进程
#         print ("开始线程：" + self.name)
#         print_time(self.name, self.counter, 5) # 延迟counter秒,执行5次
#         print ("退出线程：" + self.name)
# def print_time(threadName, delay, counter):
#     while counter:
#         time.sleep(delay)
#         print ("%s: %s" % (threadName, time.ctime()))
#         counter -= 1
# # 创建新线程
# thread1 = myThread(1, "Thread-1", 1) # id为1,进程名为Thread-1,延迟1秒执行一次
# thread2 = myThread(2, "Thread-2", 2) # 同上
# # 异步方法
# thread1.start()
# thread2.start()
# # 同步方法,直接执行类的run方法(不能这么用线程)
# # thread1.run()
# # thread2.run()
# # 异步方法是否需要等待,join方法表示在这里等待执行结束,没有join直接执行下文
# thread1.join()
# thread2.join()
# print ("退出主线程") # join 表示需要等待 1 2 都结束才执行print以及后文

# TODO:TODO:TODO:TODO:TODO: 用锁将线程变成同步
# 多线程一般会出现数据不同步的问题,遇到这种情况需要同步线程使用,让数据同步传递
# 使用线程的Lock和Rlock方法可以实现线程同步(锁的概念)
# 锁相当于多个并行方法全都同步执行,没执行完不执行下面的
# import threading
# import time
# class myThread(threading.Thread):
#     def __init__(self,threadID,name,counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#     def run(self): # 重写start需要执行的函数
#         print("开启线程：" + self.name)
#         # 获取锁
#         threadLock.acquire()
#         print_time(self.name,self.counter,3)
#         print("锁里面的内容")
#         # 释放锁,进行下面的进程
#         threadLock.release()

# def print_time(threadName,delay,counter):
#     while counter:
#         time.sleep(delay)
#         print ("%s: %s" % (threadName, time.ctime(time.time())))
#         counter -= 1

# threadLock = threading.Lock() # 创建锁
# threads = [] # 新建线程列表
# # 创建线程
# thread1 = myThread(1,"thread-1",1)
# thread2 = myThread(2,"thread-2",1)
# # 开始线程
# thread1.start()
# thread2.start()
# # 添加线程到线程列表
# threads.append(thread1)
# threads.append(thread2)
# # 等待所有线程完成,即等待队列为空,再执行下面的操作
# for t in threads:
#     t.join()
# print ("退出主线程")

# 线程优先级队列（Queue）TODO:TODO:TODO:TODO:TODO:
# Python 的 Queue 模块中提供了同步的、线程安全的队列类，包括FIFO（先入先出)队列Queue，LIFO（后入先出）队列LifoQueue，和优先级队列 PriorityQueue。
# import queue
# import threading
# import time

# exitFlag = 0

# class myThread(threading.Thread):
#     def __init__(self,threadID,name,q):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.q = q
#     def run(self):
#         print("开启线程：" + self.name)
#         process_data(self.name,self.q)
#         print("退出线程：" + self.name)
    
# def process_data(threadName,q):
#     while not exitFlag:
#         queueLock.acquire()
#         if not workQueue.empty():
#             data = q.get()
#             # 在这里获取线程数据,操作线程任务
#             print("%s 线程处理任务 %s" % (threadName,data))
#             queueLock.release()
#         else:
#             queueLock.release()
#         time.sleep(1)
        
# threadList = ["Thread-1","Thread-2","Thread-3"]
# nameList = ["One","Two","Three","four","five"]
# queueLock = threading.Lock()
# workQueue = queue.Queue(10) # 创建队列,最多执行10个任务
# threads = []
# threadID = 1

# # 创建线程,开始线程,放入线程队列
# for tName in threadList:
#     thread = myThread(threadID,tName,workQueue)
#     thread.start()
#     threads.append(thread)
#     threadID += 1

# # 填充队列
# queueLock.acquire()
# for word in nameList:
#     print("word：",word)
#     workQueue.put(word) # 将任务名称填入队列
# queueLock.release()

# # 等待队列为空,再执行后面的,否则就让pass填充,执行循环的任务(队列的任务)
# while not workQueue.empty():
#     pass

# # 通知线程退出
# exitFlag = 1

# # 等待线程队列执行完
# for t in threads:
#     t.join()
# print("退出主线程")


# 读取xml文件 (不怎么重要)
# import xml.sax
# class MovieHandler(xml.sax.ContentHandler):
#     def __init__(self):
#         self.CurrentData = ""
#         self.type = ""
#         self.format = ""
#         self.year = ""
#         self.rating = ""
#         self.stars = ""
#         self.description = ""

#     # 元素开始调用
#     def startElement(self, tag, attributes):
#         self.CurrentData = tag
#         if tag == "index":
#             print ("*****index*****")
#             title = attributes["title"]
#             print ("Title:", title)

#     # 元素结束调用
#     def endElement(self, tag):
#         if self.CurrentData == "type":
#             print ("Type:", self.type)
#         elif self.CurrentData == "format":
#             print ("Format:", self.format)
#         elif self.CurrentData == "year":
#             print ("Year:", self.year)
#         elif self.CurrentData == "rating":
#             print ("Rating:", self.rating)
#         elif self.CurrentData == "stars":
#             print ("Stars:", self.stars)
#         elif self.CurrentData == "description":
#             print ("Description:", self.description)
#         self.CurrentData = ""

#     # 读取字符时调用
#     def characters(self, content):
#         if self.CurrentData == "type":
#             self.type = content
#         elif self.CurrentData == "format":
#             self.format = content
#         elif self.CurrentData == "year":
#             self.year = content
#         elif self.CurrentData == "rating":
#             self.rating = content
#         elif self.CurrentData == "stars":
#             self.stars = content
#         elif self.CurrentData == "description":
#             self.description = content
  
# if ( __name__ == "__main__"): # 主线程

#     # 创建一个 XMLReader
#     parser = xml.sax.make_parser()
#     # 关闭命名空间
#     parser.setFeature(xml.sax.handler.feature_namespaces, 0)

#     # 重写 ContextHandler
#     Handler = MovieHandler()
#     parser.setContentHandler(Handler)

#     parser.parse("index.xml")

# 使用xml.dom解析xml 
# from xml.dom.minidom import parse
# import xml.dom.minidom

# # 使用minidom解析器打开 XML 文档
# DOMTree = xml.dom.minidom.parse("index.xml")
# collection = DOMTree.documentElement
# if collection.hasAttribute("shelf"):
#    print ("Root element : %s" % collection.getAttribute("shelf"))

# # 在集合中获取所有电影
# movies = collection.getElementsByTagName("index")

# # 打印每部电影的详细信息
# for movie in movies:
#    print ("*****index*****")
#    if movie.hasAttribute("title"):
#       print ("Title: %s" % movie.getAttribute("title"))

#    type = movie.getElementsByTagName('type')[0]
#    print ("Type: %s" % type.childNodes[0].data)
#    format = movie.getElementsByTagName('format')[0]
#    print ("Format: %s" % format.childNodes[0].data)
#    rating = movie.getElementsByTagName('rating')[0]
#    print ("Rating: %s" % rating.childNodes[0].data)
#    description = movie.getElementsByTagName('description')[0]
#    print ("Description: %s" % description.childNodes[0].data)

# JSON数据解析 TODO:(json格式的接口可能用到)
# import json
# data = {
#     'no' : 1,
#     'name' : 'Runoob',
#     'url' : 'http://www.runoob.com'
# }
# json_str = json.dumps(data) # json解码
# print(data)
# print(json_str) # str类型
# print(json.loads(json_str)) # json转码

# mongoDB数据库 TODO:与mysql相似,一样要用连接数据库的模块,看文档使用

# import json
# print(json.loads('{"key":"value"}'))
