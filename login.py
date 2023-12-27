import sys
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
import threading
# Chạy đa luồng, nhiều tab
# Lưu dữ liệu từng tab
# giao diện (truyền link, truyền số cmt, số share)
# import pathlib
# path = pathlib.Path(__file__).parent.resolve()

def data(l, path):
    print('Da luong', l)
    sleep(0.6)
    # 0. option
    option = webdriver.ChromeOptions()
    # option.add_argument(f'user-data-dir=E:\\VSCode\\CmtFb\\profile{l}')
    option.add_argument(f'user-data-dir={path}\\profile{l}')



    # option.add_argument('--app=https://www.facebook.com')
    option.add_argument('--mute-audio')
    option.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=option)
    x = l*400
    y = 10
    browser.set_window_rect(x, y, 400, 600)
    browser.get("https://www.facebook.com")
    sleep(3600)
    sys.exit()


# soluong = 4
# threads = []
# for l in range(soluong):
#     threads += [threading.Thread(target=data, args={l},)]
# for t in threads:
#     t.start()
# for t in threads:
#     t.join()
# print("end daluong")

# option.add_argument('--incognito')


# 1. Khai báo browser
# browser = webdriver.Chrome(executable_path="./chromedriver.exe")


# 2. Mở thử một trang web


# 2a. Điền thông tin vào ô user và pass
# txt_email = browser.find_element(By.ID, "email")
# txt_email.send_keys("100074275880694")
# txtPass = browser.find_element(By.ID, "pass")
# txtPass.send_keys("anhhieu88886666")
# txtPass.send_keys(Keys.ENTER)

# Lặp cmt
# for i in range(10):
#     cmt = browser.find_element(By.XPATH,'//p[@class="kmwttqpk kjdc1dyq l7ghb35v m8h3af8h"]')
#     # đợi vài giây -> random
#     s = random.uniform(0.7, 1.2)  #nhanh
#     sleep(s)
#     # random cmt
#     cmt.send_keys("123123   ")

#     # cmt.send_keys(Keys.ENTER)
# sleep(1)
# share
# share = browser.execute_script('document.querySelector(".bdao358l.om3e55n1.g4tp4svg.alzwoclg.jg3vgc78.cgu29s5g.i15ihif8.aeinzg81.jcxyg2ei.i85zmo3j.sr926ui1.jl2a5g8c.aesu6q9g.e4ay1f3w.srn514ro.hnay576k.rng1terr.ktovzxj4.g1smwn4j.kcpho0er.qm54mken > div:nth-child(1)").click()')


# 3. Dừng chương trình 5 giây
# sleep(5)

# 4. Đóng trình duyệt
# browser.close()
