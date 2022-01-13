from dataclasses import dataclass

from huobi.rest.endpoints.endpoint import DONT_SEND, Endpoint
from huobi.rest.enums import HttpMethod


@dataclass
class SystemStatusEndpoint(Endpoint):
    name: str = 'RData/SystemStatus'
    raw_path: str = 'https://status.huobigroup.com/api/v2/summary.json'
    method: HttpMethod = HttpMethod.GET


@dataclass
class MarketStatusEndpoint(Endpoint):
    name: str = 'RData/SystemStatus'
    raw_path: str = '/v2/market-status'
    method: HttpMethod = HttpMethod.GET


@dataclass
class AllSupportedTradingSymbolsEndpoint(Endpoint):
    name: str = 'RData/MarketStatus'
    raw_path: str = '/v1/common/symbols'
    method: HttpMethod = HttpMethod.GET


@dataclass
class AllSupportedCurrenciesEndpoint(Endpoint):
    name: str = 'RData/AllSuportedCurrencies'
    raw_path: str = '/v1/common/currencys'
    method: HttpMethod = HttpMethod.GET


@dataclass
class CurrentTimestampEndpoint(Endpoint):
    name: str = 'RData/CurrentTimestamp'
    raw_path: str = '/v1/common/timestamp'
    method: HttpMethod = HttpMethod.GET


@dataclass
class CurrencyChainsEndpoint(Endpoint):
    name: str = 'RData/CurrentTimestamp'
    raw_path: str = '/v2/reference/currencies'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'currency': DONT_SEND,
        'authorizedUser': DONT_SEND,
    }
