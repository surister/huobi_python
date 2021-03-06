from dataclasses import dataclass

from huobi.rest.endpoints.endpoint import DONT_SEND, Endpoint
from huobi.rest.enums import HttpMethod


@dataclass
class MarketStatusEndpoint(Endpoint):
    name: str = 'ReferenceData/SystemStatus'
    raw_path: str = '/v2/market-status'
    method: HttpMethod = HttpMethod.GET


@dataclass
class AllSupportedTradingSymbolsEndpoint(Endpoint):
    name: str = 'ReferenceData/MarketStatus'
    raw_path: str = '/v1/common/symbols'
    method: HttpMethod = HttpMethod.GET


@dataclass
class AllSupportedCurrenciesEndpoint(Endpoint):
    name: str = 'ReferenceData/AllSupportedCurrencies'
    raw_path: str = '/v1/common/currencys'
    method: HttpMethod = HttpMethod.GET


@dataclass
class CurrentTimestampEndpoint(Endpoint):
    name: str = 'ReferenceData/CurrentTimestamp'
    raw_path: str = '/v1/common/timestamp'
    method: HttpMethod = HttpMethod.GET


@dataclass
class CurrencyChainsEndpoint(Endpoint):
    name: str = 'ReferenceData/CurrentTimestamp'
    raw_path: str = '/v2/reference/currencies'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'currency': DONT_SEND,
        'authorizedUser': DONT_SEND,
    }
