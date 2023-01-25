from .base import ModrinthClient
from pprint import pprint

client = ModrinthClient(cache=True)
mods = client.fetch("search", {"query": "Sodium"})

for mod in mods:
    pprint(mod["title"])
    print("." * 80)
