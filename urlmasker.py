import time
from urllib.parse import urlparse
import pyshorteners

s = pyshorteners.Shortener()

shorteners = [
    s.tinyurl,
    s.dagd,
    s.clckru,
    s.osdb,
]



# Colors

R = '\033[31m'; G = '\033[32m'; Y = '\033[33m'; C = '\033[36m'; W = '\033[0m'

s = pyshorteners.Shortener()
shorteners = [s.tinyurl, s.dagd, s.clckru, s.osdb]

def mask_url(domain, keyword, url):
    parsed_url = urlparse(url)
    return f"{parsed_url.scheme}://{domain}-{keyword}@{parsed_url.netloc}{parsed_url.path}"

def show_loading_screen():
    print(f"{C}Generating masked URLs, please wait...{W}")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\n")

def generate_masked_urls(web_url, custom_domain, keyword):
    short_urls = []
    for i, shortener in enumerate(shorteners):
        try:
            short_url = shortener.short(web_url)
            short_urls.append(mask_url(custom_domain, keyword, short_url))
        except Exception as e:
            print(f"{R}Error with Shortener {i+1}: {W}{str(e)}")
    return short_urls
