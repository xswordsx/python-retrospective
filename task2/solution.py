from collections import defaultdict


def groupby(func, seq):
    default_dict = defaultdict(list)
    for iterable in seq:
        default_dict[func(iterable)].append(iterable)
    return dict(default_dict)


def zip_with(func, *iterables):
    for iters in list(zip(*iterables)):
        yield func(*iters)


def compose(func1, func2):
    return lambda x: func1(func2(x))


def iterate(function):
    result = lambda x: x
    while True:
        result
        result = compose(function, result)
