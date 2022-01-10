from dataclasses import dataclass

from huobi.rest.endpoints.endpoint import Endpoint, DONT_SEND
from huobi.rest.enums import HttpMethod


@dataclass
class AccountsEndpoint(Endpoint):
    name: str = 'account/Account'
    raw_path: str = '/v1/account/accounts'
    method: HttpMethod = HttpMethod.GET


@dataclass
class AccountBalanceEndpoint(Endpoint):
    name: str = 'account/Balance'
    raw_path: str = '/v1/account/accounts/{account_id}/balance'
    method: HttpMethod = HttpMethod.GET


@dataclass
class AssetValuationEndpoint(Endpoint):
    name: str = 'account/Asset'
    raw_path: str = '/v2/account/valuation'
    method: HttpMethod = HttpMethod.GET
    query_params = {'accountType': DONT_SEND}
