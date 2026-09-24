from fastapi import FastAPI, Query, Request, Header, APIRouter
from typing import Optional
app = FastAPI()
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import time
from fastapi.middleware.cors import CORSMiddleware
from fastapi . responses import JSONResponse
from fastapi import Depends
class Item(BaseModel):
    name:str
    price:float
    in_stock:bool = True
    
class ItemCreate(BaseModel):
    name:str
    price:float

class ItemPublic(BaseModel):
    id:int
    name:str
    price:float





app.add_middleware(CORSMiddleware,
allow_origins=["http://127.0.0.1:8000"] ,
allow_credentials=True ,
allow_methods=["*" ] ,
allow_headers=["*" ] ,
)

_items:list[ItemPublic] = []
_next_id: int=1

def pagination(skip:int=0, limit:int=10):
    return {'skip':skip, 'limit':limit}
def _find(item_id:int):
    for item in _items:
        if item.id == item.id:
            return item
    return None

@app.get('/')
def read_root():
    return {'Message:' "Hello World"}

## GET AN ITEM
@app.get("/item/{item_id}")
def read_item(item_id:int):
    return{'item_id':item_id}

## GET ITEMS
@app.get('/items')
def list_items(page:dict=Depends(pagination)):
    print("->getting items")
    skip=page.get('SKip')
    limit=page.get('limit')
    return _items[skip:skip+limit]

@app.get("/services")
def list_services(page:dict=Depends(pagination)):
    return []
## CREATE AN ITEM
@app.post("/items", response_model=ItemPublic, status_code=201)
def create_item(data: ItemCreate):
    global _next_id
    newItem=ItemPublic(id=_next_id, name=data.name, price=data.price)
    _items.append(newItem)
    _next_id+=1
    return newItem

## UPDATE AN ITEM
@app.put("/items", response_model=ItemPublic)
def update_item(item_id:int, data:ItemCreate):
    item=_find(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail='Item not found')
    updated = ItemPublic(id=item_id, name=data.name, price=data.price)
    index=_items.index(item)
    _items[index] = updated
    
    return 'Updated successfully'

## DELETE AN ITEM
@app.delete('/items', status_code=204)
def delete_item(item_id:int):
    item=_find(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail='Item not found')
    _items.remove(item)
    return 'Deleted'

_cart=[]
@app.post('/cart/add')
def add_cart_item(item:str):
    _cart.append(item)
    return _cart

@app.get('/cart')
def get_cart():
    return _cart

@app.middleware('http')
async def m1(request:Request, call_next):
    print('m1 before')
    response = await call_next(request)
    print('m1 after')
    return response

@app.middleware('http')
async def m2(request:Request, call_next):
    print('m2 before')
    response = await call_next(request)
    print('m2 after')
    return response

@app.get("/boom")
def boom():
    return 1/0;

@app.middleware('http')
async def catch_exceptions(request:Request, call_next):
    try:
        return await call_next(request)
    except Exception as exc:
        print(f"Unhandled error with {request.url.path}: {exc}")
        return JSONResponse(status_code=500, content = {'detail': "Internal Sever Error"})

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != 'secret-api-key':
        raise HTTPException(status_code=401, detail='API key error')
    return x_api_key


admin = APIRouter(prefix="/admin", dependencies=[Depends(verify_api_key)])
@admin.get("/secu", dependencies=[Depends(verify_api_key)])
def list_items():
    return _items

from fastapi import Cookie , Response

@app. get ("/visit")
def visit (session_id : str | None = Cookie ( default=None) ) :
    return {"session_id" :session_id }

@app. get ("/login" )
def login (response : Response ) :
    response . set_cookie ( key="session_id", value="abc123" ,
    httponly=True , samesite="lax" )
    return {"status" :"logged in"}
