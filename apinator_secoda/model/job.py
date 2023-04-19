from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, List, Dict, Union
from uuid import UUID

from pydantic import AnyUrl, BaseModel, Field, conint, constr

from .common import EntityTypeEnum, NullEnum


class PatchedJob(BaseModel):
    id: Optional[UUID] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    entity_type: Union[EntityTypeEnum, Optional[NullEnum]] = None
    native_type: Optional[constr(max_length=50)] = None
    icon: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    definition: Optional[str] = None
    multiplayers: Optional[List[UUID]] = None
    multiplayer_last_modified_by: Optional[UUID] = None
    multiplayer_last_modified: Optional[datetime] = None
    owners: Optional[List[UUID]] = None
    owners_groups: Optional[List[UUID]] = None
    collections: Optional[List[UUID]] = None
    tags: Dict[str, Optional[Any]] = None
    workspace_id: Optional[UUID] = None
    total_usage: Optional[conint(ge=-2147483648, le=2147483647)] = None
    published: Optional[bool] = None
    archived: Optional[bool] = None
    pii: Optional[bool] = None
    verified: Optional[bool] = None
    url: Optional[str] = None
    parent: Optional[UUID] = None
    children_count: Optional[int] = None
    properties: Dict[str, Optional[Any]] = None
    bookmarked_by: Optional[List[UUID]] = None
    integration: Optional[UUID] = None
    external_updated_at: Optional[datetime] = None
    internal_usage: Optional[conint(ge=-2147483648, le=2147483647)] = None
    internal_users: Dict[str, Optional[Any]] = None
    external_users: Dict[str, Optional[Any]] = None
    external_usage: Optional[conint(ge=-2147483648, le=2147483647)] = None
    databuilder_id: Optional[str] = None
    viewers_delta: Dict[str, Optional[Any]] = None
    search_metadata: Dict[str, Optional[Any]] = None
    pristine: Optional[bool] = None
    sources: Optional[List[UUID]] = None
    product: Optional[str] = None


class PatchedJobGroup(BaseModel):
    id: Optional[UUID] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    entity_type: Union[EntityTypeEnum, Optional[NullEnum]] = None
    native_type: Optional[constr(max_length=50)] = None
    icon: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    definition: Optional[str] = None
    multiplayers: Optional[List[UUID]] = None
    multiplayer_last_modified_by: Optional[UUID] = None
    multiplayer_last_modified: Optional[datetime] = None
    owners: Optional[List[UUID]] = None
    owners_groups: Optional[List[UUID]] = None
    collections: Optional[List[UUID]] = None
    tags: Dict[str, Optional[Any]] = None
    workspace_id: Optional[UUID] = None
    total_usage: Optional[conint(ge=-2147483648, le=2147483647)] = None
    published: Optional[bool] = None
    archived: Optional[bool] = None
    pii: Optional[bool] = None
    verified: Optional[bool] = None
    url: Optional[str] = None
    parent: Optional[UUID] = None
    children_count: Optional[int] = None
    properties: Dict[str, Optional[Any]] = None
    bookmarked_by: Optional[List[UUID]] = None
    integration: Optional[UUID] = None
    external_updated_at: Optional[datetime] = None
    internal_usage: Optional[conint(ge=-2147483648, le=2147483647)] = None
    internal_users: Dict[str, Optional[Any]] = None
    external_users: Dict[str, Optional[Any]] = None
    external_usage: Optional[conint(ge=-2147483648, le=2147483647)] = None
    databuilder_id: Optional[str] = None
    viewers_delta: Dict[str, Optional[Any]] = None
    search_metadata: Dict[str, Optional[Any]] = None
    pristine: Optional[bool] = None
    sources: Optional[List[UUID]] = None


class PatchedJobRun(BaseModel):
    id: Optional[UUID] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    entity_type: Union[EntityTypeEnum, Optional[NullEnum]] = None
    native_type: Optional[constr(max_length=50)] = None
    icon: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    definition: Optional[str] = None
    multiplayers: Optional[List[UUID]] = None
    multiplayer_last_modified_by: Optional[UUID] = None
    multiplayer_last_modified: Optional[datetime] = None
    owners: Optional[List[UUID]] = None
    owners_groups: Optional[List[UUID]] = None
    collections: Optional[List[UUID]] = None
    tags: Dict[str, Optional[Any]] = None
    workspace_id: Optional[UUID] = None
    total_usage: Optional[conint(ge=-2147483648, le=2147483647)] = None
    published: Optional[bool] = None
    archived: Optional[bool] = None
    pii: Optional[bool] = None
    verified: Optional[bool] = None
    url: Optional[str] = None
    parent: Optional[UUID] = None
    children_count: Optional[int] = None
    properties: Dict[str, Optional[Any]] = None
    bookmarked_by: Optional[List[UUID]] = None
    integration: Optional[UUID] = None
    external_updated_at: Optional[datetime] = None
    internal_usage: Optional[conint(ge=-2147483648, le=2147483647)] = None
    internal_users: Dict[str, Optional[Any]] = None
    external_users: Dict[str, Optional[Any]] = None
    external_usage: Optional[conint(ge=-2147483648, le=2147483647)] = None
    databuilder_id: Optional[str] = None
    viewers_delta: Dict[str, Optional[Any]] = None
    search_metadata: Dict[str, Optional[Any]] = None
    pristine: Optional[bool] = None
    sources: Optional[List[UUID]] = None
    error: Optional[str] = None
    status: Optional[str] = None
    run_created_at: Optional[datetime] = None
    run_finished_at: Optional[datetime] = None


class PatchedJobTask(BaseModel):
    id: Optional[UUID] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    entity_type: Union[EntityTypeEnum, Optional[NullEnum]] = None
    native_type: Optional[constr(max_length=50)] = None
    icon: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    definition: Optional[str] = None
    multiplayers: Optional[List[UUID]] = None
    multiplayer_last_modified_by: Optional[UUID] = None
    multiplayer_last_modified: Optional[datetime] = None
    owners: Optional[List[UUID]] = None
    owners_groups: Optional[List[UUID]] = None
    collections: Optional[List[UUID]] = None
    tags: Dict[str, Optional[Any]] = None
    workspace_id: Optional[UUID] = None
    total_usage: Optional[conint(ge=-2147483648, le=2147483647)] = None
    published: Optional[bool] = None
    archived: Optional[bool] = None
    pii: Optional[bool] = None
    verified: Optional[bool] = None
    url: Optional[str] = None
    parent: Optional[UUID] = None
    children_count: Optional[int] = None
    properties: Dict[str, Optional[Any]] = None
    bookmarked_by: Optional[List[UUID]] = None
    integration: Optional[UUID] = None
    external_updated_at: Optional[datetime] = None
    internal_usage: Optional[conint(ge=-2147483648, le=2147483647)] = None
    internal_users: Dict[str, Optional[Any]] = None
    external_users: Dict[str, Optional[Any]] = None
    external_usage: Optional[conint(ge=-2147483648, le=2147483647)] = None
    databuilder_id: Optional[str] = None
    viewers_delta: Dict[str, Optional[Any]] = None
    search_metadata: Dict[str, Optional[Any]] = None
    pristine: Optional[bool] = None
    sources: Optional[List[UUID]] = None
    start_timestamp: Optional[datetime] = None
    finish_timestamp: Optional[datetime] = None


class Job(BaseModel):
    id: UUID
    created_at: datetime
    updated_at: datetime
    entity_type: Union[EntityTypeEnum, Optional[NullEnum]] = None
    native_type: Optional[constr(max_length=50)] = None
    icon: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    definition: Optional[str] = None
    multiplayers: Optional[List[UUID]] = None
    multiplayer_last_modified_by: Optional[UUID] = None
    multiplayer_last_modified: Optional[datetime] = None
    owners: Optional[List[UUID]] = None
    owners_groups: Optional[List[UUID]] = None
    collections: Optional[List[UUID]] = None
    tags: Dict[str, Optional[Any]] = None
    workspace_id: UUID
    total_usage: Optional[conint(ge=-2147483648, le=2147483647)] = None
    published: Optional[bool] = None
    archived: Optional[bool] = None
    pii: Optional[bool] = None
    verified: Optional[bool] = None
    url: Optional[str] = None
    parent: Optional[UUID] = None
    children_count: Optional[int] = None
    properties: Dict[str, Optional[Any]] = None
    bookmarked_by: Optional[List[UUID]] = None
    integration: Optional[UUID] = None
    external_updated_at: Optional[datetime] = None
    internal_usage: Optional[conint(ge=-2147483648, le=2147483647)] = None
    internal_users: Dict[str, Optional[Any]] = None
    external_users: Dict[str, Optional[Any]] = None
    external_usage: Optional[conint(ge=-2147483648, le=2147483647)] = None
    databuilder_id: Optional[str] = None
    viewers_delta: Dict[str, Optional[Any]] = None
    search_metadata: Dict[str, Optional[Any]] = None
    pristine: Optional[bool] = None
    sources: List[UUID]
    product: Optional[str] = None


class JobGroup(BaseModel):
    id: UUID
    created_at: datetime
    updated_at: datetime
    entity_type: Union[EntityTypeEnum, Optional[NullEnum]] = None
    native_type: Optional[constr(max_length=50)] = None
    icon: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    definition: Optional[str] = None
    multiplayers: Optional[List[UUID]] = None
    multiplayer_last_modified_by: Optional[UUID] = None
    multiplayer_last_modified: Optional[datetime] = None
    owners: Optional[List[UUID]] = None
    owners_groups: Optional[List[UUID]] = None
    collections: Optional[List[UUID]] = None
    tags: Dict[str, Optional[Any]] = None
    workspace_id: UUID
    total_usage: Optional[conint(ge=-2147483648, le=2147483647)] = None
    published: Optional[bool] = None
    archived: Optional[bool] = None
    pii: Optional[bool] = None
    verified: Optional[bool] = None
    url: Optional[str] = None
    parent: Optional[UUID] = None
    children_count: Optional[int] = None
    properties: Dict[str, Optional[Any]] = None
    bookmarked_by: Optional[List[UUID]] = None
    integration: Optional[UUID] = None
    external_updated_at: Optional[datetime] = None
    internal_usage: Optional[conint(ge=-2147483648, le=2147483647)] = None
    internal_users: Dict[str, Optional[Any]] = None
    external_users: Dict[str, Optional[Any]] = None
    external_usage: Optional[conint(ge=-2147483648, le=2147483647)] = None
    databuilder_id: Optional[str] = None
    viewers_delta: Dict[str, Optional[Any]] = None
    search_metadata: Dict[str, Optional[Any]] = None
    pristine: Optional[bool] = None
    sources: List[UUID]


class JobList(BaseModel):
    id: UUID
    created_at: datetime
    updated_at: datetime
    title: Optional[str] = None
    product: Optional[str] = None
    owners: Optional[List[UUID]] = None
    owners_groups: Optional[List[UUID]] = None
    collections: Optional[List[UUID]] = None
    published: Optional[bool] = None
    pii: Optional[bool] = None
    tags: Dict[str, Optional[Any]] = None
    url: Optional[str] = None
    description: Optional[str] = None
    integration: Optional[UUID] = None
    entity_type: Union[EntityTypeEnum, Optional[NullEnum]] = None
    parent_id: UUID
    external_updated_at: Optional[datetime] = None
    internal_usage: Optional[conint(ge=-2147483648, le=2147483647)] = None
    external_usage: Optional[conint(ge=-2147483648, le=2147483647)] = None
    viewers_delta: Dict[str, Optional[Any]] = None
    pristine: Optional[bool] = None
    verified: Optional[bool] = None
    properties: Dict[str, Optional[Any]] = None


class JobRun(BaseModel):
    id: UUID
    created_at: datetime
    updated_at: datetime
    entity_type: Union[EntityTypeEnum, Optional[NullEnum]] = None
    native_type: Optional[constr(max_length=50)] = None
    icon: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    definition: Optional[str] = None
    multiplayers: Optional[List[UUID]] = None
    multiplayer_last_modified_by: Optional[UUID] = None
    multiplayer_last_modified: Optional[datetime] = None
    owners: Optional[List[UUID]] = None
    owners_groups: Optional[List[UUID]] = None
    collections: Optional[List[UUID]] = None
    tags: Dict[str, Optional[Any]] = None
    workspace_id: UUID
    total_usage: Optional[conint(ge=-2147483648, le=2147483647)] = None
    published: Optional[bool] = None
    archived: Optional[bool] = None
    pii: Optional[bool] = None
    verified: Optional[bool] = None
    url: Optional[str] = None
    parent: Optional[UUID] = None
    children_count: Optional[int] = None
    properties: Dict[str, Optional[Any]] = None
    bookmarked_by: Optional[List[UUID]] = None
    integration: Optional[UUID] = None
    external_updated_at: Optional[datetime] = None
    internal_usage: Optional[conint(ge=-2147483648, le=2147483647)] = None
    internal_users: Dict[str, Optional[Any]] = None
    external_users: Dict[str, Optional[Any]] = None
    external_usage: Optional[conint(ge=-2147483648, le=2147483647)] = None
    databuilder_id: Optional[str] = None
    viewers_delta: Dict[str, Optional[Any]] = None
    search_metadata: Dict[str, Optional[Any]] = None
    pristine: Optional[bool] = None
    sources: List[UUID]
    error: Optional[str] = None
    status: Optional[str] = None
    run_created_at: Optional[datetime] = None
    run_finished_at: Optional[datetime] = None


class JobTask(BaseModel):
    id: UUID
    created_at: datetime
    updated_at: datetime
    entity_type: Union[EntityTypeEnum, Optional[NullEnum]] = None
    native_type: Optional[constr(max_length=50)] = None
    icon: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    definition: Optional[str] = None
    multiplayers: Optional[List[UUID]] = None
    multiplayer_last_modified_by: Optional[UUID] = None
    multiplayer_last_modified: Optional[datetime] = None
    owners: Optional[List[UUID]] = None
    owners_groups: Optional[List[UUID]] = None
    collections: Optional[List[UUID]] = None
    tags: Dict[str, Optional[Any]] = None
    workspace_id: UUID
    total_usage: Optional[conint(ge=-2147483648, le=2147483647)] = None
    published: Optional[bool] = None
    archived: Optional[bool] = None
    pii: Optional[bool] = None
    verified: Optional[bool] = None
    url: Optional[str] = None
    parent: Optional[UUID] = None
    children_count: Optional[int] = None
    properties: Dict[str, Optional[Any]] = None
    bookmarked_by: Optional[List[UUID]] = None
    integration: Optional[UUID] = None
    external_updated_at: Optional[datetime] = None
    internal_usage: Optional[conint(ge=-2147483648, le=2147483647)] = None
    internal_users: Dict[str, Optional[Any]] = None
    external_users: Dict[str, Optional[Any]] = None
    external_usage: Optional[conint(ge=-2147483648, le=2147483647)] = None
    databuilder_id: Optional[str] = None
    viewers_delta: Dict[str, Optional[Any]] = None
    search_metadata: Dict[str, Optional[Any]] = None
    pristine: Optional[bool] = None
    sources: List[UUID]
    start_timestamp: Optional[datetime] = None
    finish_timestamp: Optional[datetime] = None


class PaginatedJobGroupList(BaseModel):
    count: Optional[int] = Field(None, example=123)
    next: Optional[AnyUrl] = Field(
        None, example="http://api.example.org/accounts/?page=4"
    )
    previous: Optional[AnyUrl] = Field(
        None, example="http://api.example.org/accounts/?page=2"
    )
    results: Optional[List[JobGroup]] = None


class PaginatedJobListList(BaseModel):
    count: Optional[int] = Field(None, example=123)
    next: Optional[AnyUrl] = Field(
        None, example="http://api.example.org/accounts/?page=4"
    )
    previous: Optional[AnyUrl] = Field(
        None, example="http://api.example.org/accounts/?page=2"
    )
    results: Optional[List[JobList]] = None


class PaginatedJobRunList(BaseModel):
    count: Optional[int] = Field(None, example=123)
    next: Optional[AnyUrl] = Field(
        None, example="http://api.example.org/accounts/?page=4"
    )
    previous: Optional[AnyUrl] = Field(
        None, example="http://api.example.org/accounts/?page=2"
    )
    results: Optional[List[JobRun]] = None


class PaginatedJobTaskList(BaseModel):
    count: Optional[int] = Field(None, example=123)
    next: Optional[AnyUrl] = Field(
        None, example="http://api.example.org/accounts/?page=4"
    )
    previous: Optional[AnyUrl] = Field(
        None, example="http://api.example.org/accounts/?page=2"
    )
    results: Optional[List[JobTask]] = None
