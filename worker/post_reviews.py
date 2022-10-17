import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from envs import get_logger
from utils.button import get_button, click_on_button
from utils.wait import wait_element_for_click, wait_element_for_send, switch_to_iframe
import os
import time
from webdriver_manager.chrome import ChromeDriverManager

logger = get_logger('google_reviews')


class GoogleReviews:

    def __init__(self,review_url):
        # self.review_url = 'https://www.google.com/maps/place/%D0%A3%D0%BB%D1%83%D1%83-%D0%A2%D0%BE%D0%BE/@42.8834923,74.5868375,15.77z/data=!4m5!3m4!1s0x389ec933bd943621:0x18ab7a9e283eaf18!8m2!3d42.8844016!4d74.5792839'
        self.review_url = review_url
        self.url = 'https://accounts.google.com/ServiceLogin'
        self.options = uc.ChromeOptions()
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-setuid-sandbox")
        self.options.add_argument("--disable-extensions")
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
        print('finish')
        text = self.driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/c-wiz/c-wiz/div/div[3]/div/div/header/h1').text
        print(text)


    def get_review_page(self):
        self.driver.get(self.review_url)
        time.sleep(5)

    def open_review(self):
        time.sleep(5)
        buttons = self.driver.find_elements(By.CLASS_NAME, 'S9kvJb')
        logger.info('Open google maps')
        time.sleep(5)
        language = self.driver.execute_script("return window.navigator.userLanguage || window.navigator.language")
        logger.info(f'{language}')
        button = get_button(buttons)
        logger.info(f'{button} to click')
        time.sleep(2)
        click_on_button(button)
        logger.info('Click on button to leave review')
        time.sleep(3)
        switch_to_iframe(self.driver, By.NAME, 'goog-reviews-write-widget')
        time.sleep(2)
        wait_element_for_click(self.driver, By.XPATH, '//*[@id="kCvOeb"]/div[1]/div[3]/div/div[2]/div/div[5]')
        time.sleep(3)
        wait_element_for_click(self.driver, By.XPATH, '//*[@id="ZRGZAf"]/span')
        logger.info('Review created')

    def close_context(self=None):
        self.driver.quit()


if __name__ == '__main__':
    emails = {
        'valerija.korolevat2nd0@gmail.com': 'W6r4YejgMoRh7vu',
        'jahodogevuyi76301@gmail.com': 'VDx44W8A39n5JZW',
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
