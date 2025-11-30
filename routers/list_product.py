# internal libraries
import os

# External libraries
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from starlette.background import BackgroundTask
from starlette.responses import HTMLResponse

# own methods
from db.db import conn
from output.generate_document import generate_document

router_list_products = APIRouter()

template = Jinja2Templates(directory="templates")


@router_list_products.get("/")
def list_products():
    response = None

    try:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT name,purchase_cost,shipping_cost,sale, profits FROM products"
            )

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
    return template.TemplateResponse(request=request, name="index.html", context={})


@router_list_products.get("/donwloand")
async def donwload_list_product():
    try:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT name,purchase_cost,shipping_cost,sale, profits FROM products"
            )

            response = cur.fetchall()
            generate_document(response)

            file_path = os.path.join(os.getcwd(), "files", "user_file.xlsx")
            remove_file = BackgroundTask(os.remove, file_path)

            if os.path.exists(file_path):
                return FileResponse(
                    path=file_path,
                    filename="user_file.xlsx",
                    media_type="application/octet-stream",
                    background=remove_file,
                )

        if response is None:
            raise HTTPException(status_code=404, detail="data not found")

        else:
            raise HTTPException(status_code=404, detail=" file not found")

    except Exception as err:
        raise HTTPException(status_code=500, detail=f"error ${err}")
