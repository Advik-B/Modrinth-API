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


@dataclass
class ModrinthDonationURL:
    id: str
    platform: str
    url: str


ModrinthStats = Literal["approved", "rejected", "pending", "unreviewed"]


@dataclass
class ModrinthLicense:
    id: str
    name: str
    url: str


@dataclass
class ModrinthImage:
    url: str
    featured: bool
    title: str
    description: str
    created: str
