# !/usr/bin/python
# -*- coding:utf-8 -*-

""""""
import time
from unit.base_page import BasePage

"""
 页面类，主要存放页面的元素定位和简单的操作函数.
 页面类主要是元素定位和页面操作写成函数，以供测试类使用
 集成 BasePage 二次封装通用类
 通常 1个页面为一个类
"""
# 百度首页类
class BaiduHomePage(BasePage):
    # 百度首页
    search_click = '//*[@id="app"]/div[1]/div[1]/div[3]/div/div[1]/div/p/i'
    input_box = '//*[@id="app"]/div[1]/div[1]/div[3]/div/div[1]/div/div/div/input'
    search_submit_btn = '//*[@id="app"]/div[1]/div[1]/div[3]/div/div[1]/div/div/div/span/span/i[2]'


# --------------------------------------------------------
    #点击搜索按钮
    def click_btn(self,text):
        self.click(self.search_click)  #传递点击搜索按钮的值

    # 文本内容输入
    def type_search(self,text):
        self.send_keys(self.input_box,text) # 传递文本框 id 和 内容

    # 按钮点击
    def send_submit_btn(self):
        self.click(self.search_submit_btn) # 传递百度一下按钮 xpath

# --------------------------------------------------------


    # 点击视频教程，输入搜索课程
    sports_link = '//*[@id="app"]/div[1]/div[1]/div[3]/div/div[1]/a[3]/span'
    input_box2 = "id=>ww"
    search_submit_btn2 = "id=>s_btn_wr"

    # 跳转体育新闻界面
    def click_sports_link(self):
        self.click(self.sports_link)
        time.sleep(2)

    # 新闻界面文本框输入
    def new_type_search(self):
        self.clear(self.input_box2)

    # 新闻界面搜索按钮点击
    def new_btn_click(self):
        self.click(self.search_submit_btn2)

# -----------------------------------------------------------



