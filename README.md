# PuSu Engine client for Python

## Simple example

```
from pypusu.threaded import PuSuClient

if __name__ == "__main__":
    c = PuSuClient("ws://127.0.0.1:55000")

    count = 0


    def listener(msg):
        global count
        count += 1


    c.authorize("foo")
    c.subscribe("channel.1", listener)
    c.publish("channel.1", {"foo": "bar"})

    from time import sleep

    sleep(30)

    print(count)
```


## License

Short version: MIT + New BSD.

Long version: Read the LICENSE.md -file.
