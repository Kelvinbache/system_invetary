from fastapi import APIRouter, HTTPException
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
def list_products(products: Products):
    try:
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

        return {"reponse": "ok"}

    except Exception as err:
        raise HTTPException(status_code=400, detail=f"error in: {err}")
