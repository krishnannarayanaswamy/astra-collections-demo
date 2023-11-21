import os, json

from astrapy.db import AstraDB

astra_db = AstraDB(
    api_endpoint=os.environ['ASTRA_DB_API_ENDPOINT'],
    token=os.environ['ASTRA_DB_APPLICATION_TOKEN'],
)

print(f"Connected to Astra DB: {astra_db.get_collections()}")