# 1. Image de base : Python léger (Linux)
FROM python:3.9-slim

# 2. On définit le dossier de travail dans le conteneur
WORKDIR /app

# 3. On installe les dépendances système nécessaires (pour OpenCV/YOLO si besoin)
RUN apt-get update && apt-get install -y \
    build-essential \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# 4. On copie d'abord les requirements pour profiter du cache Docker
COPY requirements.txt .

# 5. On installe les librairies Python
RUN pip install --no-cache-dir -r requirements.txt

# 6. On copie tout le reste du code (app.py, style.css, assets...)
COPY . .

# 7. On expose le port standard de Streamlit
EXPOSE 8501

# 8. Commande de lancement (On force l'adresse 0.0.0.0 pour être vu de l'extérieur)
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]