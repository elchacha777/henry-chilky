import redis

class Cache:
    def __init__(self, db: int = 0):
        self.red = redis.StrictRedis(
            host='redis',
            port=6379,
            password='',
            decode_responses=True,
            db=db,
        )