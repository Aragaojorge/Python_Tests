"""
1 - receive an int
2 - if n is multiple of 3 and 5: bacon with eggs
3 - if n is not a multiple of 3 and 5: starve
4 - if n is only a 3 multiple 3: bacon
5 - if n is only a 5 multiple: eggs
"""

def bacon_with_eggs(n):
    assert isinstance(n, int), 'n should be int'
    
    if n % 3 == 0 and n % 5 == 0:
        return 'Bacon with eggs'
    
    if n % 3 == 0:
        return 'Bacon'
    
    if n % 5 == 0:
        return 'Eggs'
    
    return 'Starve'