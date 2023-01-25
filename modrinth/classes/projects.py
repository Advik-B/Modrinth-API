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

    @staticmethod
    def from_dict(data: dict) -> "ModrinthProject":
        return ModrinthProject(
            slug=data["slug"],
            title=data["title"],
            description=data["description"],
            categories=data["categories"],
            client_side=data["client_side"],
            server_side=data["server_side"],
            additional_categories=[
                ModrinthCategory.from_dict(category)
                for category in data["additional_categories"]
            ],
            issues_url=data["issues_url"],
            source_url=data["source_url"],
            wiki_url=data["wiki_url"],
            discord_url=data["discord_url"],
            donation_urls=[
                ModrinthDonationURL.from_dict(url) for url in data["donation_urls"]
            ],
            project_type=data["project_type"],
            downloads=data["downloads"],
            icon_url=data["icon_url"],
            id=data["id"],
            team=data["team"],
            body_url=data["body_url"],
            moderator_message=data["moderator_message"],
            published=data["published"],
            updated=data["updated"],
            approved=data["approved"],
            followers=data["followers"],
            status=data["status"],
            license=ModrinthLicense.from_dict(data["license"]),
            versions=data["versions"],
            gallery=[ModrinthImage.from_dict(image) for image in data["gallery"]],
            body=data["body"],
        )

