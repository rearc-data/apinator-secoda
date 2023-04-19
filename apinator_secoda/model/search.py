from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, List, Dict, Union
from uuid import UUID

from pydantic import AnyUrl, BaseModel, Field, conint, constr

from .common import EntityTypeEnum, NullEnum


class PatchedSearch(BaseModel):
    id: Optional[UUID] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    entity_type: Union[EntityTypeEnum, Optional[NullEnum]] = None
    native_type: Optional[constr(max_length=50)] = None
    icon: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    search_metadata: Dict[str, Optional[Any]] = None
    url: Optional[str] = None
    pii: Optional[bool] = None
    verified: Optional[bool] = None
    properties: Dict[str, Optional[Any]] = None
    external_updated_at: Optional[datetime] = None
    integration: Optional[UUID] = None
    internal_usage: Optional[conint(ge=-2147483648, le=2147483647)] = None
    external_usage: Optional[conint(ge=-2147483648, le=2147483647)] = None
    total_usage: Optional[conint(ge=-2147483648, le=2147483647)] = None
    parent: Optional[UUID] = None
    viewers_delta: Dict[str, Optional[Any]] = None
    pristine: Optional[bool] = None


class Search(BaseModel):
    id: UUID
    created_at: datetime
    updated_at: datetime
    entity_type: Union[EntityTypeEnum, Optional[NullEnum]] = None
    native_type: Optional[constr(max_length=50)] = None
    icon: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    search_metadata: Dict[str, Optional[Any]] = None
    url: Optional[str] = None
    pii: Optional[bool] = None
    verified: Optional[bool] = None
    properties: Dict[str, Optional[Any]] = None
    external_updated_at: Optional[datetime] = None
    integration: Optional[UUID] = None
    internal_usage: Optional[conint(ge=-2147483648, le=2147483647)] = None
    external_usage: Optional[conint(ge=-2147483648, le=2147483647)] = None
    total_usage: Optional[conint(ge=-2147483648, le=2147483647)] = None
    parent: UUID
    viewers_delta: Dict[str, Optional[Any]] = None
    pristine: Optional[bool] = None


class PaginatedSearchList(BaseModel):
    count: Optional[int] = Field(None, example=123)
    next: Optional[AnyUrl] = Field(
        None, example="http://api.example.org/accounts/?page=4"
    )
    previous: Optional[AnyUrl] = Field(
        None, example="http://api.example.org/accounts/?page=2"
    )
    results: Optional[List[Search]] = None
