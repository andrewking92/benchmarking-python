import time
import logging
from util.Command import Command


class Ping(Command):
    def __init__(self, client):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.client = client

    def execute(self, iterations) -> dict:
        results = {}

        for _i in range(iterations):
            # Build the ping command
            command = {"ping": 1}

            # Execute the ping command
            self.client.admin.command(command)

            for server_description in self.client.topology_description.server_descriptions():
                server_data = self.client.topology_description.server_descriptions()[server_description]

                address = server_data.address[0]
                roundtrip_time = server_data.round_trip_time

                if address not in results:
                    results[address] = {
                        "mean": float(0),
                        "min": float('inf'),
                        "max": float('-inf'),
                        "total": float(0),
                        "count": 0
                    }

                results[address]["total"] += roundtrip_time
                results[address]["count"] += 1
                results[address]["mean"] = results[address]["total"] / results[address]["count"]
                results[address]["min"] = min(results[address]["min"], roundtrip_time)
                results[address]["max"] = max(results[address]["max"], roundtrip_time)

                self.output(**{"address": address, "rtt": roundtrip_time})

            self.logger.info("---")
            time.sleep(0.6)

        for key, value in results.items():
            self.logger.info({key: self.output(**value)})

        return


    def output(self, *args, **kwargs) -> dict:
        formatted = {}

        for key, value in kwargs.items():
            if isinstance(value, float):
                # Convert to ms
                formatted[key] = round(1000 * value, 2)

                if key == "rtt":
                    self.logger.info("{} -> rtt={} ms".format(formatted["address"], formatted[key]))
            else:
                formatted[key] = value

        return formatted
