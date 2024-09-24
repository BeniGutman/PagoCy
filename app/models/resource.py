from enum import Enum
from datetime import datetime
from typing import Optional, Dict
from pydantic import BaseModel


class ResourceType(str, Enum):
    User = "User"
    Group = "Group"
    Repository = "Repository"
    Branch = "Branch"


class Resource(BaseModel):
    scan_id: int
    urn: str
    name: str
    type: ResourceType
    date_fetched: datetime
    data: str | dict = None
