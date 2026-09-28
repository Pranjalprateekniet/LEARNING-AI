from typing import TypedDict

class person(TypedDict):
    name:str
    age=int

new_person: Person={'name':'Pranjal', 'age':'22'}

print(new_person)
