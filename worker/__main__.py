from db.orm import get_all_emails, get_email
from utils.rs import Cache
from worker.post_reviews import GoogleReviews
import time
from envs import get_logger
import os
logger = get_logger('google_reviews')


class Worker:

    def __init__(self):
        self.cache = Cache(0)
        self.google_reviews = None

    def main(self, url):

        _id = 1

        for i in range(get_all_emails() + 1):


            # print(_id)
            attempts = 2
            logger.info(f'{attempts} for email with id:{_id}')
            while attempts:
                try:
                    logger.info(f'attempts {attempts}')
                    obj = GoogleReviews(url)
                    obj.get_page()
                    time.sleep(3)
                    logger.info(f'id:{_id}')
                    (email, password) = get_email(_id)
                    obj.login(email, password)
                    logger.info(f'{email} started')
                    time.sleep(7)
                    obj.get_review_page()
                    time.sleep(3)
                    obj.open_review()
                    time.sleep(5)
                    obj.close_context()
                    logger.info(f'{email} left a review')
                    _id +=1
                    time.sleep(30)
                    break
                except Exception as e:
                    logger.info(f'{e}')
                    obj.close_context()
                    logger.info(f'{email} didnt left a review')
                    attempts -=1
                    if attempts == 0:
                        _id += 1
                        break







    def run(self):
        while True:
            url = self.cache.red.lpop('url')
            if url != None:
                self.main(url)
            continue


if __name__ == '__main__':
    worker = Worker()
    worker.run()
