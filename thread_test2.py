import threading
from threading import current_thread


class MyThread(threading.Thread):
    def run(self):
        print(current_thread().name, 'start')
        print('run')
        print(current_thread().name, 'stop')


t1 = MyThread()
t1.start()
t1.join()

print(current_thread().name, 'end')
