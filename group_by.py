from typing import Callable, Iterable


def group_by(function: Callable, iterable: Iterable) -> dict:
    """
    Go over all values in iterable and run the function on them.
    Return a dictionary with return values from function as a key
    and value corresponding to a particular key from the iterable.
    :param function: Function run on all values in iterable.
    :param iterable: Arguments for function.
    :return: A dictionary with function(value) as a key and all values (with this key)
    as a list.
    """
    return_dict = {}
    for value in iterable:
        return_dict.setdefault(function(value), []).append(value)
    return return_dict


if __name__ == '__main__':
    print(group_by(len, ["hi", "bye", "yo", "try"]))
