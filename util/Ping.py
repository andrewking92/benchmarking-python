import time


class Ping:
    def __init__(self, database, iterations):
        self.database = database
        self.iterations = iterations

    def ping(self):
        total_duration = 0

        for i in range(self.iterations):
            start_time = int(round(time.time() * 1000))

            # Build the ping command
            command = {"ping": 1}

            # Execute the ping command
            self.database.command(command)

            end_time = int(round(time.time() * 1000))
            duration = end_time - start_time
            total_duration += duration

        average_response_time = total_duration / self.iterations

        print("Pinged deployment", self.iterations, "times.")
        print("Execution time:", total_duration, "milliseconds.")
        print(
            "Average response time per ping command:",
            average_response_time,
            "milliseconds",
        )
