from __future__ import annotations

from typing import Any, Optional, List, Dict
from uuid import UUID

from pydantic import AnyUrl, BaseModel, Field


class Announcement(BaseModel):
    title: Optional[str] = None
    properties: Dict[str, Optional[Any]] = None
    definition: Optional[str] = None
    receivers: Optional[List[UUID]] = None
    sender: UUID
    read: Optional[bool] = None
    integration: Optional[UUID] = None
    receiver_slack_channel_ids: Dict[str, Optional[Any]] = None


class PaginatedAnnouncementList(BaseModel):
    count: Optional[int] = Field(None, example=123)
    next: Optional[AnyUrl] = Field(
        None, example="http://api.example.org/accounts/?page=4"
    )
    previous: Optional[AnyUrl] = Field(
        None, example="http://api.example.org/accounts/?page=2"
    )
    results: Optional[List[Announcement]] = None


class PatchedAnnouncement(BaseModel):
    title: Optional[str] = None
    properties: Dict[str, Optional[Any]] = None
    definition: Optional[str] = None
    receivers: Optional[List[UUID]] = None
    sender: Optional[UUID] = None
    read: Optional[bool] = None
    integration: Optional[UUID] = None
    receiver_slack_channel_ids: Dict[str, Optional[Any]] = None
