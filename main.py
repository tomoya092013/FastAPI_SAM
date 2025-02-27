from fastapi import FastAPI
from mangum import Mangum
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "こんにちは, FastAPI on Lambda!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "name": f"Item {item_id}"}

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
def create_item(item: Item):
    return {"message": f"アイテム '{item.name}' を作成しました。価格: {item.price}"}

handler = Mangum(app)
