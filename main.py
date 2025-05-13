from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from routes import cheese


app = FastAPI()

app.include_router(cheese.router, tags=["Cheese types"])


@app.get("/", include_in_schema=False)
async def redirect_root():
    return RedirectResponse("/docs")
