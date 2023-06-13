import time
import logging

class Ping:
    def __init__(self, database, iterations):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.database = database
        self.iterations = iterations

    def ping(self):
        total_duration = 0.0
        min_response_time = float('inf')
        max_response_time = float('-inf')

        for i in range(self.iterations):
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

        average_response_time = total_duration / self.iterations

        # Create and print the table
        timings = {
            "total": round(total_duration, 2),
            "mean": round(average_response_time, 2),
            "min": round(min_response_time, 2),
            "max": round(max_response_time, 2)
        }

        self.logger.info(timings)

        return timings