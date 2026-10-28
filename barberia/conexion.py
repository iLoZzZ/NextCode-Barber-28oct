
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

URI = os.getenv("MONGODB_URI")

cliente_mongo = MongoClient(URI)

db = cliente_mongo["barberiaNextCode"]

barberos = db["barberos"]
clientes = db["clientes"]
servicios = db["servicios"]
horarios = db["horarios"]
citas = db["citas"]
productos = db["productos"]
notificaciones = db["notificaciones"]
