# bailisha-selenium
自动测试用例
#coding = utf-8
from selenium import webdriver
from time import sleep, ctime
import os

options = webdriver.ChromeOptions()
#Chrome浏览器可执行文件的地址
options.binary_location = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chrome.exe"
#浏览器驱动地址
chrome_driver_binary = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_binary,chrome_options=options)
#要测试的网页，打开网页
driver.get("http://www.baidu.com")
#睡3秒
sleep(3)
#在网页上选择对应组件点击检查，查看组件的id号
#找到id为“kw”的控件，输入测试文本
driver.find_element_by_id("kw").send_keys("Test search")
#找到id为“su”的控件，模拟鼠标点击
driver.find_element_by_id("su").click()
sleep(3)
#推出
driver.quit()
