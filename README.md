# MongoDB Benchmarking Tool

This script is designed to perform benchmarking tasks related to MongoDB. It provides a command-line interface to execute the benchmarking operations and collect round-trip time statistics for MongoDB servers.

## Features

- **Ping Operation**: The script supports a "ping" operation, which sends a ping command to MongoDB servers and measures the round-trip time. You can specify the number of iterations for the ping operation to collect statistics over multiple runs. The script accepts a MongoDB URI as an argument or reads it from the "MONGODB_URI" environment variable.

## Requirements

- Python 3.x
- `pymongo` library


## Installation

1. Clone the repository:
```
git clone https://github.com/andrewking92/benchmarking-python.git
cd benchmarking-python
```

2. Install the dependencies:
```
sudo pip3 install virtualenv

virtualenv -p /usr/bin/python3.11 benchmarking

source benchmarking/bin/activate

pip install -r requirements.txt


Optional

export MONGODB_URI=mongodb://localhost:27017
```

## Usage

To execute the benchmarking script, use the following command:
```
python main.py -h
usage: main.py [-h] [-M [MONGO_URI]] {ping} [iterations]

Script to perform benchmarking tasks.

positional arguments:
  {ping}                The action to perform.
  iterations            The number of iterations for the action. Default is 1.

options:
  -h, --help            show this help message and exit
  -M [MONGO_URI], --mongo-uri [MONGO_URI]
                        The MongoDB URI to test against. If not set, will use the 'MONGODB_URI' environment variable.


python main.py ping 500

```


### Examples

1. Perform a single ping operation against the MongoDB server using the "MONGODB_URI" environment variable:
```
python main.py ping
```
2. Perform 10 ping operations against a specific MongoDB server:
```
python main.py ping 10 --mongo-uri "mongodb+srv://<username>:<password>@atlas-cluster.mongodb.net/"
```


## Output

The script logs the round-trip time statistics for each MongoDB server in the following format:

```
<server_address> -> rtt=<round_trip_time> ms
```

## License

This project is licensed under the [MIT License](LICENSE).

## Contribution

Contributions to this project are welcome. Feel free to open issues or submit pull requests.

## Disclaimer

This script is provided as-is without any warranties. Use it at your own risk.