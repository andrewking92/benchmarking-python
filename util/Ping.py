import sys
import time


class Ping:
    def __init__(self, database):
        self.database = database


    def ping(self):
        TOTAL_ITER = int(sys.argv[1])

        total_duration = 0

        for i in range(TOTAL_ITER):
            start_time = int(round(time.time() * 1000))

            # Build the ping command
            command = {"ping": 1}

            # Execute the ping command
            self.database.command(command)

            end_time = int(round(time.time() * 1000))
            duration = end_time - start_time
            total_duration += duration

        average_response_time = total_duration / TOTAL_ITER

        print("Pinged deployment", TOTAL_ITER, "times.")
        print("Execution time:", total_duration, "milliseconds.")
        print("Average response time per ping command:", average_response_time, "milliseconds")