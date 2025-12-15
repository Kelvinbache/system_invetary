import ast

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

from db.db import conn


class Products(BaseModel):
    name: str
    purchase_cost: float
    shipping_cost: float
    sale: float
    profits: float

class User(BaseModel):
    name_user: str
    password: str


router = APIRouter()


@router.post("/")
async def list_products(request: Request):
    body = await request.body()

    try:
        bodyDecode = ast.literal_eval(body.decode("utf-8"))

        external_data = {
            "name": bodyDecode["name"],
            "purchase_cost": float(bodyDecode["purchase_cost"]),
            "shipping_cost": float(bodyDecode["shipping_cost"]),
            "sale": float(bodyDecode["sale"]),
            "profits": float(bodyDecode["sale"]) - (float(bodyDecode["purchase_cost"]) + float(bodyDecode["shipping_cost"])),
        }

        products = Products(**external_data)

        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO products (name, purchase_cost, shipping_cost, sale, profits ) VALUES (%s, %s, %s, %s, %s)",
                (
                    products.name,
                    products.purchase_cost,
                    products.shipping_cost,
                    products.sale,
                    products.profits,
                ),
            )

            conn.commit()

        return {"reponse": "ok"}

    except Exception as err:
        conn.rollback()
        raise HTTPException(status_code=400, detail=f"error in: {err}")


@router.post("/user")
async def access(user:User):
    if user.name_user == "admin" and user.password == "adminSystem123":
          return RedirectResponse(
            url="/home",
            status_code=303
        )

    else:
        raise HTTPException(status_code=401, detail="Access denied, invalid password or username")