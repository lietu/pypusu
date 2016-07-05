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

## Dependencies

Not quite sure how to deal with dependencies yet, so for now you'll have to 
install them separately.

For the threaded client you'll need the following in your `requirements.txt`:

```
ws4py==0.3.5
wsaccel==0.6.2
```

Or you can try:

```
pip install ws4py wsaccel
```


## License

Short version: MIT + New BSD.

Long version: Read the LICENSE.md -file.


## Uploading to PyPi

You can't really do that without the appropriate username + password information,
but I'm saving this here because I'll just forget.

```
python setup.py sdist upload -r pypitest
python setup.py sdist upload -r pypi
```