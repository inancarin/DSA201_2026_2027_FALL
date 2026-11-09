import clock as c
import time

myClock = c.Clock(23, 59, 50)
print(myClock)
for i in range(60):
    time.sleep(1)
    myClock.tick()
    print(myClock)