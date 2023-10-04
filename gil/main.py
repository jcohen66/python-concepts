import logging
import time
from fastapi import FastAPI
import sys
import os

""" Gunicorn

    1 - Acts as a process manager for FastAPI application.
    2 - Ensures that the necessary number of workers are available.
"""


""" Uvicorn Workers

    1 - Obtain the listening socket from Gunicorn
    2 - Create a TCP server using the syncio low-level framework.
    3 - For every new connection, use the specified protocol
    to pass the request to the FastAPI application.
"""

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
app = FastAPI()
logger = logging.getLogger()


@app.get("/gil")
async def gil():
    start = time.time()
    logger.info(f"Running on {os.getpid()}")
    x = 1 + len(range(100000000))
    logger.info(f"Took {time.time()-start}")
