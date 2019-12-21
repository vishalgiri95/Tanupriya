from functools import lru_cache
import time

@lru_cache()
def info():
    time.sleep(2)
    return "This is info 1"

def info2():
    time.sleep(2)
    return "This is info 2"


print(info())
print(info2())
print(info())
print(info())
print(info())

print(info())
print(info())
print(info())
print(info())
print(info())
print(info2())


