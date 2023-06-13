import time
from tabulate import tabulate


class Ping:
    def __init__(self, database, iterations):
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
        table = [
            ["Metric", "Time (ms)"],
            ["Total Execution", round(total_duration, 2)],
            ["Mean", round(average_response_time, 2)],
            ["Min", round(min_response_time, 2)],
            ["Max", round(max_response_time, 2)]
        ]
        # print(tabulate(table, headers="firstrow", tablefmt="grid"))
        print(tabulate(table, headers="firstrow", tablefmt="grid", numalign="center"))
