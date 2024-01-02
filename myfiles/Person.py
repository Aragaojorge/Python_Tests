from __future__ import annotations
import requests

class Person:
    def __init__(self, name, lastname) -> None:
        self.name = name
        self.lastname = lastname
        self.recovered_data = False
                
    def recovered_all_data(self):
        answer = requests.get('')
        
        if answer.ok:
            self.recovered_data = True
            return 'Connected'
        
        else:
            self.recovered_data = False
            return 'Error 404'