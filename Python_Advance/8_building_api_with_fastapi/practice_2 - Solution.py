#import FastAPI
from fastapi import FastAPI

#create an instance
app = FastAPI()

#create a dictionary for coupon code
coupon_code = {
    1: "10%",
    2: "20%",
    3: "30%"
}


#write a get code to return coupon code
#it will return as like
""" Disount amount is 20% """

@app.get("/get_coupon/{code}")
def get_items(code: int):
    return f"Discount amount is {coupon_code.get(code,'Code not found')}"



""" in the terminal write fastapi dev .\practice_2.py"""

