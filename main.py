import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# routers
from routers.add_product import router
from routers.list_product import router_list_products

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(router)
app.include_router(router_list_products)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, log_level="info", reload=True)
