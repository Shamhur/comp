import time

def timer(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Функція виконувалася {end_time - start_time:.6f} секунд")
        return result, elapsed_time
    return wrapper

@timer
def sample_function(x):
    return x ** 2

@timer
def sleep_function(seconds):
    time.sleep(seconds)
    return f"Спали {seconds} секунд"

