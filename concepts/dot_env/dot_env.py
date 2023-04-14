from dotenv import load_dotenv
import os


load_dotenv('.env')

username: str = os.getenv('USERNAME')
password: str = os.getenv('PASSWORD')
api_pipkey: str = os.getenv("API_KEY")


def api_call(url: str, *, key: str) -> str:
    return '/'.join([url, key])


result: str = api_call('www.helloworld.com', key=api_key)
print(result)
