import time
import random
import math


pessoas = [
    ("Amanda", "CWB"),
    ("Pedro", "GIG"),
    ("Marcos", "POA"),
    ("Priscila", "FLN"),
    ("Jessica", "CNF"),
    ("Paulo", "GYN")
]

destino = "GRU"

voos = {}

with open("voos.txt", "r+") as arquivo:
    for linha in arquivo:
        origem, destino, saida, chegada, preco = linha.split(",")
        voos.setdefault((origem, destino), [])
        voos[(origem, destino)].append((saida, chegada, int(preco)))

