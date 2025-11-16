import uvicorn
from fastapi import FastAPI

from routers.add_product import router

app = FastAPI()

app.include_router(router)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, log_level="info", reload=True)
