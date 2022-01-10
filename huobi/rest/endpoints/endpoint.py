from dataclasses import dataclass, field

from huobi.rest.enums import HttpMethod


@dataclass
class Endpoint:
    name: str
    raw_path: str
    method: HttpMethod
    path_params: dict = field(default_factory=dict)
    query_params: dict = field(default_factory=dict)

    @property
    def path(self):
        return self.raw_path

    @property
    def prepared_query_params(self):
        return {k: v for k, v in self.query_params.items() if v is not DONT_SEND}


class _DONT_SEND_IF_NONE:
    def __repr__(self):
        return 'DONT_SEND_IF_NONE'


DONT_SEND = _DONT_SEND_IF_NONE()
