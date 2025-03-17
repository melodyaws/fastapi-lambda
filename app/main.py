from fastapi import FastAPI, HTTPException
from mangum import Mangum
from pydantic import BaseModel
from typing import Optional, List
import os

# 初始化 FastAPI 應用
app = FastAPI(
    title="FastAPI Lambda Demo",
    description="使用 FastAPI 和 AWS Lambda 構建的 API 示例",
    version="0.1.0",
)

# 數據模型
class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float
    is_offer: Optional[bool] = None

# 內存數據存儲（示例用途）
items_db = {}
next_id = 1

# 路由定義
@app.get("/")
def read_root():
    return {"Hello": "World", "Message": "Welcome to FastAPI on Lambda!"}

@app.get("/items", response_model=List[Item])
def read_items():
    return list(items_db.values())

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]

@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    global next_id
    item_id = next_id
    next_id += 1
    item.id = item_id
    items_db[item_id] = item
    return item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    item.id = item_id
    items_db[item_id] = item
    return item

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
    return {"message": "Item deleted successfully"}

# The adaptor which will transfer the request AWS Lambda to FastAPI
handler = Mangum(app)

# run "uvicorn main:app --reloadt" rapid development and API testing
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)