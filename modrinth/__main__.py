from .base import ModrinthClient

client = ModrinthClient(cache=True)
mods = client.fetch("mod", {"query": "Midnight"})

print(mods)
