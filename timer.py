import time

for seconds in range (5, 0, -1):  # negative indexes means that you start iterating backwards, from the end to the start
    print(seconds)
    time.sleep(1)  # this takes as parameter how many seconds the method has to pause each time

print("Happy new year!")