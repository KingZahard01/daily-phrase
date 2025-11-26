# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

**Frase Diaria** is a FastAPI application that serves daily inspirational Christian phrases via REST API. The application delivers biblical verses and quotes from Christian theologians/leaders in Spanish.

## Architecture

### Core Components

- **`app/main.py`**: Single FastAPI application entry point containing all endpoint logic
- **`app/database.json`**: Static phrase database with biblical verses and Christian quotes
- **Virtual environment**: Located in `venv/` directory

### Data Model

The database contains phrase objects with:
- `id`: Unique identifier
- `texto`: Quote text (Spanish)
- `autor`: Attribution (biblical reference or author name)

### API Design

The application uses a deterministic daily phrase algorithm: `date.today().toordinal() % len(PHRASES)` to ensure the same phrase is returned for a given date across all requests.

## Common Commands

### Running the Application

```bash
# Activate virtual environment
source venv/bin/activate

# Run development server
uvicorn app.main:app --reload

# Run on specific host/port
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### Testing Endpoints

```bash
# Test home endpoint
curl http://localhost:8000/

# Test daily phrase (deterministic based on date)
curl http://localhost:8000/daily-phrase

# Test random phrase
curl http://localhost:8000/phrase-random

# Test all phrases endpoint
curl http://localhost:8000/phrases
```

### Managing Dependencies

```bash
# Install dependencies
pip install -r requirements.txt  # If requirements.txt exists

# Or install FastAPI and uvicorn directly
pip install fastapi uvicorn

# Freeze current dependencies
pip freeze > requirements.txt
```

## API Endpoints

- `GET /` - Welcome message
- `GET /daily-phrase` - Returns deterministic daily phrase based on current date
- `GET /phrase-random` - Returns random phrase from database
- `GET /phrases` - Returns all phrases with total count

## Development Notes

### File Paths

The database is loaded using relative path `app/database.json`. When running the application, ensure the working directory is the repository root so the relative path resolves correctly.

### Adding Phrases

To add new phrases, edit `app/database.json` and append entries following the existing schema:
```json
{
  "id": <next_sequential_id>,
  "texto": "<quote_text>",
  "autor": "<attribution>"
}
```

### Code Style

- Spanish language used for: comments, docstrings, variable names related to business logic
- English used for: technical terms (FastAPI decorators, Python keywords)
- Docstrings follow simple format describing endpoint purpose

### Virtual Environment

This project uses a Python virtual environment in `venv/`. Always activate before development:
```bash
source venv/bin/activate
```
