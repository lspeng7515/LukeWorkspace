from time import sleep
import traceback
import time, sys


class huoche(object):
    driver_name = ''
    executable_path = ''
    # 用户名 ，密码
    username = u"xxx"
    passwd = u"xxx"
    # cookies自己去找
    starts = u"%u6C88%u9633%2CSYT"
    ends = u"%u54C8%u5C14%u6EE8%2CHBB"

    # 时间格式
    dtime = u"2019-1014"
    # 车次，选择第几趟
    order = 0
    # 乘客名
    users = [u"xxx", u"xxx"]
    # 席位
    xb = u"二等座"
    pz = u"成人票"

    """网址"""
    ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init"
    login_url = "https://kyfw.12306.cn/otn/login/init"
    initmy_url = "https://kyfw.12306.cn/otn/index/initMy12306"
    buy = "https://kyfw.12306.cn/otn/confirmPassenger/initDc"

    def __init__(self):
        self.driver_name = 'chrome'
        self.executable_path = "D:/chromedirver"

    def login(self):
        self.driver.visit(self.login_url)
        self.driver.fill("loginUserDTO.user_name", self.username)
        # sleep(1)
        self.driver.fill("userDTO.password", self.passwd)
        print(u"等待验证码，自行输入")
        while True:
            if self.driver.url != self.initmy_url:
                sleep(1)
            else:
                break

    def start(self):
        self.driver = Browser
