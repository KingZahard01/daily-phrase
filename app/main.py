from fastapi import FastAPI

from app.database import TOTAL_VERSES  # , VERSES
from app.routes import stats, verses

app = FastAPI(
    title="Frase Bíblica Diaria API",
    version="1.0.0",
    description="API de versículos bíblicos Reina Valera 1909",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Incluir routers
app.include_router(verses.router)
app.include_router(stats.router)


@app.get("/", tags=["Raíz"])
def root():
    """
    Página principal con información de la API.
    """
    return {
        "message": "Bienvenido a Frase Bíblica Diaria API",
        "description": "API completa de la Biblia Reina Valera 1909",
        "total_verses": TOTAL_VERSES,
        "endpoints": {
            "documentación": "/docs",
            "versículo_diario": "/api/daily-verse",
            "versículo_aleatorio": "/api/random-verse",
            "búsqueda": "/api/verses?book=Genesis",
            "versículo_específico": "/api/verse/Genesis/1/1",
            "estadísticas": "/api/stats",
        },
    }


@app.on_event("startup")
def startup_event():
    """
    Evento al iniciar la aplicación.
    """
    print(f"✅ API iniciada con {TOTAL_VERSES:,} versículos cargados")
    if TOTAL_VERSES == 0:
        print("⚠️  Advertencia: No se cargaron versículos")
