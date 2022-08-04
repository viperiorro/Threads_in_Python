import time
from threading import Lock, RLock, Semaphore


class Employee:
    def __init__(self):
        self.rate = 0
        self.age = 20
        self._lock = Lock()
        self._rlock = RLock()
        self._semaphore = Semaphore(value=5)

    def increase_salary(self):
        # self._rlock.acquire()
        # local_age = self.age
        # local_age += 1
        # time.sleep(0.5)
        # self.age = local_age
        self._semaphore.acquire()
        # with self._lock:
        local_value = self.rate
        local_value += 100
        time.sleep(0.5)
        self.rate = local_value
        self._semaphore.release()
        # self._rlock.release()
