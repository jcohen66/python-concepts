import time


def retry(max_attempts, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Attempt {attempts} failed: {e}")
                    time.sleep(delay)
            print(f"Function failed after {max_attempts} attempts")

        return wrapper

    return decorator


@retry(max_attempts=3, delay=2)
def fetch_data(url):
    print("Fetching the data...")
    # raise timeout error to simulate a server not responding
    raise TimeoutError("Server us not responding")


if __name__ == "__main__":
    fetch_data("https://example.com/data")
