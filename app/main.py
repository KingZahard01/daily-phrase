import json
import random
from datetime import date

from fastapi import FastAPI

app = FastAPI(title="Frase Diaria", version="1.0.0")

# cargar la base de datos
with open("app/database.json", "r", encoding="utf-8") as f:
    PHRASES = json.load(f)


@app.get("/")
def home():
    """
    Obtiene la página de inicio.
    """
    return {"message": "Welcome to Frase Diaria"}


@app.get("/daily-phrase")
def daily_phrase():
    """
    Obtiene una frase del día.
    """
    if not PHRASES:  # Manejo de errores
        return {"error": "No phrases available"}

    index = date.today().toordinal() % len(PHRASES)
    phrase = PHRASES[index]
    return {
        "date": str(date.today()),
        "text": phrase["texto"],
        "author": phrase["autor"],
    }


@app.get("/phrase-random")
def frase_random():
    """
    Obtiene una frase aleatoria.
    """
    phrase = random.choice(PHRASES)
    return {
        "text": phrase["texto"],
        "author": phrase["autor"],
    }


@app.get("/phrases")
def all_phrases():
    """
    Obtiene todas las frases.
    """
    return {
        "total": len(PHRASES),
        "phrases": [
            {"text": phrase["texto"], "author": phrase["autor"]}
            for phrase in PHRASES  # para cada frase en la lista de frases
        ],
    }
