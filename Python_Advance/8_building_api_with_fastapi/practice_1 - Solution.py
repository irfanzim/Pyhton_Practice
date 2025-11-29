#import FastAPI
from fastapi import FastAPI

#create an instance
app = FastAPI()

#create a dictionary
food_items = {
    "indian": ["samusa", "vadapav"],
    "bengali": ["singara", "fuchka"],
    "japanese": ["sushi", "teriyaki"]
}


#write a get code to return a specific cuisine
@app.get("/get_items/{cuisine}")
def get_items(cuisine):
    return food_items.get(cuisine,"Cuisine not found")


""" in the terminal write fastapi dev .\practice_1.py"""

