from typing import Callable, Iterable


def group_by(function: Callable, iterable: Iterable) -> dict:
    """
    :param function: Function run on all values in iterable.
    :param iterable: Arguments for function.
    :return: A dictionary with function(value) as a key and all values (with this key)
    as a list.
    """
    ret = {}
    for value in iterable:
        ret.setdefault(function(value), []).append(value)
    return ret


if __name__ == '__main__':
    print(group_by(len, ["hi", "bye", "yo", "try"]))
