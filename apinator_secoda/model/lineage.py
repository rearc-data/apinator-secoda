from __future__ import annotations

from datetime import datetime
from typing import Optional, List
from uuid import UUID

from pydantic import AnyUrl, BaseModel, Field


class LineageAPI(BaseModel):
    id: UUID
    created_at: datetime
    updated_at: datetime
    from_entity: UUID
    to_entity: UUID
    direction: str


class PaginatedLineageAPIList(BaseModel):
    count: Optional[int] = Field(None, example=123)
    next: Optional[AnyUrl] = Field(
        None, example="http://api.example.org/accounts/?page=4"
    )
    previous: Optional[AnyUrl] = Field(
        None, example="http://api.example.org/accounts/?page=2"
    )
    results: Optional[List[LineageAPI]] = None


class PatchedLineageAPI(BaseModel):
    id: Optional[UUID] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    from_entity: Optional[UUID] = None
    to_entity: Optional[UUID] = None
    direction: Optional[str] = None
