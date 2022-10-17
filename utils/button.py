import time

from envs import get_logger

logger = get_logger('google_reviews')

def get_button(buttons):
    attempts = 20
    while attempts:
        try:
            for button in buttons:
                review = button.get_attribute('data-value')
                if review == 'Оставить отзыв':
                    time.sleep(1)
                    return button
                elif review == 'Write a review':
                    time.sleep(1)
                    return button
        except Exception as e:
            logger.info(f'{e}')
            attempts -= 1
            time.sleep(1)
    raise 'No found required button'

# def get_button_en(buttons):
#     attempts = 20
#     while attempts:
#         try:
#             for button in buttons:
#                 review = button.get_attribute('data-value')
#                 if review == 'Write a review':
#                     time.sleep(1)
#                     return button
#         except:
#             attempts -= 1
#             time.sleep(1)
#     raise 'No found required button'

def click_on_button(button):
    attempts = 20
    while attempts:
        try:
            button.click()
            return True
        except Exception as e:
            logger.info(f'{e}')
            attempts -= 1
            time.sleep(1)
    raise 'Cant click on button'