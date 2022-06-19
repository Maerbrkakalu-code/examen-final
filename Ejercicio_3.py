import time

def mesureTime(function):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = function(*args, **kwargs)

        total = time.time() - start
        print("La demora de ejecución fue de: {}".format(total))

        return result

    return wrapper


@mesureTime
def multipliacion(a, b):
    time.sleep(1)
    s = a * b
    return s

print(multipliacion(20, 40))