import ast

from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel

from db.db import conn


class Products(BaseModel):
    name: str
    purchase_cost: float
    shipping_cost: float
    sale: float
    profits: float


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
            "profits": (
                float(bodyDecode["purchase_cost"]) + float(bodyDecode["shipping_cost"])
            )
            - float(bodyDecode["sale"]),
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
