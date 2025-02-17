from pydantic import BaseModel
from typing import Set

class Recipe(BaseModel):
    name: str
    ingredients: Set[str]
    description: str
    calories: int
    num_of_servings: int
