# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item (BaseModel):
    text:str = None
    is_done:bool = False

items = []

@app.get("/")
def read_root():
    return {"mensaje": "¡Hola, FastAPI!"}

@app.post("/items")
def createItems (item:Item):
    items.append(item)
    return item

@app.get("/items/{itemId}", response_model=Item)
def getItem (itemId:int) -> Item:
    item = items[itemId]
    if itemId < len(items):
        return items(itemId)
    else:
        raise HTTPException (status_code=404, detail=f"item {itemId} not found")
    
@app.get("/items", response_model=list[Item])
def ListItems (limit:int = 10):
    return items[0:limit]