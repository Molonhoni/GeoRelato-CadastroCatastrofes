import json
import os
from math import radians, cos, sin, sqrt, atan2

def calcular_distancia(coord1, coord2):
    R = 6371  # raio da Terra em km
    lat1, lon1 = coord1
    lat2, lon2 = coord2

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distancia = R * c
    return distancia

def carregar_dados(caminho):
    if not os.path.exists(caminho):
        return {"relatores": [], "relatos": []}
    with open(caminho, "r") as f:
        return json.load(f)

def salvar_dados(caminho, dados):
    with open(caminho, "w") as f:
        json.dump(dados, f, indent=4)
