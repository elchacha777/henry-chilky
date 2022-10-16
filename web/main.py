from fastapi import FastAPI
from pydantic import BaseModel
import redis

app = FastAPI()


class Cache:
    def __init__(self, db: int = 0):
        self.red = redis.StrictRedis(
            host='redis',
            port=6379,
            password='',
            decode_responses=True,
            db=db,
        )


cache_0 = Cache(0)


class Data(BaseModel):
    url: str

@app.post('/')
def post_url(data:Data):
    print(data.url)
    url = data.url
    cache_0.red.rpush('url', url)
    return 'Success'


