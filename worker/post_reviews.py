import undetected_chromedriver as uc
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from envs import get_logger
from utils.button import get_button, click_on_button
from utils.wait import wait_element_for_click, wait_element_for_send, switch_to_iframe, wait_web_driver, button_click
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
        self.options.add_argument('--window-size=1920,1080')

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



    def get_review_page(self):
        self.driver.get(self.review_url)
        time.sleep(5)
        # button = self.driver.find_element(By.XPATH, '//*[@id="gb"]/div/div/div[1]/div[2]/div/a').get_attribute('title')
        # print(button)

    def open_review(self):
        time.sleep(5)
        buttons = self.driver.find_elements(By.CLASS_NAME, 'S9kvJb')
        logger.info('Open google maps')
        time.sleep(10)
        button = get_button(buttons)
        time.sleep(5)
        click_on_button(self.driver, button)
        logger.info(f'{button} to click')
        time.sleep(5)
        # click_on_button(button)
        logger.info('Click on button to leave review')
        time.sleep(3)
        switch_to_iframe(self.driver, By.NAME, 'goog-reviews-write-widget')
        time.sleep(10)
        # button = wait_web_driver(self.driver, By.XPATH, '//*[@id="kCvOeb"]/div[1]/div[3]/div/div[2]/div/div[5]')
        #
        # click_on_button(self.driver, button)
        # time.sleep(2)
        # button1 = wait_web_driver(self.driver, By.XPATH, '//*[@id="ZRGZAf"]/span')
        # click_on_button(self.driver, button1)
        time.sleep(20)
        button = self.driver.find_elements(By.CLASS_NAME, 's2xyy')
        def fast_test(button):
            for b in button:
                if b.get_attribute('data-rating') == 5:
                    return b

        if fast_test(button) == 5:
            # button_click(self.driver, By.CLASS_NAME, 's2xyy')
            self.driver.execute_script("arguments[0].click();", button)
        logger.info('web driver wait')

        # button = self.driver.find_elements(By.CLASS_NAME, 's2xyy').get_attribute('data-rating')
        # if button == 5:
        #     # button_click(self.driver, By.CLASS_NAME, 's2xyy')
        #     self.driver.execute_script("arguments[0].click();", button)
        # wait_web_driver(self.driver, By.XPATH, '//*[@id="kCvOeb"]/div[1]/div[3]/div/div[2]/div/div[5]')
        # WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kCvOeb"]/div[1]/div[3]/div/div[2]/div/div[5]'))).click()
        time.sleep(20)
        # button1 = self.driver.find_element(By.ID, 'ZRGZAf')
        # // *[ @ id = "ZRGZAf"] / span
        # button1 = self.driver.find_elements(By.XPATH, '//*[@id="ZRGZAf"]/span')
        # def fast_test_1(button):
        #     for b in button:
        #         if b.text == 'Post':
        #             return b
        # b = fast_test_1(button1)
        # self.driver.execute_script("arguments[0].click();", b)
        logger.info('web driver wait 2')
        # button = self.driver.find_element(By.ID, 'ZRGZAf')
        # wait_element_for_click(self.driver, By.ID, 'ZRGZAf')
        try:
            showmore_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ZRGZAf"]')))
            showmore_link.click()

        except Exception as e:
            logger.info(f'{e}')
            print("Trying to click on the button again")
            showmore_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ZRGZAf"]')))

            self.driver.execute_script("arguments[0].click()", showmore_link)

        # logger.info(f'{button} last element')
        # time.sleep(5)
        # wait_web_driver(self.driver, By.XPATH, '//*[@id="ZRGZAf"]/span')
        # click_on_button(self.driver, button)

        # WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(
        #     (By.ID, 'ZRGZAf'))).click()
        # wait_element_for_click(self.driver, By.XPATH, '//*[@id="kCvOeb"]/div[1]/div[3]/div/div[2]/div/div[5]')
        # time.sleep(3)
        # wait_element_for_click(self.driver, By.XPATH, '//*[@id="ZRGZAf"]/span')
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
