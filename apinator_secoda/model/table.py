from __future__ import annotations

import random
import string
from datetime import datetime
from typing import Any, Optional, List, Dict, Union
from uuid import UUID

from pydantic import AnyUrl, BaseModel, Field, conint, constr

from .common import (
    EntityTypeEnum,
    NullEnum,
    PaginatedBase,
)
from .query import LimitedQuery


class PatchedColumn(BaseModel):
    id: Optional[UUID] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    entity_type: Union[EntityTypeEnum, Optional[NullEnum]] = None
    native_type: Optional[constr(max_length=50)] = None
    icon: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    multiplayers: Optional[List[UUID]] = None
    multiplayer_last_modified_by: Optional[UUID] = None
    multiplayer_last_modified: Optional[datetime] = None
    owners: Optional[List[UUID]] = None
    owners_groups: Optional[List[UUID]] = None
    collections: Optional[List[UUID]] = None
    tags: Dict[str, Optional[Any]] = None
    workspace_id: Optional[UUID] = None
    published: Optional[bool] = None
    archived: Optional[bool] = None
    pii: Optional[bool] = None
    verified: Optional[bool] = None
    url: Optional[str] = None
    parent: Optional[UUID] = None
    properties: Dict[str, Optional[Any]] = None
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
    type: Optional[str] = None
    sort_order: Optional[conint(ge=-2147483648, le=2147483647)] = None
    is_pk: Optional[bool] = None
    stale: Optional[bool] = None
    hidden: Optional[bool] = None
    table_cluster: Optional[str] = None
    table_database: Optional[str] = None
    table_schema: Optional[str] = None
    table_title: Optional[str] = None


class PatchedTable(BaseModel):
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
    children_count: Optional[str] = None
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
    schema_: Optional[str] = Field(None, alias="schema")
    database: Optional[str] = None
    cluster: Optional[str] = None
    type: Optional[str] = None
    stale: Optional[bool] = None
    creation_query: Optional[LimitedQuery] = None


class PatchedTableTreeList(BaseModel):
    id: Optional[UUID] = None
    title: Optional[str] = None
    schema_: Optional[str] = Field(None, alias="schema")
    database: Optional[str] = None
    cluster: Optional[str] = None
    type: Optional[str] = None
    entity_type: Union[EntityTypeEnum, Optional[NullEnum]] = None


class Table(BaseModel):
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
    children_count: str
    properties: Dict[str, Optional[Any]] = None
    bookmarked_by: Optional[List[UUID]] = None
    integration: Optional[UUID] = None
    external_updated_at: Optional[datetime] = None
    internal_usage: Optional[conint(ge=-2147483648, le=2147483647)] = None
    internal_users: Optional[List[str]] = None
    external_users: Optional[List[str]] = None
    external_usage: Optional[conint(ge=-2147483648, le=2147483647)] = None
    databuilder_id: Optional[str] = None
    viewers_delta: Dict[str, Optional[Any]] = None
    search_metadata: Dict[str, Optional[Any]] = None
    pristine: Optional[bool] = None
    sources: Optional[List[UUID]] = None
    schema_: Optional[str] = Field(None, alias="schema")
    database: Optional[str] = None
    cluster: Optional[str] = None
    type: Optional[str] = None
    stale: Optional[bool] = None
    creation_query: Optional[LimitedQuery] = None

    def update_custom_property(self, key: str, value: Any) -> None:
        self.properties = self.properties or {}
        self.properties.setdefault("custom", [])
        custom_props = self.properties["custom"]
        for custom_prop in custom_props:
            if custom_prop["name"] == key:
                custom_prop["value"] = value
                custom_prop["updated_at"] = datetime.utcnow().isoformat()
                break
        else:
            custom_props.append(
                dict(
                    id="".join(
                        random.choices(string.ascii_lowercase + string.digits, k=25)
                    ),
                    name=key,
                    value=value,
                    type="string",
                    order=len(custom_props),
                    created_at=datetime.utcnow().isoformat(),
                    updated_at=datetime.utcnow().isoformat(),
                )
            )


class TableList(BaseModel):
    id: UUID
    created_at: datetime
    updated_at: datetime
    title: Optional[str] = None
    schema_: Optional[str] = Field(None, alias="schema")
    database: Optional[str] = None
    cluster: Optional[str] = None
    type: Optional[str] = None
    owners: Optional[List[UUID]] = None
    owners_groups: Optional[List[UUID]] = None
    collections: Optional[List[UUID]] = None
    published: Optional[bool] = None
    pii: Optional[bool] = None
    tags: Optional[List[UUID]] = None
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


class TableTreeList(BaseModel):
    id: UUID
    title: Optional[str] = None
    schema_: Optional[str] = Field(None, alias="schema")
    database: Optional[str] = None
    cluster: Optional[str] = None
    type: Optional[str] = None
    entity_type: Union[EntityTypeEnum, Optional[NullEnum]] = None


class Column(BaseModel):
    id: UUID
    created_at: datetime
    updated_at: datetime
    entity_type: Union[EntityTypeEnum, Optional[NullEnum]] = None
    native_type: Optional[constr(max_length=50)] = None
    icon: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    multiplayers: Optional[List[UUID]] = None
    multiplayer_last_modified_by: Optional[UUID] = None
    multiplayer_last_modified: Optional[datetime] = None
    owners: Optional[List[UUID]] = None
    owners_groups: Optional[List[UUID]] = None
    collections: Optional[List[UUID]] = None
    tags: Dict[str, Optional[Any]] = None
    workspace_id: UUID
    published: Optional[bool] = None
    archived: Optional[bool] = None
    pii: Optional[bool] = None
    verified: Optional[bool] = None
    url: Optional[str] = None
    parent: Optional[UUID] = None
    properties: Dict[str, Optional[Any]] = None
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
    type: Optional[str] = None
    sort_order: Optional[conint(ge=-2147483648, le=2147483647)] = None
    is_pk: Optional[bool] = None
    stale: Optional[bool] = None
    hidden: Optional[bool] = None
    table_cluster: Optional[str] = None
    table_database: Optional[str] = None
    table_schema: Optional[str] = None
    table_title: Optional[str] = None


class PaginatedColumnList(BaseModel):
    count: Optional[int] = Field(None, example=123)
    next: Optional[AnyUrl] = Field(
        None, example="http://api.example.org/accounts/?page=4"
    )
    previous: Optional[AnyUrl] = Field(
        None, example="http://api.example.org/accounts/?page=2"
    )
    results: Optional[List[Column]] = None


class PaginatedTableListList(PaginatedBase):
    results: Optional[List[TableList]] = None


class PatchedSecodaCluster(BaseModel):
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


class PatchedSecodaDatabase(BaseModel):
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
    stale: Optional[bool] = None


class PatchedSecodaSchema(BaseModel):
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
    database: Optional[str] = None
    visible: Optional[bool] = None


class SecodaCluster(BaseModel):
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


class SecodaDatabase(BaseModel):
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
    stale: Optional[bool] = None


class SecodaSchema(BaseModel):
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
    database: str
    visible: Optional[bool] = None


class PaginatedSecodaClusterList(BaseModel):
    count: Optional[int] = Field(None, example=123)
    next: Optional[AnyUrl] = Field(
        None, example="http://api.example.org/accounts/?page=4"
    )
    previous: Optional[AnyUrl] = Field(
        None, example="http://api.example.org/accounts/?page=2"
    )
    results: Optional[List[SecodaCluster]] = None


class PaginatedSecodaDatabaseList(BaseModel):
    count: Optional[int] = Field(None, example=123)
    next: Optional[AnyUrl] = Field(
        None, example="http://api.example.org/accounts/?page=4"
    )
    previous: Optional[AnyUrl] = Field(
        None, example="http://api.example.org/accounts/?page=2"
    )
    results: Optional[List[SecodaDatabase]] = None


class PaginatedSecodaSchemaList(BaseModel):
    count: Optional[int] = Field(None, example=123)
    next: Optional[AnyUrl] = Field(
        None, example="http://api.example.org/accounts/?page=4"
    )
    previous: Optional[AnyUrl] = Field(
        None, example="http://api.example.org/accounts/?page=2"
    )
    results: Optional[List[SecodaSchema]] = None


class TestRun(BaseModel):
    id: UUID
    title: Optional[str] = None
    integration: Optional[UUID] = None
    suite_title: Optional[str] = None
    test_title: Optional[str] = None
    product: Optional[str] = None
    columns: Optional[List[str]] = None
    status: Optional[str] = None
    run_created_at: Optional[datetime] = None
    run_finished_at: Optional[datetime] = None
    result: Optional[str] = None
    error: Optional[str] = None


class PatchedTest(BaseModel):
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
    suite_title: Optional[str] = None
    product: Optional[str] = None
    columns: Optional[List[str]] = None
    latest_run: Optional[TestRun] = None


class Test(BaseModel):
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
    suite_title: Optional[str] = None
    product: Optional[str] = None
    columns: Optional[List[str]] = None
    latest_run: TestRun


class PaginatedTestList(BaseModel):
    count: Optional[int] = Field(None, example=123)
    next: Optional[AnyUrl] = Field(
        None, example="http://api.example.org/accounts/?page=4"
    )
    previous: Optional[AnyUrl] = Field(
        None, example="http://api.example.org/accounts/?page=2"
    )
    results: Optional[List[Test]] = None
