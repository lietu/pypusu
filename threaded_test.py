from pypusu.threaded import PuSuClient
from time import sleep, time

if __name__ == "__main__":
    print("Connecting")
    c = PuSuClient("ws://127.0.0.1:55000")

    count = 0


    def listener(msg):
        global count
        count += 1


    print("Authorizing")
    c.authorize("foo")
    print("Subscribing")
    c.subscribe("channel.1", listener)

    print("Waiting")

    target = 500
    start = time()
    for i in range(1, target + 1):
        c.publish("channel.1", {"foo": "bar"})
    end = time()
    elapsed = end - start

    print("Sent {} messages in {:.3f}s, {:.2f}msg/s".format(
        target,
        elapsed,
        target / elapsed
    ))

    sleep(60)

    print("Got {} messages".format(count))
