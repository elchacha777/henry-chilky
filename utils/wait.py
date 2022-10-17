from selenium.webdriver.common.by import By
import time
from envs import get_logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
logger = get_logger('google_reviews')


def wait_element_for_send(driver, by, element, data):
    attempts = 20
    while attempts:
        try:
            input_email = driver.find_element(by, element)
            input_email.send_keys(data)
            logger.info('Send data')
            return True
        except Exception as e:
            logger.info(f'{e}')
            attempts -= 1
            time.sleep(1)
    raise 'Error while wait_element_for_send'

def wait_element_for_click(driver, by, element):
    attempts = 20
    while attempts:
        try:
            input_email = driver.find_element(by, element)
            input_email.click()
            logger.info('Click on button')
            return True
        except Exception as e:
            logger.info(f'{e}')
            attempts -= 1
            time.sleep(1)
    raise 'Error while wait_element_for_click'

def switch_to_iframe(driver, by, element):
    attempts = 20
    while attempts:
        try:
            driver.switch_to.frame(driver.find_element(by, element))
            logger.info('Switch to frame')
            return True
        except Exception as e:
            logger.info(f'{e}')
            attempts -= 1
            time.sleep(1)
    raise 'Error while switch_to_iframe'


def wait_web_driver(driver, by, xpath):
    attempts = 20
    while attempts:
        try:
            element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((by, xpath)))
            return element
        except Exception as e:
            logger.info(f'{e}')
            attempts -= 1
            time.sleep(1)
    raise 'Error while wait'

