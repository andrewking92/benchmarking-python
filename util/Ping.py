import time
import logging
from util.command import Command


class Ping(Command):
    def __init__(self, client, *, cli_flag=False):
        self.logger = logging.getLogger("benchmarking.ping")
        self.client = client
        self.cli_flag = cli_flag
        super().__init__()

    def execute(self, iterations) -> dict:
        results = {}

        for _i in range(iterations):
            # Build the ping command
            command = {"ping": 1}

            # Execute the ping command
            self.client.admin.command(command)

            for server_description in self.client.topology_description.server_descriptions():
                server_data = self.client.topology_description.server_descriptions()[server_description]

                if server_data.address not in results:
                    results[server_data.address] = {
                        "mean": float(0),
                        "min": float("inf"),
                        "max": float("-inf"),
                        "total": float(0),
                        "count": 0,
                    }

                results[server_data.address]["total"] += server_data.round_trip_time
                results[server_data.address]["count"] += 1
                results[server_data.address]["mean"] = (
                    results[server_data.address]["total"] / results[server_data.address]["count"]
                )
                results[server_data.address]["min"] = min(
                    results[server_data.address]["min"], server_data.round_trip_time
                )
                results[server_data.address]["max"] = max(
                    results[server_data.address]["max"], server_data.round_trip_time
                )

                self.output(**{"address": server_data.address, "rtt": server_data.round_trip_time})

            self.logger.info("---")
            time.sleep(0.6)

        for key, value in results.items():
            results[key] = self.output(**value)
            self.logger.info({key: results[key]})

        return results

    def output(self, *args, **kwargs) -> dict:
        formatted = {}

        for key, value in kwargs.items():
            if isinstance(value, float):
                formatted[key] = round(1000 * value, 2)  # Convert to ms
                if key == "rtt":
                    msg = "{} -> rtt={} ms".format(formatted["address"], formatted[key])
                    if self.cli_flag:
                        self.logger.info(msg)
                    else:
                        print(msg)
            else:
                formatted[key] = value
        
        if args and "---" in args:
            if self.cli_flag:
                self.logger.info("---")
            else:
                print("---")

        return formatted
