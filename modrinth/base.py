from dataclasses import dataclass
from requests import get, post
from warnings import simplefilter
from urllib3.connectionpool import InsecureRequestWarning
from diskcache import Cache

BASE_URL = "http://api.modrinth.com"

@dataclass
class ModrinthClient:
    version: str = "v2"
    cache: bool = False
    cache_dir: str = "cache/modrinth"

    def __post_init__(self):
        if self.cache:
            self.cache_obj = Cache(self.cache_dir)

    def fetch_raw(self, url: str, queries: dict = None, method: str = "GET"):
        if queries is None:
            queries = {}

        method = method.casefold()
        # The queries are passed as a dictionary, but the API expects them as a string.
        # Example: {"query": "Midnight"} -> "query=Midnight"
        # For multiple queries, the API expects them to be separated by "&".
        # Example: {"query": "Midnight", "author": "Cryptic-Mushroom"} -> "query=Midnight&author=Cryptic-Mushroom"
        queries = "&".join([f"{key}={value}" for key, value in queries.items()])
        simplefilter("ignore", InsecureRequestWarning)
        if method == "get":
            return get(
                f"{BASE_URL}/{self.version}/{url}?{queries}",
                verify=False
            )
        elif method == "post":
            return post(
                f"{BASE_URL}/{self.version}/{url}?{queries}",
                verify=False
            )
        simplefilter("default", InsecureRequestWarning)

    def fetch(self, url: str, params: dict = None, method: str = "GET") -> dict:
        if params is None:
            params = {}

        if self.cache:
            temp = self.cache_obj.get(url)
        if self.cache and temp is not None:
            return temp["hits"]

        response = self.fetch_raw(url, params, method)
        if response.status_code == 200:
            data = response.json()
            if self.cache:
                self.cache_obj.set(url, data)
            return data["hits"]

