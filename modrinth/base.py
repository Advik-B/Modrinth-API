from dataclasses import dataclass
from requests import get, post
from diskcache import Cache
from .classes import ModrinthProject
from urllib3.connectionpool import InsecureRequestWarning
from warnings import simplefilter

BASE_URL = "http://api.modrinth.com"


@dataclass
class ModrinthClient:
    version: str = "v2"
    cache: bool = False
    cache_dir: str = "cache/modrinth"

    def __post_init__(self):
        if self.cache:
            self.cache_obj = Cache(self.cache_dir)

    def fetch_raw(self, path: str, queries: dict = None, method: str = "GET"):
        if queries is None:
            queries = {}

        method = method.casefold()
        # The queries are passed as a dictionary, but the API expects them as a string.
        # Example: {"query": "Midnight"} -> "query=Midnight"
        # For multiple queries, the API expects them to be separated by "&".
        # Example: {"query": "Midnight", "author": "Cryptic-Mushroom"} ->
        # "query=Midnight&author=Cryptic-Mushroom"
        queries = "&".join([f"{key}={value}" for key, value in queries.items()])
        URL = f"{BASE_URL}/{self.version}/{path}?{queries}"
        # print(URL)  # Debugging
        simplefilter("ignore", InsecureRequestWarning)
        if method == "get":
            return get(
                URL,
                verify=False,
            )
        elif method == "post":
            return post(
                URL,
                verify=False,
            )
        simplefilter("default", InsecureRequestWarning)

    def fetch(self, url: str, queries: dict = None, method: str = "GET") -> dict:
        if queries is None:
            queries = {}

        if self.cache:
            temp = self.cache_obj.get(url)
        if self.cache and temp is not None:
            return temp

        response = self.fetch_raw(url, queries, method)
        if response.status_code == 200:
            data = response.json()
            if self.cache:
                self.cache_obj.set(url, data)
            return data

    def get_project(self, project_id: str) -> ModrinthProject:
        return ModrinthProject.from_dict(self.fetch(f"project/{project_id}"))
