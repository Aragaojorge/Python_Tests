def sum(x, y):
    """
    >>> sum(10, 20)
    31
    
    >>> sum(-10, 20)
    10
    
    >>> sum('40', 10)
    Traceback (most recent call last):
    ...
    AssertionError: x should be int or float!
    """

    assert isinstance(x, (int, float)), 'x should be int or float!'
    assert isinstance(x, (int, float)), 'y should be int or float!'
    return x + y



if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    
    