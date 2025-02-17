from fastapi import FastAPI
from db.models import Recipe
from db.database import recipes_collection
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.requests import Request


app = FastAPI()
templates = Jinja2Templates(directory="frontend")

recipes = []
@app.get('/')
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production (e.g., ["http://localhost:5173"])
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

@app.post('/create_recipe')
async def create_recipe(recipe: Recipe):
    # Add recipe to mongo DB
    recipe_dict = recipe.model_dump()
    recipe_dict["ingredients"] = list(recipe_dict["ingredients"])
    result = await recipes_collection.insert_one(recipe_dict)

    recipes.append(recipe)
    print("Recipe added:", recipe_dict)
    return {"message": "Recipe added successfully!", "recipe": recipe}

@app.get('/recipes')
async def get_all_recipes():
    # fetch all recipes from mongo DB
    recipes_cursor = recipes_collection.find({})
    recipes = await recipes_cursor.to_list(100)
    for recipe in recipes:
        recipe["_id"] = str(recipe["_id"])  # Convert MongoDB ObjectId to string
        recipe["ingredients"] = list(recipe["ingredients"])
    return {"recipes": recipes}

