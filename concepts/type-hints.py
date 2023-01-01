from typing import List
from typing import Final
from typing import Union
from typing import Iterable
from typing import Optional
from typing import Any
from typing import TypeAlias
from typing import Literal

def my_func(nums: Iterable):
    for n in nums:
        print(n)


# Can att ':type' but its just a hint not mandatory rule:
name: str = "Yang"
age: int = 29
assets: list = []
posts: tuple = ()
hobbies: dict = {}
notes: list[str] = ['Python Type Hints', 'Python Tricks']
msgs: dict[int, str] = {1: 'Python Type Hints', 2: 'Python Tricks'}

age = "29th"

DATABASE: Final = "MySQL"
data: Union[int, float] = 3.14

data: int|float = 3.14

my_func(notes)

# This is equivalent to Union[X, None]
a: Optional[int] = 123

def my_funcAny(nums: Any):
    pass

def greeting(name: str):
    return "Hello " + name

# Create an alias for the type
PostsType: TypeAlias = dict[int, str]

# Then reuse the alias
new_posts: PostsType = {1: "Python Type Hints", 2: "Python Tricks"}
old_posts: PostsType =  {}


# Enums/Literals
weekends: Literal['Saterday', 'Sunday']

weekends = 'Saturday'
weekends = 'Monday'
