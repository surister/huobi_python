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
        return self.raw_path.format(**self.path_params)


@dataclass
class AccountsEndpoint(Endpoint):
    name: str = 'Account'
    raw_path: str = '/v1/account/accounts'
    method: HttpMethod = HttpMethod.GET


@dataclass
class AccountBalanceEndpoint(Endpoint):
    name: str = 'Balance'
    raw_path: str = '/v1/account/accounts/{account_id}/balance'
    method: HttpMethod = HttpMethod.GET


@dataclass
class AssetValuation(Endpoint):
    name: str = 'Asset'
    raw_path: str = '/v2/account/asset-valuation'
    method: HttpMethod = HttpMethod.GET
