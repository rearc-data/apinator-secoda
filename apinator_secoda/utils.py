from typing import List, Generic, TypeVar, Type, Iterator
from urllib.parse import urlparse, parse_qs

from apinator import EndpointGroup, EndpointAction

from apinator_secoda.model.common import PaginatedBase

P = TypeVar("P", bound=PaginatedBase)


class PaginatedEndpointGroup(EndpointGroup, Generic[P]):
    def __init__(
        self, *args, list_type: Type[P], actions: List[EndpointAction], **kwargs
    ):
        actions.append(EndpointAction.list(response_model=list_type))
        super().__init__(*args, actions=actions, **kwargs)

    def iterate(self) -> Iterator[P]:
        cur_list: P = self.list()
        yield from cur_list.results

        while cur_list.links.next:
            parsed_next = urlparse(cur_list.links.next)
            query = {k: v[0] for k, v in parse_qs(parsed_next.query).items()}
            cur_list: P = self.list(query=query)
            yield from cur_list.results
