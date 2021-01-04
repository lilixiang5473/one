# -*- coding: UTF-8 -*=
x=30  #当前价格
m=5    #杠杆配置倍数
a=0 	#交易币余额数量
b=149.55	    #计价币余额
c=4     #已借交易币数量
d=0 	#已借计价币数量
e_hour=2    #已借交易币小时
f_hour=0     #已借计价币小时
e=c*0.000021*e_hour	#交易币利息
f=d*0.000021*f_hour  #计价币利息
rank=1 #后台配置风险率（后台配置的爆仓风险率）

#杠杆账户我的资产计算公式： 可用+冻结-已借
#总资产
summary=a*x+b
print("总资产等于%s"%summary)
#未还借入资产
borrow=c*x+d
print("未还借入资产等于%s"%borrow)
#未还利息
interest=e*x+f
print("未还利息%s"%interest)



print("交易币利息%s"%e)
print("计价币利息%s"%f)
#可借最大计价币
max_borrow=(summary-borrow-interest)*(m-1)-borrow
print("可借最大计价币%s"%round(max_borrow,5))

#可借最大交易币
max_trad=max_borrow/x
print("可借最大交易币保留6位截取%s "%round(max_trad,9))

#风险率
risk=(summary-interest)/borrow
res = format(risk, '.4%')
print("风险率保留两位%s"%res)
if risk>3:
    print("无风险")
else:
    print("有风险")

#爆仓价
baocang=(rank*d+f-b)/(a-e-rank*c)
print("爆仓价%s"%str(baocang))


#最大可转出的计价币
roll_borrow=(summary-interest)-borrow*(m/(m-1))
print("最大可转出的计价币%s"%str(roll_borrow))

#最大可转出的交易币
roll_trad=roll_borrow/x
print("最大可转出的交易币%s" %str(roll_trad))


oo=(summary-interest)/borrow
print(oo)

#破产价格
bankruptcy_price=(d+f-b)/(a-e-c)
print("破产价格为%s"%bankruptcy_price)