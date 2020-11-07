import time


def time_execution(function):
    def wrapper():
        start_time = time.time()
        function()
        end_time = time.time()
        print("[{function}] Time Execution: {total_time}".format(
            function=function.__name__,
            total_time=str(end_time - start_time))
        )

    return wrapper

@time_execution
def main():
    for n in range(0, 10000000):
        pass

main()
