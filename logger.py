import sys
import functools
import logging
from typing import Callable, Any, Optional


def logger(func=None, *, handle=sys.stdout):
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            is_logger = isinstance(handle, logging.Logger)

            # Собираем строку с аргументами
            args_list = [repr(arg) for arg in args]
            kwargs_list = [f"{key}={repr(val)}" for key, val in kwargs.items()]
            params_str = ", ".join(args_list + kwargs_list)

            # Лог старта
            if is_logger:
                handle.info(f"START {func.__name__}: args=({params_str})")
            else:
                handle.write(f"INFO: START {func.__name__} | args=({params_str})\n")

            try:
                result = func(*args, **kwargs)

                # Лог успеха
                if is_logger:
                    handle.info(f"SUCCESS {func.__name__}: result={repr(result)}")
                else:
                    handle.write(f"INFO: SUCCESS {func.__name__} | result={repr(result)}\n")

                return result

            except Exception as exc:
                # Лог ошибки
                err_msg = f"{type(exc).__name__}: {exc}"
                if is_logger:
                    handle.error(f"ERROR {func.__name__}: {err_msg}")
                else:
                    handle.write(f"ERROR: {func.__name__} | {err_msg}\n")
                raise

        return wrapper

    if func is None:
        return decorator
    return decorator(func)