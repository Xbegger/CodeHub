import threading
import time

def run(n):
    print("task", n)
    time.sleep(1)
    print('2s\n')
    time.sleep(1)
    print('1s\n')
    time.sleep(1)
    print('0s\n')
    time.sleep(1)

if __name__ == '__main__':
    t1 = threading.Thread(target=run, args=("t1",))
    t2 = threading.Thread(target=run, args=("t2",))
    t1.start()
    t2.start()