import json
import random
from datetime import date

from fastapi import FastAPI

app = FastAPI(title="Frase Bíblica Diaria", version="1.0.0")

PHRASES = []

# Nota: usamos utf-8-sig para manejar el BOM
with open("app/es_rvr.json", "r", encoding="utf-8-sig") as f:
    books = json.load(f)

for book in books:
    book_name = book["name"]
    for chapter_index, chapter in enumerate(book["chapters"], start=1):
        for verse_index, verse_text in enumerate(chapter, start=1):
            PHRASES.append(
                {
                    "texto": verse_text,
                    "autor": book_name,
                    "reference": f"{book_name} {chapter_index}:{verse_index}",
                    "version": "Reina Valera 1909",
                }
            )


@app.get("/")
def home():
    return {"message": "Welcome to Frase Bíblica Diaria"}


@app.get("/daily-phrase")
def daily_phrase():
    if not PHRASES:
        return {"error": "No verses available"}

    index = date.today().toordinal() % len(PHRASES)
    phrase = PHRASES[index]
    return {
        "date": str(date.today()),
        "text": phrase["texto"],
        "author": phrase["autor"],
        "reference": phrase["reference"],
        "version": phrase["version"],
    }


@app.get("/phrase-random")
def phrase_random():
    phrase = random.choice(PHRASES)
    return {
        "text": phrase["texto"],
        "author": phrase["autor"],
        "reference": phrase["reference"],
        "version": phrase["version"],
    }


@app.get("/phrases")
def all_phrases():
    return {
        "total": len(PHRASES),
        "phrases": [
            {
                "text": p["texto"],
                "author": p["autor"],
                "reference": p["reference"],
                "version": p["version"],
            }
            for p in PHRASES
        ],
    }
