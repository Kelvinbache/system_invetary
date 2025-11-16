from fastapi import APIRouter

router = APIRouter()


@router.post("/")
def list_products():
    return {"list": "product"}
