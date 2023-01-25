from django.db import connection, reset_queries
import time
import functools


def query_debugger(func):
    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        reset_queries()

        start_queries = len(connection.queries)

        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        end_queries = len(connection.queries)

        print(*connection.queries, sep='\n')
        print(f"Function : {func.__name__}")
        print(f"Number of Queries : {end_queries - start_queries}")
        print(f"Finished in : {(end - start):.2f}s")
        return result

    return inner_func


class DebugQueryMixin:
    """ Debugs only .get method """
    def __init__(self, *args, **kwargs):
        for method_name in ('get',):
            method = query_debugger(getattr(self, method_name))
            setattr(self, method_name, method)
        super().__init__(*args, **kwargs)
