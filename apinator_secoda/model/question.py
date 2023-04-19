from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, List, Dict, Union
from uuid import UUID

from pydantic import AnyUrl, BaseModel, Field, conint, constr

from .common import EntityTypeEnum, NullEnum


class PartnerStackQuestion(BaseModel):
    id: UUID
    title: Optional[str] = None
    neo4j_id: str
    status: Optional[str] = None
    description: str
    answered_at: str
    has_answer: str
    owner: str
    creator: str
    tags: Dict[str, Optional[Any]] = None
    replies: str
    created_at: str
    updated_at: str


class PatchedPartnerStackQuestion(BaseModel):
    id: Optional[UUID] = None
    title: Optional[str] = None
    neo4j_id: Optional[str] = None
    status: Optional[str] = None
    description: Optional[str] = None
    answered_at: Optional[str] = None
    has_answer: Optional[str] = None
    owner: Optional[str] = None
    creator: Optional[str] = None
    tags: Dict[str, Optional[Any]] = None
    replies: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None


class PatchedQuestion(BaseModel):
    id: Optional[UUID] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    entity_type: Optional[str] = None
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
    status: Optional[str] = None
    priority: Optional[str] = None
    reactions: Dict[str, Optional[Any]] = None
    answer: Optional[UUID] = None
    assigned_to: Optional[UUID] = None
    votes_sum: Optional[int] = None
    current_user_vote: Optional[str] = None


class PatchedQuestionReply(BaseModel):
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
    reactions: Dict[str, Optional[Any]] = None


class Question(BaseModel):
    id: UUID
    created_at: datetime
    updated_at: datetime
    entity_type: str
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
    internal_users: Dict[str, Optional[Any]] = None
    external_users: Dict[str, Optional[Any]] = None
    external_usage: Optional[conint(ge=-2147483648, le=2147483647)] = None
    databuilder_id: Optional[str] = None
    viewers_delta: Dict[str, Optional[Any]] = None
    search_metadata: Dict[str, Optional[Any]] = None
    pristine: Optional[bool] = None
    sources: List[UUID]
    status: Optional[str] = None
    priority: Optional[str] = None
    reactions: Dict[str, Optional[Any]] = None
    answer: Optional[UUID] = None
    assigned_to: Optional[UUID] = None
    votes_sum: Optional[int] = None
    current_user_vote: str


class QuestionList(BaseModel):
    id: UUID
    created_at: datetime
    updated_at: datetime
    title: Optional[str] = None
    owners: Optional[List[UUID]] = None
    collections: Optional[List[UUID]] = None
    assigned_to: Optional[UUID] = None
    entity_type: str
    status: Optional[str] = None
    priority: Optional[str] = None
    votes_sum: Optional[int] = None
    current_user_vote: str
    children_count: str
    viewers_delta: Dict[str, Optional[Any]] = None
    pristine: Optional[bool] = None


class QuestionReply(BaseModel):
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
    reactions: Dict[str, Optional[Any]] = None


class PaginatedPartnerStackQuestionList(BaseModel):
    count: Optional[int] = Field(None, example=123)
    next: Optional[AnyUrl] = Field(
        None, example="http://api.example.org/accounts/?page=4"
    )
    previous: Optional[AnyUrl] = Field(
        None, example="http://api.example.org/accounts/?page=2"
    )
    results: Optional[List[PartnerStackQuestion]] = None


class PaginatedQuestionListList(BaseModel):
    count: Optional[int] = Field(None, example=123)
    next: Optional[AnyUrl] = Field(
        None, example="http://api.example.org/accounts/?page=4"
    )
    previous: Optional[AnyUrl] = Field(
        None, example="http://api.example.org/accounts/?page=2"
    )
    results: Optional[List[QuestionList]] = None


class PaginatedQuestionReplyList(BaseModel):
    count: Optional[int] = Field(None, example=123)
    next: Optional[AnyUrl] = Field(
        None, example="http://api.example.org/accounts/?page=4"
    )
    previous: Optional[AnyUrl] = Field(
        None, example="http://api.example.org/accounts/?page=2"
    )
    results: Optional[List[QuestionReply]] = None
