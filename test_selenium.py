#coding = utf-8
from selenium import webdriver
from time import sleep, ctime
import os
import pytest

options = webdriver.ChromeOptions()
#Chrome浏览器可执行文件的地址
options.binary_location = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chrome.exe"
#浏览器驱动地址
chrome_driver_binary = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

class TestClass():
    def teardown_class(self):
        sleep(3)
        # 退出浏览器
        driver.quit()
    def setup_method(self):
        # 要测试的网页，打开网页
        driver.get("http://www.baidu.com")
        sleep(2)
    def teardown_method(self):
        # 找到id为“su”的控件，模拟鼠标点击
        driver.find_element_by_id("su").click()
        sleep(3)
    #字母
    def test_one(self):
        #在网页上选择对应组件点击检查，查看组件的id号
        #找到id为“kw”的控件，输入测试文本
        driver.find_element_by_id("kw").send_keys("Testsearch")
    #空格
    def test_two(self):
        driver.find_element_by_id("kw").send_keys(" ")
    #汉字
    def test_tree(self):
        driver.find_element_by_id("kw").send_keys("淘宝")
    #数字
    def test_four(self):
        driver.find_element_by_id("kw").send_keys("1243353")
    #字母+空格
    def test_five(self):
        driver.find_element_by_id("kw").send_keys("Test search")
    #数字+空格
    def test_sex(self):
        driver.find_element_by_id("kw").send_keys("1234 124")
    #中文+空格
    def test_seven(self):
        driver.find_element_by_id("kw").send_keys("你好 不好")
    #字母+数字
    def test_eight(self):
        driver.find_element_by_id("kw").send_keys("123tygfg212")
    #字母+中文
    def test_night(self):
        driver.find_element_by_id("kw").send_keys("sahsja你好fdf你好")
    # 数字+中文
    def test_ten(self):
        driver.find_element_by_id("kw").send_keys("12121你21121好你好")
    #字母+数字+中文
    def test_eleven(self):
        driver.find_element_by_id("kw").send_keys("121sdsd21你2112asd1好你sadsds好")
    #超长字符串
    def test_twelve(self):
        driver.find_element_by_id("kw").send_keys("121sdsd21你2112asd1好你sashjdgjsgsajdsdjdadsadadsadsadsvcbhdfsdsagjshgfhjtwygejwgrywqutywr的萨哈讲的故事好的教科书的就开始打闪电借款大嘎哈坚实的各环节说过的话时间啊僵尸国度好几十个的机会数据结构好的故事讲的故事价格多少手机还是广东省是广东省dsds好")