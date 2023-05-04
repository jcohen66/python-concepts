from pydantic import BaseSettings

class Envs(BaseSettings):
    name: str
    age: int

    
envs = Envs(_env_file=".env")

print(envs)