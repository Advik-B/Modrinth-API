from dataclasses import dataclass
from .general import ModrinthBoolean, ModrinthCategory, ModrinthDonationURL
from typing import Generator
@dataclass
class ModrinthProject:
    slug: str
    title: str
    description: str
    categories: list
    client_side: ModrinthBoolean
    server_side: ModrinthBoolean
    body: str
    additional_categories: list[ModrinthCategory]
    issues_url: str
    source_url: str
    wiki_url: str
    discord_url: str
    donation_urls: list[ModrinthDonationURL]