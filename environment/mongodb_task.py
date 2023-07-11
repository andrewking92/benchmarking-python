import time
from functools import wraps
from locust import task

def mongodb_task(weight=1):
    """
    A decorator to run a MongoDB operation as a Locust task
    :param weight: the task weight
    """
    def decorator(func):
        @wraps(func)
        @task(weight=weight)
        def wrapper(self, *args, **kwargs):
            name = func.__name__  # Get the name of the decorated function

            try:
                start_time = time.time()
                func(self, *args, **kwargs)  # Execute the decorated function
                end_time = time.time()
                total_sec = end_time - start_time
                total_time = round(float((end_time - start_time) * 1000), 2)

                self.environment.events.request.fire(
                        request_type='mongodb', name=name, response_time=total_time, total_sec = total_sec, response_length=1
                )

            except Exception as e:
                print(e)

        return wrapper

    return decorator
