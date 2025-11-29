# Frase Diaria API 📖

Una API REST desarrollada con FastAPI que proporciona frases cristianas diarias para edificación.

## 🚀 Características

- **Frase del día**: Determinística basada en la fecha
- **Frase aleatoria**: Para inspiración instantánea
- **Lista completa**: Todas las frases disponibles
- **Base de datos**: 89+ frases de reformadores y escrituras

## 📚 Endpoints

- `GET /` - Página de inicio
- `GET /daily-phrase` - Frase del día
- `GET /phrase-random` - Frase aleatoria  
- `GET /phrases` - Todas las frases

## 🛠️ Tecnologías

- Python 3.8+
- FastAPI

## ⚡ Instalación

```bash
# Clonar repositorio
git clone https://github.com/tu-usuario/frase-diaria.git

# Entrar al directorio
cd frase-diaria

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar servidor
fastapi dev app/main.py 
```
## 🌐 Uso

Accede a la API en: http://localhost:8000

Documentación automática: http://localhost:8000/docs
