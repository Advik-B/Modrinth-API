from typing import Literal
from dataclasses import dataclass

ModrinthBoolean = Literal["required", "optional", "unsupported"]


@dataclass
class ModrinthSVG:
    svg: str


@dataclass
class ModrinthCategory:
    name: str
    description: str
    project_type: str
    header: str
    icon: ModrinthSVG

    @staticmethod
    def from_dict(data: dict) -> "ModrinthCategory":
        return ModrinthCategory(
            name=data["name"],
            description=data["description"],
            project_type=data["project_type"],
            header=data["header"],
            icon=ModrinthSVG.from_dict(data["icon"]),
        )


@dataclass
class ModrinthDonationURL:
    id: str
    platform: str
    url: str

    @staticmethod
    def from_dict(data: dict) -> "ModrinthDonationURL":
        return ModrinthDonationURL(
            id=data["id"],
            platform=data["platform"],
            url=data["url"],
        )


ModrinthStats = Literal["approved", "rejected", "pending", "unreviewed"]


@dataclass
class ModrinthLicense:
    id: str
    name: str
    url: str

    @staticmethod
    def from_dict(data: dict) -> "ModrinthLicense":
        return ModrinthLicense(
            id=data["id"],
            name=data["name"],
            url=data["url"],
        )


@dataclass
class ModrinthImage:
    url: str
    featured: bool
    title: str
    description: str
    created: str

    @staticmethod
    def from_dict(data: dict) -> "ModrinthImage":
        return ModrinthImage(
            url=data["url"],
            featured=data["featured"],
            title=data["title"],
            description=data["description"],
            created=data["created"],
        )
