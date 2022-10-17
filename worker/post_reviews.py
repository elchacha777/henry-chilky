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

    def __init__(self, review_url):
        # self.review_url = 'https://www.google.com/maps/place/%D0%9A%D1%83%D1%80%D0%BC%D0%B0%D0%BD+%D0%9A%D0%B0%D1%84%D0%B5+%D0%9A%D0%B5%D0%BD%D1%87/@42.9174501,74.6297435,16.92z/data=!4m12!1m6!3m5!1s0x0:0xdb9a5b5ad899367e!2z0J_QsNC9INCQ0LfQuNCw0YI!8m2!3d42.8736383!4d74.5808161!3m4!1s0x389eb98ae7b1ed75:0x5d3b4c20063735b7!8m2!3d42.9191705!4d74.6316092'
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



    def get_review_page(self):
        self.driver.get(self.review_url)
        time.sleep(5)
        button = self.driver.find_element(By.XPATH, '//*[@id="gb"]/div/div/div[1]/div[2]/div/a').get_attribute('title')
        print(button)

    def open_review(self):
        time.sleep(5)
        buttons = self.driver.find_elements(By.CLASS_NAME, 'S9kvJb')
        logger.info('Open google maps')
        time.sleep(5)
        language = self.driver.execute_script("return window.navigator.userLanguage || window.navigator.language")
        logger.info(f'{language}')
        button = get_button(buttons)
        time.sleep(5)
        click_on_button(self.driver, button)
        logger.info(f'{button} to click')
        time.sleep(5)
        # click_on_button(button)
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
