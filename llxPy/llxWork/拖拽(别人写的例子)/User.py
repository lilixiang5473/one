# -*- coding: utf-8 -*-

#driver.maximize_window()    #窗口最大化

import time
import random
from selenium import webdriver
from rediscluster import RedisCluster

Test_startup_nodes = [
    {"host": "10.32.1.100", "port": 6379},
    {"host": "10.32.1.101", "port": 6379},
    {"host": "10.32.1.10", "port": 6379},
    {"host": "10.32.1.100", "port": 6380},
    {"host": "10.32.1.101", "port": 6380},
    {"host": "10.32.1.10", "port": 6380}
]

r = RedisCluster(startup_nodes=Test_startup_nodes,decode_responses=True)
oldPass = "Chen0727"
newPass = "chen0727"


#登录
class DragUtil:
    def __init__(self, driver):
        self.driver = driver

    def __getRadomPauseScondes(self):
        """
        :return:随机的拖动暂停时间
        """
        return random.uniform(0.6, 0.9)

    def simulateDragX(self, source, targetOffsetX):
        # """
        # 模仿人的拖拽动作：快速沿着X轴拖动（存在误差），再暂停，然后修正误差
        # 防止被检测为机器人，出现“图片被怪物吃掉了”等验证失败的情况
        # :param source:要拖拽的html元素
        # :param targetOffsetX: 拖拽目标x轴距离
        # :return: None
        # """
        action_chains = webdriver.ActionChains(self.driver)
        # 点击，准备拖拽
        action_chains.click_and_hold(source)
        # 拖动次数，二到三次
        dragCount = random.randint(2, 3)
        if dragCount == 2:
            # 总误差值
            sumOffsetx = random.randint(-15, 15)
            action_chains.move_by_offset(targetOffsetX + sumOffsetx, 0)
            # 暂停一会
            action_chains.pause(self.__getRadomPauseScondes())
            # 修正误差，防止被检测为机器人，出现图片被怪物吃掉了等验证失败的情况
            action_chains.move_by_offset(-sumOffsetx, 0)
        elif dragCount == 3:
            # 总误差值
            sumOffsetx = random.randint(-15, 15)
            action_chains.move_by_offset(targetOffsetX + sumOffsetx, 0)
            # 暂停一会
            action_chains.pause(self.__getRadomPauseScondes())

            # 已修正误差的和
            fixedOffsetX = 0
            # 第一次修正误差
            if sumOffsetx < 0:
                offsetx = random.randint(sumOffsetx, 0)
            else:
                offsetx = random.randint(0, sumOffsetx)

            fixedOffsetX = fixedOffsetX + offsetx
            action_chains.move_by_offset(-offsetx, 0)
            action_chains.pause(self.__getRadomPauseScondes())

            # 最后一次修正误差
            action_chains.move_by_offset(-sumOffsetx + fixedOffsetX, 0)
            action_chains.pause(self.__getRadomPauseScondes())

        else:
            raise Exception("莫不是系统出现了问题？!")

        # 参考action_chains.drag_and_drop_by_offset()
        action_chains.release()
        action_chains.perform()

    def simpleSimulateDragX(self, source, targetOffsetX):
        # """
        # 简单拖拽模仿人的拖拽：快速沿着X轴拖动，直接一步到达正确位置，再暂停一会儿，然后释放拖拽动作
        # B站是依据是否有暂停时间来分辨人机的，这个方法适用。
        # :param source:
        # :param targetOffsetX:
        # :return: None
        # """

        action_chains = webdriver.ActionChains(self.driver)
        # 点击，准备拖拽
        action_chains.click_and_hold(source)
        action_chains.pause(0.2)
        action_chains.move_by_offset(targetOffsetX, 0)
        action_chains.pause(0.6)
        action_chains.release()
        action_chains.perform()


def isNeedCheckVeriImage(driver):
    if driver.find_element_by_css_selector(".geetest_panel_error").is_displayed():
        driver.find_element_by_css_selector(".geetest_panel_error_content").click()
        return True
    return False


def login(driver, password):
    driver.find_element_by_xpath('//*[@id="account"]').send_keys("Chen727518@163.com")  #获取账号文本框填写账号
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)           #获取密码文本框填写密码
    driver.find_element_by_xpath('//*[@id="LoginCont"]/span/div/div[3]/div/button').click()          #获取点击登录按钮
    time.sleep(2)

    location_box = driver.find_element_by_xpath('//*[@id="puzzleBox"]').location       #{'x': 100, 'y': 100}，获取背景图片并打印x，y的距离
    location_lost = driver.find_element_by_xpath('//*[@id="puzzleLost"]').location     #{'x': 60, 'y': 600}，获取滑动图片并打印x，y的距离
    size = location_box['x'] - location_lost['x']                                      #背景图片-滑动图片=滑动重合后的图片
    print(size)

    drag_element = driver.find_element_by_xpath('//*[@id="imgVer"]/div[2]/div[2]')     #获取滑动事件
    drat_util = DragUtil(driver)                                                       #将获取的图片存储
    drat_util.simulateDragX(drag_element, size)                                        #模拟点击滑动事件，滑动距离等于求出的size
    time.sleep(2.5)

    r.get('mail:web:chen727518@163.com:35856194:0002')
    print(r.get('mail:web:chen727518@163.com:35856194:0002'))
    # 从redis获取邮箱验证码

    r.get('sms:web:17600199676:35856194:0101')
    print(r.get('sms:web:17600199676:35856194:0101'))
    time.sleep(2)
    # 从redis获取手机验证码

    driver.find_element_by_xpath('//*[@id="emailCode"]').send_keys(r.get('mail:web:chen727518@163.com:35856194:0002'))
    time.sleep(5)
    # 输入获取的邮箱验证码

 # 点击个人中心入口
def cont(driver):
    driver.find_element_by_xpath('//*[@id="cont"]/div[1]/div[1]/div[2]/div/div/div[2]/div[3]/div[3]').click()
    time.sleep(2)

def task():
    driver = webdriver.Chrome()  # 调用浏览器
    driver.get('https://www.3q5k68.cn/user/userLogin/login')     #访问路径URL
    time.sleep(5)
    login(driver,password=oldPass)
    cont(driver)


    #修改登录密码
    driver.find_element_by_xpath('//*[@id="UserCont"]/div[2]/div/div[2]/ul/li[1]/div[2]/em/button').click()
    time.sleep(2)

    driver.find_element_by_xpath('//*[@id="oldPass"]').send_keys(oldPass)
    time.sleep(2)

    driver.find_element_by_xpath('//*[@id="newPass"]').send_keys(newPass)
    time.sleep(2)

    driver.find_element_by_xpath('//*[@id="confirm"]').send_keys(newPass)
    time.sleep(2)

    driver.find_element_by_xpath('//*[@id="cont"]/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/form/div[4]/div[2]/span').click()
    time.sleep(2)

    driver.find_element_by_xpath('//*[@id="phoneCode"]').send_keys(r.get('mail:web:chen727518@163.com:35856194:0114'))
    time.sleep(2)

    driver.find_element_by_xpath('//*[@id="cont"]/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/form/div[5]/div/div/span/button').click()
    time.sleep(35)

    login(driver, password=newPass)

    cont(driver)

#======================================================================================================================
    #绑定手机号
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div/div/div/div[2]/div/div[2]/ul/li[2]/div[2]/em/button').click()
    time.sleep(2)
    # 点击绑定手机号

    driver.find_element_by_xpath('//*[@id="phone"]').send_keys('17600199676')
    time.sleep(2)
    # 输入手机号

    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[3]/div/form/div[2]/div[2]/div/span/span').click()
    time.sleep(2)
    # 点击获取手机验证码

    driver.find_element_by_xpath('//*[@id="phoneCode"]').send_keys(r.get('sms:web:17600199676:35856194:0101'))
    time.sleep(2)
    # 输入获取的手机验证码

    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[3]/div/form/div[3]/div[2]/div/span/span').click()
    time.sleep(2)
    # 点击获取邮箱验证码

    driver.find_element_by_xpath('//*[@id="emailCode"]').send_keys(r.get('mail:web:chen727518@163.com:35856194:0101'))
    time.sleep(2)
    # 输入获取的邮箱验证码

    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[3]/div/form/div[4]/div/div/span/button').click()
    time.sleep(5)
    # 点击确认绑定按钮



    # driver.close()
    #  退出浏览器
    # pass


  # 该方法用来确认元素是否存在，如果存在返回flag=true，否则返回false
def isElementExist(driver, css):
    try:
        driver.find_element_by_css_selector(css)
        return True
    except:
        return False


if __name__ == '__main__':
    task()
