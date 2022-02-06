import sys
import time
import threading
import requests
from bs4 import BeautifulSoup

bars = ["/", "-", "\\", "|"]
barsIdx = 0


def updateText():
    global barsIdx
    barsIdx += 1
    if barsIdx > 3:
        barsIdx = 0
    sys.stdout.write('\r')
    sys.stdout.write("[%s]: Product not on sale yet ..." %
                     (bars[barsIdx]))
    sys.stdout.flush()
    threading.Timer(.5, updateText).start()


updateText()

while True:
    page = requests.get("https://www.digitec.ch/LiveShopping/109")
    soup = BeautifulSoup(page.content, 'html.parser')
    print("Writing...\n")
    f = open("demofile2.txt", "a")
    f.write(str(page.content))
    f.close()
    print(soup.find_all('article', class_='liveshoppingProduct'))
    break
    time.sleep(3)
