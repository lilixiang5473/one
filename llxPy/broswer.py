# 操作浏览器

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains # 鼠标事件

driver = webdriver.Chrome()
driver.get("https://www.fameex.com")

def eleDragFunc(driver,targetPath,startPath,endPath):
    # driver.switch_to.frame("x-URS-iframe")
    actions = ActionChains(driver)
    
    target = driver.find_elements_by_xpath(targetPath)[0]
    start = driver.find_elements_by_xpath(startPath)[0]
    end = driver.find_elements_by_xpath(endPath)[0]
    x1 = start.location.get('x')
    x2 = end.location.get('x')
    print(x2 - x1)
    # 拖拽到指定元素位置
    # actions.drag_and_drop(target, end)
    # 拖拽到指定位置
    actions.drag_and_drop_by_offset(target,x2 - x1,0)
    # 执行
    actions.perform()

if driver.find_elements_by_xpath("//*[text()='登录']")[0]:
    driver.find_elements_by_xpath("//*[text()='登录']")[0].click()
    
    time.sleep(3)
    driver.find_elements_by_xpath('//*[@id="account"]')[0].send_keys("jy547311291@sina.com")
    driver.find_elements_by_xpath('//*[@id="password"]')[0].send_keys("lilixiang123")

    driver.find_elements_by_xpath('//*[@id="LoginCont"]/span/div/div[3]/div/div[2]/div/label/span[1]/input')[0].click()
    driver.find_elements_by_xpath('//*[@id="LoginCont"]/span/div/div[3]/div/button')[0].click()
    
    time.sleep(2)
    eleDragFunc(driver,'//*[@id="imgVer"]/div[2]/div[2]','//*[@id="puzzleLost"]','//*[@id="puzzleBox"]')

    

# if driver.find_elements_by_xpath("//*[@id='account']")[0]:
# driver.find_element_by_css_selector(".box div div div div div div button").click()
