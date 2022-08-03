from threading import Thread
from time import sleep


def make_tea():
    for tea in range(5):
        # print(f'Thread-1: {tea}')
        sleep(0.1)


thread = Thread(target=make_tea, name='TEST_THREAD')
print(f'Thread_name: {thread.getName()} before start')
print(f'{thread.is_alive()} before start')
thread.setDaemon(False)
print(str(thread.isDaemon()) + ' is daemon before start')
# thread.setName('NEW_NAME')
print(str(thread.native_id) + ' native ID before START')
thread.start()
print('START')
print(str(thread.ident) + ' ID ')
print(str(thread.isDaemon()) + ' is daemon after start')
thread.setName('NEW_NAME')
print(f'{thread.is_alive()} after start')
print(f'Thread_name: {thread.getName()} after start')
print(thread.name + ' from property')
print(str(thread.isDaemon()) + ' is deamon')
print(str(thread.native_id) + ' native ID after START')

# for tea in range(5):
#     print(f'Tea from main thread number {tea}')
#     sleep(2)

print('FINISH')
sleep(5)
print(f'{thread.is_alive()} after Finish')
print(str(thread.native_id) + ' native ID after FINISH')
