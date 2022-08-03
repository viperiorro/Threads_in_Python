from threading import Thread
from time import sleep
from typing import Callable


class CustomThread(Thread):
    def __init__(self, target: Callable, thread_id: str):
        super().__init__(target=target)
        self.__id = thread_id
        self._target = target

    def run(self) -> None:
        print(f'{self.__class__.__name__} was started with id {self.__id}')
        try:
            if self._target:
                print('START ITERATION IN CHILD TREAD')
                self._target()
        finally:
            # Avoid a refcycle if the thread is running a function with
            # an argument that has a member that points to the thread.
            print(f'DELETE {self._target}')
            del self._target


def make_tea():
    for tea in range(5):
        print(f'Tea from thread-{1}: {tea}')
        sleep(1)


thread = CustomThread(target=make_tea, thread_id=1)
thread.start()
print('FINISH')
