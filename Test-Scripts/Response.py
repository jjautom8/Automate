import threading
import requests
import time

def check_website(url):
    try:
        response = requests.get(url)
        print(f"{url} is UP! Status code: {response.status_code}")
    except requests.exceptions.RequestException:
        print(f"{url} is DOWN!")

websites = [
    "https://example.com",
    "https://google.com",
    "https://nonexistentwebsite.com"
]

threads = []

for website in websites:
    thread = threading.Thread(target=check_website, args=(website,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Website status check completed.")
