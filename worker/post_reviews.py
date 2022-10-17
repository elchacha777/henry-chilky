import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from envs import get_logger
from utils.button import get_button, click_on_button
from utils.wait import wait_element_for_click, wait_element_for_send, switch_to_iframe, wait_web_driver
import os
import time
from webdriver_manager.chrome import ChromeDriverManager

logger = get_logger('google_reviews')


class GoogleReviews:

    def __init__(self, review_url):
        # self.review_url = 'https://www.google.com/maps/place/Maroush+Park+Royal/@51.5313201,-0.280724,15.11z/data=!4m13!1m7!3m6!1s0x47d8a00baf21de75:0x52963a5addd52a99!2z0JvQvtC90LTQvtC9LCDQktC10LvQuNC60L7QsdGA0LjRgtCw0L3QuNGP!3b1!8m2!3d51.5072178!4d-0.1275862!3m4!1s0x4876115d05c8d531:0x540c94266558ed3e!8m2!3d51.5341256!4d-0.2672221'
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

        wait_web_driver(self.driver, By.XPATH, '//*[@id="kCvOeb"]/div[1]/div[3]/div/div[2]/div/div[5]')
        # WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kCvOeb"]/div[1]/div[3]/div/div[2]/div/div[5]'))).click()
        time.sleep(3)
        wait_web_driver(self.driver, By.XPATH, '//*[@id="ZRGZAf"]/span')

        # WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
        #     (By.XPATH, '//*[@id="ZRGZAf"]/span'))).click()
        # wait_element_for_click(self.driver, By.XPATH, '//*[@id="kCvOeb"]/div[1]/div[3]/div/div[2]/div/div[5]')
        time.sleep(3)
        # wait_element_for_click(self.driver, By.XPATH, '//*[@id="ZRGZAf"]/span')
        logger.info('Review created')

    def close_context(self=None):
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
