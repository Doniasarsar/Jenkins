# Utiliser l'image officielle Python
FROM python:3.13.0-alpine3.20

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le script sum.py dans le répertoire /app
COPY sum.py /app/sum.py

# Commande par défaut pour maintenir le conteneur actif
CMD ["tail", "-f", "/dev/null"]
