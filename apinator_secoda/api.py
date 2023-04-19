import logging
from collections.abc import Iterable
from urllib.parse import urlparse

from apinator import JsonApiBase, EndpointGroup, EndpointAction
from pydantic import BaseModel

from . import model
from .utils import PaginatedEndpointGroup

log = logging.getLogger(__name__)


class SecodaContext(BaseModel):
    access_token: str
    api_host: str
    api_version: str = "v1"


class SecodaApi(JsonApiBase):
    def __init__(self, context: SecodaContext):
        self._access_token = context.access_token
        super().__init__(
            scheme="https",
            host=context.api_host,
            path_prefix=f"/api/{context.api_version}/",
            append_trailing_slash=True,
        )

    def get_headers(self):
        return {"Authorization": f"Bearer {self._access_token}"}

    collections = PaginatedEndpointGroup(
        url="collection/collections/",
        list_type=model.collection.PaginatedCollectionList,
        actions=[
            EndpointAction.retrieve(model.collection.Collection),
            EndpointAction.create(model.collection.Collection),
            EndpointAction.update(model.collection.Collection),
            EndpointAction.partial_update(model.collection.Collection),
            EndpointAction.destroy(),
            EndpointAction.head(),
        ],
    )

    tables = PaginatedEndpointGroup(
        url="table/tables/",
        list_type=model.table.PaginatedTableListList,
        actions=[
            EndpointAction.retrieve(model.table.Table),
            EndpointAction.create(model.table.Table),
            EndpointAction.update(model.table.Table),
            EndpointAction.partial_update(model.table.Table),
            EndpointAction.destroy(),
            EndpointAction.head(),
        ],
    )
