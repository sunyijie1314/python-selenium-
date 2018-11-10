# -*- coding: UTF-8 -*-
import time
from selenium import webdriver


def time_break():
    time.sleep(3)

def switch_handle(driver):
    if driver.current_window_handle==driver.window_handles[0]:
        driver.switch_to.window(driver.window_handles[1])
    else:
        driver.switch_to.window(driver.window_handles[0])

def isElementExist(title):
    address='/番剧/'+title
    new_address="//span[@data-file-path=\'"+address+"\']/.."
    try:
        driver.find_element_by_xpath(new_address).click()
        return True
    except:
        return False

def isAnimeExist():
    try:
        driver.find_element_by_link_text("番剧")
        return True
    except:
        return False

def login_mikan(driver,account,password):
    driver.get("https://mikanani.me/")
    driver.find_element_by_css_selector("div#user-login>a:nth-child(2)").click()
    driver.find_element_by_id("login-popover-input-username").send_keys(account)
    driver.find_element_by_id("login-popover-input-password").send_keys(password)
    driver.find_element_by_id("login-popover-submit").click()

def login_pan(driver,account,password):
    newwindow = 'window.open("https://pan.baidu.com/");'
    driver.execute_script(newwindow)
    switch_handle(driver)
    time_break()
    driver.find_element_by_id("TANGRAM__PSP_4__footerULoginBtn").click()
    time_break()
    driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys(account)
    time_break()
    driver.find_element_by_id("TANGRAM__PSP_4__password").send_keys(password)
    time_break()
    driver.find_element_by_id("TANGRAM__PSP_4__submit").click()
    time_break()
    driver.refresh()
    time_break()
    driver.refresh()
    time_break()
    if not isAnimeExist():      #是否存在番剧文件夹
        time_break()
        driver.find_element_by_xpath("//div[@class='tcuLAu']/a[1]/span").click()      #点击新建文件夹
        time_break()
        driver.find_element_by_xpath("//input[@class='GadHyA']").send_keys("番剧")      #用番剧名取名
        time_break()
        driver.find_element_by_xpath("//span[@class='amppO4EQ']").click()     #点击√确认
    time_break()
    driver.find_element_by_xpath("//div[@class='tcuLAu']//a[2]//span").click()      #点击离线下载
    #driver.refresh()
    #time_break()

def manage(driver,Link):
    switch_handle(driver)
    driver.refresh()
    title=driver.find_element_by_css_selector("div#an-list-res>div:nth-child(1)>div>div:nth-child(2)>div>a").get_attribute('textContent') #作品名称
    Title=driver.find_element_by_xpath("//div[@id='an-list-res']/div[1]/div/div[2]/a[1]").get_attribute('textContent')  #剧集名名称
    link=driver.find_element_by_xpath("//a[@class='js-magnet magnet-link w-other-c rss-episode-name']").get_attribute('data-clipboard-text')    #下载链接
    switch_handle(driver)
    if not Link==link:
        time_break()
        driver.find_element_by_xpath("//a[@id='_disk_id_2']//span[1]").click()      #点击新建任务
        time_break()
        driver.find_element_by_link_text("更改").click()          #点击更改
        time_break()
        driver.find_element_by_xpath("//span[@data-file-path='/番剧']/..").click()        #选择番剧
        time_break()
        if not isElementExist(title):       #是否存在该作品文件夹
            driver.find_element_by_xpath("//div[@id='fileTreeDialog']//div[3]//a[3]//span").click()     #点击新建文件夹
            time_break()
            driver.find_element_by_xpath("//li[@id='plus-createFolder']//div//span//span//input").send_keys(title)      #用番剧名取名
            time_break()
            driver.find_element_by_xpath("//li[@id='plus-createFolder']//div//span//span//span[1]").click()     #点击√确认
            time_break()
        driver.find_element_by_xpath("//div[@id='fileTreeDialog']//div[3]//a[3]//span").click()     #点击新建文件夹
        time_break()
        driver.find_element_by_xpath("//li[@id='plus-createFolder']//div//span//span//input").send_keys(Title)      #用剧集名取名
        time_break()
        driver.find_element_by_xpath("//li[@id='plus-createFolder']//div//span//span//span[1]").click()     #点击√确认
        time_break()
        driver.find_element_by_xpath("//div[@id='fileTreeDialog']//div[3]//a[2]//span").click()     #点击确定
        time_break()
        driver.find_element_by_id("share-offline-link").send_keys(link)         #输入链接
        time_break()
        driver.find_element_by_xpath("//div[@id='newoffline-dialog']//div[3]//a[2]//span").click()      #点击确定
        time_break()
        driver.find_element_by_xpath("//div[@id='offlinebtlist-dialog']//div[3]//a[2]//span").click()       #点击下载
        time_break()
    return link    

if __name__ == "__main__":
    #大于991px的宽度
    mikan_account="mikan账号"
    mikan_password="mikan密码"
    pan_account="百度云账号"
    pan_password="百度云密码"
    Link=" "
    driver = webdriver.Chrome()
    driver.maximize_window()
    login_mikan(driver,mikan_account,mikan_password)
    login_pan(driver,pan_account,pan_password)
    while True:
        time.sleep(30)
        Link=manage(driver,Link)




