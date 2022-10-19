from datetime import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from envs import get_logger

logger = get_logger('google_reviews')

def cookie_accept_btn_exists(driver):
    try:
        cookie_accept_btn = driver.find_elements(
            By.XPATH,
            '//div[@class="VfPpkd-dgl2Hf-ppHlrf-sM5MNb"]/button[@class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 Nc7WLe"]'
        )[1]
        return cookie_accept_btn
    except:
        return False


# //*[@id="headingText"]/span



