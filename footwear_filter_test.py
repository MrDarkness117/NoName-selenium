from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.store_page import Footwear
import time

map_xoffset = 0
map_yoffset = 10

options = Options()
browser = webdriver.Chrome(options=options)
browser.set_window_position(0, 0)
browser.maximize_window()

noone = Footwear(driver=browser)
noone.go()

try:
    noone.region_confirm.click()
except Exception:
    print("Region selection didn't appear")
    try:
        noone.region_confirm_manual.click()
        noone.region_confirm_manual_rus.click()
    except Exception:
        print("No region selection available")

noone.store_filter.click()

try:
    noone.store_ads.click()
except Exception:
    print("Ads didn't appear")
noone.store_map.hover_center_and_click()
try:
    noone.checkbox_last.click()
except Exception:
    print("Checkbox blocked!!! See SHOW button!")

try:
    noone.store_filter_show_filtered.click()

except Exception:
    print("Can't find the SHOW button, closing.")
    try:
        noone.store_filter_close.click()
    except Exception:
        print("Clicked SHOW button while attempting to click checkbox")

print("Completed, terminating.")

time.sleep(3)

browser.close()
