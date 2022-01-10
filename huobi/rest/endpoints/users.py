from dataclasses import dataclass

from huobi.rest.endpoints.endpoint import Endpoint
from huobi.rest.enums import HttpMethod


@dataclass
class UIDEndpoint(Endpoint):
    name: str = 'user/UID'
    raw_path: str = '/v2/user/uid'
    method: HttpMethod = HttpMethod.GET


@dataclass
class AggregatedBalanceEndpoint(Endpoint):
    name: str = 'subuser/AggregatedBalance'
    raw_path: str = '/v1/subuser/aggregate-balance'
    method: HttpMethod = HttpMethod.GET
