from fastapi import FastAPI
from pydantic import BaseModel

#  Validation of user input
class UserRegistrationInputFields(BaseModel):
    first_name : str
    last_name : str
    mobile : int
    email : str


# create an obj of FastAPI Class
app = FastAPI()


@app.post("/user_registration_form")
def user_reg_function(data : UserRegistrationInputFields):
    print(data.first_name)
    print(data.last_name)
    print(data.mobile)
    print(data.email)






