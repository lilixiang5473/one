
# -*- coding: UTF-8 -*-

import pymysql
from mysql_init import Operta_mysql 
import json
from rediscluster import RedisCluster #redis集群     pip install --upgrade pip


#服务器
test_startup_nodes = [
    {"host":"172.31.144.145", "port":6379},
    {"host":"172.31.144.146", "port":6379},
    {"host":"172.31.144.144", "port":6379},
    {"host":"172.31.144.145", "port":6380},
    {"host":"172.31.144.146", "port":6380},
    {"host":"172.31.144.144", "port":6380}
]
#连接Redis
r = RedisCluster(startup_nodes=test_startup_nodes, decode_responses=True)

#加钱
def add_money():
    # 遍历userid
        userid=input("请输入需要加钱的userid:")
        dict_name = 'wallet:c2c:'+userid
        coin_name_list = ['usdt','dot','bal','uni','icx','algo','btc','eth','eos','ada','bch','bnb','bsv','ckb','dash','doge','etc','link','ltc','omg','solo','sushi','tomo','trx','tt','xlm','xrp','xtz','bat']
        # print(dict_name,coin_name_list)
        """"""
        #添加所有币种
        for coin_name in coin_name_list:
            try:
                r.hincrby(dict_name, coin_name+':available', '1000000000000000')
                print({'message': 'success!'})
            except BaseException as e:
                print({'error': e})

#删除用户数据
#with open("./test_scripts/config.json",'r') as f:
with open("config.json",'r') as f:
    data=json.loads(f.read())
#数据库操作mysql_init实例化
Operta=Operta_mysql(data["host"],data["port"],data["user"],data["password"],data['db'])

def delete():
    userid=input("请输入用户id:")
    if userid == None or userid=="":
       print("userid不能为空")
    else:
        sql="DELETE FROM db_user.user_user WHERE userid="+userid+";DELETE FROM db_user.user_info WHERE userid="+userid+";DELETE FROM db_user.user_kychistory WHERE userid="+userid+";DELETE FROM db_user.user_auth WHERE userid="+userid+";DELETE FROM db_user.user_app_user WHERE userid="+userid+";delete from db_user.user_bankcard  where userid = "+userid+";delete from db_user.user_history where userid = "+userid+";delete from db_user.user_invitecode where userid = "+userid+";delete from db_user.user_withdrawadress where userid = "+userid
        Operta.delete(sql)
        Operta.close_db()

#最近一次审批通过        
def pass_approval():
    
    sql="SELECT check_id FROM db_cms_oprate.oprate_check  ORDER BY id  desc limit 1"
    result=Operta.select(sql)
    #print(result[0][0])
    update_sql="UPDATE db_cms_oprate.oprate_check SET process_id=6,is_notify=2 WHERE check_id=\""+result[0][0]+"\""
    Operta.updata(update_sql)
    Operta.close_db()


#kyc设置0    
def set_kyc0():
    userid=input("请输入用户id:")
    if userid == None or userid=="":
       print("userid不能为空")
    else:
        sql="UPDATE db_user.user_auth set userlevel=0,kyc1count=0,realname=\"\",realnamecardnum='',kyc1result=0,country=86,kyc2count=0,kyc3count=0,kyc2result=0,kyc3_file='',content='',kyc1applytime=NULL,kyc1passtime=NULL,kyc1failtime=NULL,kyc2applytime=NULL,kyc2passtime=NULL,kyc2failtime=NULL,kyc3applytime=NULL,kyc3passtime=NULL,kyc3failtime=NULL,realnamefurl=NULL,realnameburl=NULL,realnamegurl=NULL,country_data=NULL,realnamebiz_result=0 WHERE userid=\""+userid+"\""
        Operta.updata(sql)
        Operta.close_db()
#kyc设置1
def set_kyc1():
    userid=input("请输入用户id:")
    if userid == None or userid=="":
       print("userid不能为空")
    else:
        sql="UPDATE db_user.user_auth set userlevel=0,kyc1count=0,realname=\"\",realnamecardnum='',kyc1result=0,country=86,kyc2count=0,kyc3count=0,kyc2result=0,kyc3_file='',content='',kyc1applytime=NULL,kyc1passtime=NULL,kyc1failtime=NULL,kyc2applytime=NULL,kyc2passtime=NULL,kyc2failtime=NULL,kyc3applytime=NULL,kyc3passtime=NULL,kyc3failtime=NULL,realnamefurl=NULL,realnameburl=NULL,realnamegurl=NULL,country_data=NULL,realnamebiz_result=0 WHERE userid=\""+userid+"\""
        Operta.updata(sql)
        sql="UPDATE db_user.user_auth set userlevel=1,kyc1count=1,realname=\"张三\",realnamecardtype=1,realnamecardnum='411221199206266531',sex=1,kyc1result=0,country=86 WHERE userid=\""+userid+"\""
        Operta.updata(sql)
        Operta.close_db()
#kyc设置2        
def set_kyc2():
    userid=input("请输入用户id:")
    if userid == None or userid=="":
       print("userid不能为空")
    else:
        sql="UPDATE db_user.user_auth set userlevel=0,kyc1count=0,realname=\"\",realnamecardnum='',kyc1result=0,country=86,kyc2count=0,kyc3count=0,kyc2result=0,kyc3_file='',content='',kyc1applytime=NULL,kyc1passtime=NULL,kyc1failtime=NULL,kyc2applytime=NULL,kyc2passtime=NULL,kyc2failtime=NULL,kyc3applytime=NULL,kyc3passtime=NULL,kyc3failtime=NULL,realnamefurl=NULL,realnameburl=NULL,realnamegurl=NULL,country_data=NULL,realnamebiz_result=0 WHERE userid=\""+userid+"\""
        Operta.updata(sql)
        sql="UPDATE db_user.user_auth set userlevel=1,kyc1count=1,realname=\"张三\",realnamecardtype=1,realnamecardnum='411221199206266531',sex=1,kyc1result=0,country=86 WHERE userid=\""+userid+"\""
        Operta.updata(sql)
        sql="UPDATE db_user.user_auth set userlevel=2,kyc2count=1,kyc2result=1 where userid=\""+userid+"\""
        Operta.updata(sql)
        Operta.close_db()
#kyc设置3  
def set_kyc3():
    userid=input("请输入用户id:")
    if userid == None or userid=="":
       print("userid不能为空")
    else:
        sql="UPDATE db_user.user_auth set userlevel=0,kyc1count=0,realname=\"\",realnamecardnum='',kyc1result=0,country=86,kyc2count=0,kyc3count=0,kyc2result=0,kyc3_file='',content='',kyc1applytime=NULL,kyc1passtime=NULL,kyc1failtime=NULL,kyc2applytime=NULL,kyc2passtime=NULL,kyc2failtime=NULL,kyc3applytime=NULL,kyc3passtime=NULL,kyc3failtime=NULL,realnamefurl=NULL,realnameburl=NULL,realnamegurl=NULL,country_data=NULL,realnamebiz_result=0 WHERE userid=\""+userid+"\""
        Operta.updata(sql)
        sql="UPDATE db_user.user_auth set userlevel=1,kyc1count=1,realname=\"张三\",realnamecardtype=1,realnamecardnum='411221199206266531',sex=1,kyc1result=0,country=86 WHERE userid=\""+userid+"\""
        Operta.updata(sql)
        sql="UPDATE db_user.user_auth set userlevel=2,kyc2count=1,kyc2result=1 where userid=\""+userid+"\""
        Operta.updata(sql)
        Operta.close_db()
#指定审批单通过
def pass_approval1():
    approval_nub=input("请输入审批单号:")
    if approval_nub == None or approval_nub=="":
       print("审批单号不能为空")
    else:
        update_sql="UPDATE db_cms_oprate.oprate_check SET process_id=6,is_notify=2 WHERE check_id=\""+approval_nub+"\""
        Operta.updata(update_sql)
        Operta.close_db()
#修改用户手机号
def update_phone():
    userid=input("请输入userid:")
    phone=input("请输入手机号:")
    if userid == None or userid=="":
       print("userid不能为空")
    elif phone == None or phone=="":
        print("手机号不能为空")
    else:
        update_sql="UPDATE db_user.user_user set areacode=86,phone="+phone+" WHERE userid="+userid+"; UPDATE db_user.user_info set phone="+phone+",phonevalidflag=1 WHERE userid="+userid+";UPDATE db_user.user_app_user set area_code=86,phone="+phone+" WHERE userid="+userid+";UPDATE db_user.user_auth set phonevalidflag=1 WHERE userid="+userid
        Operta.updata(update_sql)
        Operta.close_db()
#修改用户手机号
def get_code():
    mail_keys=r.keys('*mail*')
    sms_keys=r.keys('*sms*')
    for i in mail_keys:
        if ':' in i :
            mail_address=i.split(':')
            if r.get(i)!="60":
                print("\n\n邮箱为",mail_address[2],"验证码为",r.get(i))
        else:
            mail_address=i.split('_')
            if r.get(i)!="60":
                print("后台验证码为",r.get(i))
    for i in sms_keys:
        phone_address=i.split(':')
        if r.get(i)!="60":
            print("\n\n手机号为",phone_address[2],"验证码为：",r.get(i))

#查询用户手机号
def get_phone():
    userid=input("请输入userid")
    sql="select phone from user_user  where userid = "+userid
    print(Operta.select(sql))

#清空账号错误5次冻结
def get_clear():
    userid=input("请输入用户UID：")
    clear_keys='USER_Login_Fail_Times_'+userid
    #修改KEY的值
    r.set(clear_keys,0)
    print(clear_keys)
    #获取KEY的值  GET   
    print(r.get(clear_keys))

#重置谷歌
def get_reset():
    userid=input("请输入用户id:")
    if userid == None or userid=="":
       print("userid不能为空")
    else:
        update_sql="UPDATE db_user.user_info set googleflag=0,googlesecuret='',googleurl='' where userid="+userid+";UPDATE db_user.user_auth set googleexist=0,googleflag=0 where userid="+userid
        Operta.updata(update_sql)
        Operta.close_db()
    #else:
     #   sql="DELETE FROM db_user.user_user WHERE userid="+userid+";DELETE FROM db_user.user_info WHERE userid="+userid+";DELETE FROM db_user.user_kychistory WHERE userid="+userid+";DELETE FROM db_user.user_auth WHERE userid="+userid+";DELETE FROM db_user.user_app_user WHERE userid="+userid+";delete from db_user.user_bankcard  where userid = "+userid+";delete from db_user.user_history where userid = "+userid+";delete from db_user.user_invitecode where userid = "+userid+";delete from db_user.user_withdrawadress where userid = "+userid
      #  Operta.delete(sql)
       # Operta.close_db()
if __name__ == "__main__":
    for i in range(0,100):
        print("\n\n\n---------测试专用改数据-------")
        print("0：加钱")
        print("1：删除用户数据")
        print("2：最近一次审批通过")
        print("3：kyc设置0")
        print("4：kyc设置为1")
        print("5：kyc设置为2")
        print("6：kyc设置为3")
        print("7：指定审批单通过")
        print("8：修改用户手机号")
        print("9：获取验证码")
        print("10:查询ID的信息项")
        print("11:清空账户冻结")
        print("12:重置谷歌")
        print("t：退出程序")
        need_nub=input("请输入功能编号:")
        print(need_nub)
        if need_nub == "0":
            add_money()
            del add_money
            del r
        elif need_nub == "1":
            delete()
        elif need_nub== "2":
            pass_approval()
        elif need_nub=="3":
            set_kyc0()
        elif need_nub=="4":
            set_kyc1()
        elif need_nub=="5":
            set_kyc2()
        elif need_nub=="6":
            set_kyc3()
        elif need_nub=="7":
            pass_approval1()
        elif need_nub=="8":
            update_phone()
        elif need_nub=="9":
            get_code()
        elif need_nub=="10":
            get_phone()
        elif need_nub=="11":
            get_clear()
        elif need_nub=="12":
            get_reset()    
        elif need_nub=="t":
            break
        else:
            print("请输入有效编号")
    



