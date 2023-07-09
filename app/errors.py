def errors_handler(func):
    def wrapper(*args, **kwargs):
        try:
            func_result = func(*args, **kwargs)
        except Exception:
            print("Произошла непредвиденная ошибка. Перезапустите программу.")
            exit(1)
        return func_result
    return wrapper
