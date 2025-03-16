# Настройка логирования
from functools import wraps

def log(function=None):
    """
    Декоратор для логирования выполнения функций.
    """

    def her(fun):
        @wraps(fun)
        def ytr(*args, **kwargs):
            try:
                result = fun(*args, **kwargs)
                if function:
                    with open(function, "a") as file:
                        file.write(f"\n{fun.__name__} ok")
                else:
                    print(f"{fun.__name__} ok")
                return result
            except Exception as r:
                if function:
                    with open(function, "a") as file:
                        file.write(f"\n{fun.__name__} error: {type(r)}. Inputs:{args}")
                else:
                    print(f"{fun.__name__} error: {r}. Inputs:{args}")
                raise r

        return ytr

    return her
