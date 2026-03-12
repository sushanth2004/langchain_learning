from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class Student(BaseModel):
    name : str = 'Sushanth Neelam'
    age : Optional[int] = None
    email : EmailStr
    cgpa : float = Field(ge=0 , le= 10, default=0, description="A decimal value representing cgpa of student.")

new_student = {'name': 'manohar', 'age':'45', 'email': 'abc@gmail.com', 'cgpa' : 0} 

student = Student(**new_student)

print(student)

student_dict = student.model_dump()
student_json = student.model_dump_json()

print(student_dict['age'])
print(student_json)
