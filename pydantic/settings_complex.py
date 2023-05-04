# https://itnext.io/elegantly-handle-environment-variables-in-python-with-pydantic-452aae26f34
from pydantic import BaseSettings, BaseModel
from typing import List

class NestedEnvs(BaseModel):
    a: str
    b: str

class Envs(BaseSettings):
    my_array: List[str] = ''
    my_object: dict = {}
    nested: NestedEnvs

envs = Envs(_env_file=".env2")

print(envs)