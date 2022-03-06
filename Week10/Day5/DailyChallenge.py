# TASK: Modules
import urllib.request
from time import time


def load_time(url):
    """
        Using the requests and time modules,
        create a function which returns the amount of time it takes a webpage to load
        (how long it takes for a complete response to a request).
        Test your code with multiple sites such as google, ynet, imdb, etc.
    """
    stream = urllib.request.urlopen(url)
    start_time = time()
    stream.read()
    end_time = time()
    stream.close()
    print(round(end_time - start_time, 3))


if __name__ == '__main__':
    load_time('https://www.google.co.il')
    load_time('https://www.ynet.co.il')
    load_time('https://www.imdb.com/')
