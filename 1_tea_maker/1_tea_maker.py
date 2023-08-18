from time import sleep


def make_tea():
    for tea in range(5):
        print(f'From main Thread make tea number: {tea}')
        sleep(0.5)


make_tea()

for i in range(5):
    print(f'From main Thread global make tea number: {i}')
    sleep(1)

print('FINISH')
