import time
import random
import threading
# def fn():
#     result={}
#     a = 0
#     for x in range(5):
#         result['key'] = random.randint(1, 100)
#         time.sleep(3)
#         a+=result['key']
#     return a
# print(fn())

def api(result):
    time.sleep(3)
    result['key'] = random.randint(1, 100)

def fn():
    num=0
    for x in range(5):
        res={}
        api(res)
        num=res['key']+num
    print(num)
#fn()


def experiment():
    threads = []
    x = 0
    for _ in range(5):
        result = {}
        t = threading.Thread(target=api, args=(result,))
        t.start()
        threads.append([t, result])
    thread_number = 1
    for thread, result in threads:
        thread.join()
        x+=result['key']
        print("Поток " + str(thread_number) + ' вернул ' + str(result['key']))
        thread_number = thread_number + 1
    print(x)
if __name__ == "__main__":
    experiment()