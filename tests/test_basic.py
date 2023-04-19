import uuid
from datetime import datetime

import pytest
import responses

from apinator_secoda import model
from apinator_secoda.api import SecodaApi, SecodaContext


@pytest.fixture
def context():
    return SecodaContext(access_token="TOKEN", api_host="example.secoda.co")


@pytest.fixture
def api(context):
    return SecodaApi(context)


@responses.activate
def test_pagination(api):
    """Tests that pagination works as expected"""
    table1 = model.table.TableList(
        id=uuid.uuid4(),
        created_at=datetime.now(),
        updated_at=datetime.now(),
        parent_id=uuid.uuid4(),
    )
    table2 = model.table.TableList(
        id=uuid.uuid4(),
        created_at=datetime.now(),
        updated_at=datetime.now(),
        parent_id=uuid.uuid4(),
    )
    table3 = model.table.TableList(
        id=uuid.uuid4(),
        created_at=datetime.now(),
        updated_at=datetime.now(),
        parent_id=uuid.uuid4(),
    )

    page1 = model.table.PaginatedTableListList(
        count=2,
        total_pages=2,
        links=model.common.PaginationLinks(
            next="https://example.secoda.co/api/v1/table/tables/?page=2"
        ),
        meta=model.common.PaginationMeta(page=1, next_page=2),
        resource_totals={},
        results=[table1, table2],
    )
    page2 = model.table.PaginatedTableListList(
        count=1,
        total_pages=2,
        links=model.common.PaginationLinks(
            previous="https://example.secoda.co/api/v1/table/tables/?page=1"
        ),
        meta=model.common.PaginationMeta(page=2, previous_page=1),
        resource_totals={},
        results=[table3],
    )

    req1: responses.BaseResponse = responses.get(
        "https://example.secoda.co/api/v1/table/tables/",
        body=page1.json(),
    )
    req2: responses.BaseResponse = responses.get(
        "https://example.secoda.co/api/v1/table/tables/?page=2",
        body=page2.json(),
    )

    all_tables = list(api.tables.iterate())
    assert all_tables == [table1, table2, table3]
    assert req1.call_count == req2.call_count == 1
