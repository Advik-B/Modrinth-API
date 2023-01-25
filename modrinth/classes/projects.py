from dataclasses import dataclass
from .general import (
    ModrinthBoolean,
    ModrinthCategory,
    ModrinthDonationURL,
    ModrinthStats,
    ModrinthLicense,
    ModrinthImage,
)
from typing import Literal, Union

ModrinthProjectType = Literal[
    "mod",
    "plugin",
    "data_pack",
    "shader",
    "resource_pack",
    "modpack",
]


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
    project_type: ModrinthProjectType
    downloads: int
    icon_url: str
    id: str
    team: str
    body_url: Union[str, None]
    moderator_message: Union[str, None]
    published: str
    updated: str
    approved: str
    followers: int
    status: ModrinthStats
    license: ModrinthLicense
    versions: list[str]
    gallery: list[ModrinthImage]
