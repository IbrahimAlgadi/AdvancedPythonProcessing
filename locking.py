import threading

counter = 0


def increment():
    global counter

    for i in range(10 ** 6):
        counter += 1


threads = []

for i in range(4):
    x = threading.Thread(target=increment)
    threads.append(x)

for t in threads:
    t.start()

for t in threads:
    t.join()

print("Counter Value: ", counter)