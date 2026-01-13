from fastapi import FastAPI
from typing import Any
from scalar_fastapi import get_scalar_api_reference
web=FastAPI()

@web.get("/model/{id}")
def get_details(id:int)-> Any:
    return {
        "model_id": id,
        "details": "Placeholder for model details."
    }

@web.get("/scalar",include_in_schema=False)
def get_scalar_reference()-> Any:
    return get_scalar_api_reference(
        openapi_url=web.openapi_url,
        title="Scalar API Reference",
    )
