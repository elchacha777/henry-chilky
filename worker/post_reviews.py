import undetected_chromedriver as uc
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from envs import get_logger
from utils.button import get_button, click_on_button
from utils.check import cookie_accept_btn_exists
from utils.wait import wait_element_for_click, wait_element_for_send, switch_to_iframe
import os
import time
from webdriver_manager.chrome import ChromeDriverManager

logger = get_logger('google_reviews')


class GoogleReviews:

    def __init__(self, review_url):
        # self.review_url = 'https://www.google.com/maps/place/%D0%9A%D0%B0%D1%84%D0%B5+%D0%A8%D0%B0%D0%BE+%D0%9B%D0%B8%D0%BD%D1%8C/@42.8898984,74.5714998,16z/data=!4m5!3m4!1s0x389ec80e8682abb3:0xafc265a98fb7e755!8m2!3d42.8883425!4d74.5761052'
        self.review_url = review_url
        self.url = 'https://accounts.google.com/ServiceLogin'
        self.options = uc.ChromeOptions()
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-setuid-sandbox")
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--disable-dev-shm-usage")


        # self.options.add_argument("--lang=en")
        self.options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})

        self.driver = uc.Chrome(use_subprocess=True, options=self.options)

    def get_page(self):
        self.driver.get(self.url)

    def login(self,email, password):
        time.sleep(2)
        print(self.driver.find_element(By.XPATH, '//*[@id="headingSubtext"]/span').text)
        time.sleep(5)
        logger.info('Google login ')
        wait_element_for_send(self.driver, By.NAME, 'identifier', email)
        time.sleep(5)
        wait_element_for_click(self.driver, By.ID, 'identifierNext')
        logger.info('Google enter email  ')
        time.sleep(5)
        wait_element_for_send(self.driver, By.NAME, 'Passwd', password)
        time.sleep(5)
        wait_element_for_click(self.driver, By.ID, 'passwordNext')
        logger.info('Google enter password ')
        time.sleep(5)
        # check_cookie(self.driver)
        time.sleep(5)

    def check_verify(self):
        def login_btn_exists(driver):
            try:
                login_btn = driver.find_element(By.XPATH, '//a[@id="gb_70"]')
                return True
            except:
                return False

    def get_review_page(self):
        self.driver.get(self.review_url)
        time.sleep(10)
        assert not self.driver.current_url.startswith('https://consent.google.com/')


        # button = self.driver.find_element(By.XPATH, '//*[@id="gb"]/div/div/div[1]/div[2]/div/a').get_attribute('title')
        # print(button)

    def open_review(self):
        cookie_accept_btn = cookie_accept_btn_exists(self.driver)

        if cookie_accept_btn:
            click_on_button(self.driver, cookie_accept_btn)
            logger.info(f'cookie_accept_btn pressed {cookie_accept_btn}')
        else:
            logger.info(f'NO COOKIE BUTTON!!!')

        time.sleep(5)
        buttons = self.driver.find_elements(By.XPATH, '//div[@class="TrU0dc kdfrQc"]/button')[-1]
        logger.info(f'{buttons}')
        time.sleep(10)

        logger.info('Open google maps')

        time.sleep(10)
        time.sleep(5)
        click_on_button(self.driver, buttons)
        logger.info(f'{buttons} to click')
        # click_on_button(button)
        logger.info('Click on button to leave review')
        time.sleep(15)
        frame = self.driver.find_element(By.XPATH, '//iframe[@class="goog-reviews-write-widget"]')
        time.sleep(7)
        self.driver.switch_to.frame(frame)
        logger.info(f'switched to frame')
        time.sleep(15)
        # button = self.driver.find_elements(By.CLASS_NAME, 's2xyy')
        b = self.driver.find_element(By.XPATH, '//*[@id="kCvOeb"]/div[1]/div[3]/div/div[2]/div/div[5]')
        try:
            b.click()
        except:
            self.driver.execute_script("var evt = document.createEvent('MouseEvents');" + "evt.initMouseEvent('click',true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0,null);" + "arguments[0].dispatchEvent(evt);", b)



        logger.info('web driver wait')


        time.sleep(20)

        parent = self.driver.find_element(By.ID, 'ZRGZAf')
        logger.info(f'{parent}')
        child = parent.find_element(By.CLASS_NAME, 'VfPpkd-RLmnJb')
        logger.info(f'{child}')

        time.sleep(5)
        self.driver.execute_script("var evt = document.createEvent('MouseEvents');" + "evt.initMouseEvent('click',true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0,null);" + "arguments[0].dispatchEvent(evt);", child)

        logger.info('Review created')

    def close_context(self=None):
        self.driver.close()

        self.driver.quit()


if __name__ == '__main__':
    emails = {

        'yeziluxaxug@gmail.com': '5LvRmDBUKThEdhr',
        'supeloviwusis@gmail.com': 'w896JL0m3c460VG'}
    for email, password in emails.items():
        attempts = 5
        while attempts:
            try:
                obj = GoogleReviews()
                obj.get_page()
                time.sleep(3)
                obj.login(email, password)
                time.sleep(7)
                obj.get_review_page()
                time.sleep(3)
                obj.open_review()
                time.sleep(5)
                obj.close_context()
                logger.info(f'{email} left a review')
            except Exception as e:
                logger.info(f'{e}')
                obj.close_context()
                logger.info(f'{email} didnt left a review')
                attempts -= 1
