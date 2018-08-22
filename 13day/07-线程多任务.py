import time
from threading import Thread
def saysorry():
    print("亲爱的，跪安了")
    time.sleep(1)
for i in range(5):
    #t = Threadinng(target=saysorry)
    #t.start()
    saysorry()
