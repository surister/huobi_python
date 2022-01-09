from dataclasses import dataclass, field

from huobi.rest.enums import HttpMethod


class _DONT_SEND_IF_NONE:
    def __repr__(self):
        return 'DONT_SEND_IF_NONE'


DONT_SEND = _DONT_SEND_IF_NONE()


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
        d = {}
        for k, v in self.query_params.items():
            if v is not DONT_SEND:
                d.update({k: v})

        return d


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


@dataclass
class LatestTickersForAllPairsEndpoint(Endpoint):
    name: str = 'market/LatestTickersAllPairs'
    raw_path: str = '/market/tickers'
    method: HttpMethod = HttpMethod.GET


@dataclass
class UIDEndpoint(Endpoint):
    name: str = 'user/UID'
    raw_path: str = '/v2/user/uid'
    method: HttpMethod = HttpMethod.GET
