import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
chromedriver="C:\webdriver\chromedriver"
driver=webdriver.Chrome(executable_path="C:\webdriver\chromedriver")
driver.get("https://web.whatsapp.com/")
driver.maximize_window()


input("scan the Qr Code of whatapp")
#name=input(("Enter the group name"))
#send_message(name)
while(True):
    name=input(("Enter the group name"))
    msg=input("Enter the message")
    count=int(input("Enter the count"))
    c=driver.find_element_by_xpath("//span[@title]")
    print(c)
    l=[c]
    print(l)
    user=driver.find_element_by_xpath("//span[@title='{}']".format(name))
    print(user.is_enabled())
    user.click()
    print("yooo")
    x=input("Press any key")
    msg_box=driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
    for i in range(count):
        msg_box.send_keys(msg)
        xn=driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button")
        xn.click()
    print("do you want to send more message (y/n)")
    ch=input()
    if(ch=='N')or ch=='n':
        break
print("success")

