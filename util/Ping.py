import time
import logging
from util.Command import Command


class Ping(Command):
    def __init__(self, database):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.database = database


    def execute(self, iterations) -> dict:
        total_duration = 0.0
        min_response_time = float('inf')
        max_response_time = float('-inf')

        for i in range(iterations):
            start_time = float(time.time() * 1000)

            # Build the ping command
            command = {"ping": 1}

            # Execute the ping command
            self.database.command(command)

            end_time = float(time.time() * 1000)
            duration = end_time - start_time

            min_response_time = min(min_response_time, duration)
            max_response_time = max(max_response_time, duration)

            total_duration += duration
        
        average_response_time = total_duration / iterations

        return self.output(iterations, total_duration, average_response_time, min_response_time, max_response_time)


    def output(self, *args) -> dict:

        # Create and print the table
        timings = {
            "count": args[0],
            "total": round(args[1], 2),
            "mean": round(args[2], 2),
            "min": round(args[3], 2),
            "max": round(args[4], 2)
        }

        self.logger.info(timings)

        return timings