from fastapi import APIRouter, HTTPException

from db.db import conn

router_delete_products = APIRouter()


@router_delete_products.delete("/api/delete_product/{id_product}")
async def controllerDeleteProducts(id_product: int):
    if id_product < 0:
        raise HTTPException(
            status_code=404,
            detail=" The product you are trying to remove does not exist.",
        )

    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM products WHERE id=%s", (id_product,))
            conn.commit()

        return {"response": "The product is successfully removed"}

    except Exception as err:
        conn.rollback()
        raise HTTPException(status_code=404, detail=f" this is error: {err}")
