# FastAPI entry point
from fastapi import FastAPI
from app.api.routes import router as api_router
from app.api.evento import router as evento_router


app = FastAPI()

# Ruta básica de prueba
@app.get("/")
def root():
    return {"message": "Hello, world!"}

# Incluir las rutas del webhook (y otras futuras)
app.include_router(api_router)
app.include_router(evento_router)
