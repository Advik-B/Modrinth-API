from .base import ModrinthClient
from pprint import pprint

client = ModrinthClient(cache=True)

print("Fetching project...")
project = client.get_project("iris")
for img in project.versions:
    print(img)