import sys
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
import threading
import string
# import pathlib
# path = pathlib.Path(__file__).parent.resolve()

# Chạy đa luồng, nhiều tab
# Lưu dữ liệu từng tab
# giao diện (truyền link, truyền số cmt, số share)

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def facebookCmt(l, so_cmt, linkfb, path):
    print('Da luong', l)
    sleep(0.6)
    # 0. option
    option = webdriver.ChromeOptions()
    option.add_argument(f'user-data-dir={path}\\profile{l}')
    # option.add_argument(f'user-data-dir=E:\\VSCode\\CmtFb\\profile{l}')

    # option.add_argument('--app=https://www.facebook.com')
    option.add_argument('--mute-audio')
    option.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=option)
    x = l*400
    y = 10
    # browser.set_window_rect(x, y, 400, 600)
    browser.get(linkfb)
    sleep(1)
    # Cmt
    for i in range(so_cmt):
        cmt = browser.find_element(
            By.XPATH, '// *[@class="xdj266r x11i5rnm xat24cr x1mh8g0r"]')
        # đợi vài giây -> random
        s1 = random.uniform(0.3, 0.5)
        sleep(s1)
        length = random.randint(4, 7)
        cmt_cmt = get_random_string(length)
        cmt.send_keys(cmt_cmt)
        s2 = random.uniform(0.1, 0.2)  # delay ->enter
        sleep(s2)
        cmt.send_keys(Keys.ENTER)
    # sleep(7200)
    # sys.exit()


def close_cmt():
    facebookCmt.browser.close()

# soluong = 1
# so_cmt = 10
# threads = []
# for l in range(soluong):
#     threads += [threading.Thread(target=data, args={l, so_cmt},)]
# for t in threads:
#     t.start()
# for t in threads:
#     t.join()
# print("end daluong")
