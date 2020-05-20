# !/usr/bin/python
# -*- coding:utf-8 -*-

from unit.base_page import BasePage

class NewsSportHome(BasePage):
    # 进入超级会员页面
    nba_link = '//*[@id="app"]/div[1]/div[1]/div[3]/div/div[1]/a[5]/span'

    # 跳转 NBA 界面
    def click_nba_link(self):
        self.click(self.nba_link)