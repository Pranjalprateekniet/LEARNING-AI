from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name:str
    age:Optional[int]=None
    email:EmailStr
    cgpa:float=Field(gt=0,lt=10,default=5,description="A decimal value representing the cgpa of the student")


new_student={'name':'Pranjal','age':22,'email':'abc@gmail.com','cgpa':7.99}

student=Student(**new_student)

student_dict=dict(student)
print(student_dict['age'])
print(student)