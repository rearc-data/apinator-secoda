from __future__ import annotations

from enum import Enum
from typing import Optional, List, TypeVar, Generic

from apinator.common import StrictBaseModel
from pydantic import AnyUrl


class NullEnum(Enum):
    NoneType_None = None


class EntityTypeEnum(Enum):
    table = "table"
    column = "column"
    schema = "schema"
    database = "database"
    cluster = "cluster"
    dashboard = "dashboard"
    dashboard_group = "dashboard_group"
    job = "job"
    job_group = "job_group"
    query = "query"
    test_suite = "test_suite"
    test = "test"
    test_run = "test_run"
    chart = "chart"
    dictionary_term = "dictionary_term"
    collection = "collection"
    document = "document"
    question = "question"
    question_reply = "question_reply"
    run = "run"
    event = "event"
    event_property = "event_property"
    category = "category"
    user = "user"
    user_group = "user_group"
    announcement = "announcement"
    task = "task"
    report = "report"


class PaginationLinks(StrictBaseModel):
    next: Optional[AnyUrl] = None
    previous: Optional[AnyUrl] = None


class PaginationMeta(StrictBaseModel):
    page: Optional[int]
    next_page: Optional[int]
    previous_page: Optional[int]


T = TypeVar("T")


class PaginatedBase(StrictBaseModel, Generic[T]):
    count: int
    total_pages: int
    links: PaginationLinks
    meta: PaginationMeta
    resource_totals: dict
    results: List[T]
