# benchmarking

## Setup
```
export MONGODB_URI=mongodb://localhost:27017
export DATABASE_NAME=admin
```

## HELP
```
python main.py -h
usage: main.py [-h] {ping} [iterations]

Script to perform benchmarking tasks.

positional arguments:
  {ping}      The action to perform.
  iterations  The number of iterations for the action. Default is 1.

options:
  -h, --help  show this help message and exit
```

## UTIL
```
python main.py ping 500
```