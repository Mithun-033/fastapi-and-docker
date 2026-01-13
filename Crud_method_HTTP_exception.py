from fastapi import FastAPI,HTTPException,status
from typing import Any
from scalar_fastapi import get_scalar_api_reference

from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str

web=FastAPI()

data={
    1:{"name":"Item One","description":"This is the first item."},
    2:{"name":"Item Two","description":"This is the second item."},
    3:{"name":"Item Three","description":"This is the third item."},
    4:{"name":"Item Four","description":"This is the fourth item."}
}

@web.get("/items/")
def get_items(id:int)->dict[int,str]:
    if id not in data.keys():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="ID not in databse")
    return data[id]

@web.post("/items/")
def put_item(name:str,description:str)-> dict[int,str]:
    new_id=max(data.keys)+1
    data[new_id]={
        "name":name,
        "descritpion":description}
    return data[new_id]

@web.put("/items/")
def update_item(id:int,name:str,description:str)-> dict[int,Any]:
    if id not in data.keys():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="ID not in databse")
    data[id]={
        "name":name,
        "descritpion":description}
    return data[id]

@web.patch("/items/")
def patch_items(data:Item,id:int)-> dict[int,str]:
    if id not in data.keys():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="ID not in databse")
    if data.name:
        data[id]["name"]=data.name
    if data.description:
        data[id]["description"]=data.description
    return data[id]

@web.delete("/items/")
def delete_item(id:int)-> dict[int,str]:
    if id not in data.keys():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="ID not in databse")
    deleted_item=data.pop(id)
    return deleted_item

@web.get("/scalar",include_in_schema=False)
def get_scalar_reference()-> Any:
    return get_scalar_api_reference(
        openapi_url=web.openapi_url,
        title="Scalar API Reference",
    )
#awrbg