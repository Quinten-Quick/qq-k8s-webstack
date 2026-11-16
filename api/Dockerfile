# 1. Start vanaf een lichtgewicht Python base-image
FROM python:3.12-slim

# 2. Zet de werkmap in de container op /app
WORKDIR /app

# 3. Installeer eerst alleen de dependencies (zodat Docker deze laag kan hergebruiken)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Kopieer je FastAPI-code en maak een non-root gebruiker aan
COPY main.py .
RUN useradd -m appuser && chown -R appuser:appuser /app

# 5. Draai de API als non-root gebruiker voor extra veiligheid
USER appuser

# 6. Geef aan dat Uvicorn luistert op poort 8000
EXPOSE 8000

# 7. Start de FastAPI-server op alle netwerkinterfaces (0.0.0.0)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]