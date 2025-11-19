from fastapi import APIRouter, HTTPException

from db.db import conn

router = APIRouter()


@router.get("/")
def list_products():
    response = None

    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM products")
            response = cur.fetchall()

        return {"response": response}

    except Exception as err:
        raise HTTPException(status_code=404, detail=f" this is error: {err}")
