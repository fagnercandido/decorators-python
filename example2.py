import time


def time_execution(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        function(*args, **kwargs)
        end_time = time.time()
        print("[{function}] Time Execution: {total_time}".format(
            function=function.__name__,
            total_time=str(end_time - start_time))
        )

    return wrapper

@time_execution
def main(name):
    print(name)
    for n in range(0, 10000000):
        pass

main('Test')
