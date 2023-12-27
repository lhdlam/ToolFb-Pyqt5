from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
import string
# Chạy đa luồng, nhiều tab
# Lưu dữ liệu từng tab
# giao diện (truyền link, truyền số cmt, số share)

# 0. option
option = webdriver.ChromeOptions()
option.add_argument(f'user-data-dir=/home/lamle/LeHaiLam/ToolFb/facebook/profile1')
option.add_argument('--mute-audio')
option.add_experimental_option('excludeSwitches', ['enable-logging'])
# option.add_argument('--app=https://www.facebook.com')
# option.debugger_address = '127.0.0.1:2222'
# option.add_argument('--incognito')
browser = webdriver.Chrome(options=option)
browser.set_window_size(400, 600)
# 1. Khai báo browser
# browser = webdriver.Chrome(executable_path="./chromedriver.exe")


# 2a. Điền thông tin vào ô user và pass
# txt_email = browser.find_element(By.ID, "email")
# txt_email.send_keys("100074275880694")
# txtPass = browser.find_element(By.ID, "pass")
# txtPass.send_keys("anhhieu88886666")

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


# 2. Mở thử một trang web
browser.get("https://www.facebook.com/")

sleep(1000)
if input() == "-":
    browser.quit()
# Lặp cmt
for i in range(3):
    cmt = browser.find_element(
        By.XPATH, '// *[@class="xdj266r x11i5rnm xat24cr x1mh8g0r"]')
    # đợi vài giây -> random
    s1 = random.uniform(0.3, 0.7)
    sleep(s1)
    length = random.randint(4, 7)
    cmt_cmt = get_random_string(length)
    cmt.send_keys(cmt_cmt)
    s2 = random.uniform(0.4, 0.6)  # delay ->enter
    sleep(s2)
    cmt.send_keys(Keys.ENTER)

# share
share = browser.find_element(
    By.XPATH, '// *[@class="x9f619 x1n2onr6 x1ja2u2z x78zum5 x1r8uery x1iyjqo2 xs83m0k xeuugli xl56j7k x6s0dn4 xozqiw3 x1q0g3np xn6708d x1ye3gou xexx8yu xcud41i x139jcc6 x4cne27 xifccgj xn3w4p2 xuxw1ft"]').clicks()

# 3. Dừng chương trình 5 giây
sleep(5)

# 4. Đóng trình duyệt
browser.close()
