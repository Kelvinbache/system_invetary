from fastapi import APIRouter, HTTPException, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse

from db.db import conn

router_list_products = APIRouter()

template = Jinja2Templates(directory="templates")


@router_list_products.get("/")
def list_products():
    response = None

    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM products")
            response = cur.fetchall()

        if response is None:
            raise HTTPException(status_code=404, detail="data not found")

        else:
            return {"response": response}

    except Exception as err:
        raise HTTPException(status_code=404, detail=f" this is error: {err}")


@router_list_products.get("/home", response_class=HTMLResponse)
def controllerHome(request: Request):
    return template.TemplateResponse(request=request, name="index.html", context={})


@router_list_products.get("/add_product", response_class=HTMLResponse)
def controllerAddProducto(request: Request):
    print(request.url)
    return template.TemplateResponse(request=request, name="index.html", context={})
