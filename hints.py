# Read documentation: https://docs.python.org/3/library/typing.html
from typing import List, Union, Tuple, Dict, Callable, Sequence, Iterable

# Primitive type
number: int = 1
floating: float = 10.5
boolean0: bool = False
string: str = 'Jorge'

# Sequences
lista: List[int] = [1, 2, 3]
lista_str_int: List[Union[int, str]] = [1, 2, 3, 'Jorge']
tupla: Tuple[int, int, int] = (1, 2, 3)

# Dict and Set
person: Dict[str, Union[str, int]] = {'Name': 'Jorge', 'Lastname': 'Aragão', 'Age': 39}

# My type(dict)
MyDict = Dict[str, Union[str, int, List[int]]] # Alias
person2: MyDict = {'Name': 'Jorge', 'Lastname': 'Aragão', 'Age': 39, 'L': [1, 2]}

# Function
def return_function(funcao: Callable[[int, int], int]) -> Callable:
    return funcao

def sum(x:int, y: int) -> int:
    return x + y

print(return_function(sum)(10, 20))

# Class

class Person:
    def __init__(self, name: str, lastname: str, age: int) -> None:
        self.name: str = name
        self.lastname: str = lastname
        self.age: int = age
    
    def speaking(self) -> None:
        print(f'{self.name} {self.lastname} is speaking his age is {self.age}!')
        
person = Person('Jorge', 'Aragão', 39)
person.speaking()
print(person)

# Iterable
def iterar(sequencia: Sequence[int]):
    return [x * 2 for x in sequencia]

def iterar2(sequencia: Iterable[int]):
    return [x for x in sequencia]

print(iterar([1, 2, 3]))
print(iterar2([1, 2, 3]))