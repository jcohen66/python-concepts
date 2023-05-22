import logging
import time
from fastapi import FastAPI
import sys
import os

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
app = FastAPI()
logger = logging.getLogger()


@app.get("/gil")
async def gil():
    start = time.time()
    logger.info(f"Running on {os.getpid()}")
    x = 1 + len(range(100000000))
    logger.info(f"Took {time.time()-start}")
