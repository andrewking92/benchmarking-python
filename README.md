# benchmarking

## Setup
```
sudo pip3 install virtualenv

virtualenv -p /usr/bin/python3.11 benchmarking

source benchmarking/bin/activate

pip install -r requirements.txt

export MONGODB_URI=mongodb://localhost:27017
export DATABASE_NAME=admin
```

## HELP
```
python main.py -h
usage: main.py [-h] [-M [MONGO_URI]] [-D [DATABASE]] {ping} [iterations]

Script to perform benchmarking tasks.

positional arguments:
  {ping}                The action to perform.
  iterations            The number of iterations for the action. Default is 1.

options:
  -h, --help            show this help message and exit
  -M [MONGO_URI], --mongo-uri [MONGO_URI]
                        The MongoDB URI to test against. If not set, will use the 'MONGODB_URI' environment variable.
  -D [DATABASE], --database [DATABASE]
                        The MongoDB Database to test against. If not set, will use the 'DATABASE_NAME' environment variable.
```

## UTIL
```
python main.py ping 500
```