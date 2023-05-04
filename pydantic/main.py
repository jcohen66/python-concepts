import string
import pydantic
import json
from typing import Optional

class User(pydantic.BaseModel):
    username: str
    password: str
    age: int
    score: float
    email: Optional[str]
    phone_number: Optional[str]
    
    @pydantic.root_validator(pre=True)
    @classmethod
    def validate_phone_or_mail(cls, values):
        if "email" in values or "phone_number" in values:
            return values
        else:
            raise ValueError("Need either phone_number or email")
    
    @pydantic.validator("username")
    @classmethod
    def username_valid(cls, value):
        if any(p in value for p in string.punctuation):
            raise ValueError("Username must not contain punctuation")
        else:
            return value
        
    @pydantic.validator("password")
    @classmethod
    def password_valid(cls, value):
        if len(value) < 8:
            raise ValueErrr("Password must be at least 8 characters.")
        if any(p in value for p in string.punctuation):
            if any(d in value for d in string.digits):
                if any(l in value for l in string.ascii_lowercase):
                    if any(u in value for u in string.ascii_uppercase):
                        return value
        
        raise ValueError("Password must have punctuation character, digit, upper and lowercase characters.")
    
    @pydantic.validator("age", "score")
    @classmethod
    def number_valid(cls, value):
        if value >= 0:
            return value
        else:
            raise ValueError("Age and Score must be positive.")   


if __name__ == '__main__':
    user1 = User(username="user1", password='Blort_01', age=42, score=99.0, phone_number="+19145551212")

    print(user1)
    
    # For each dictionary in json file, unpack (**u) the object.
    json_users =  [User(**u) for u in json.load(open("users.json"))]
    print(json_users)