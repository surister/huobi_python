from dataclasses import dataclass

from huobi.rest.endpoints.endpoint import DONT_SEND, Endpoint
from huobi.rest.enums import HttpMethod


@dataclass
class ExchangeRateEndpoint(Endpoint):
    name: str = 'StableCoinExchange/ExchangeRate'
    raw_path: str = '/v1/stable-coin/quote'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'currency': DONT_SEND,
        'amount': DONT_SEND,
        'type': DONT_SEND,
    }


@dataclass
class ExchangeStableCoinEndpoint(Endpoint):
    name: str = 'StableCoinExchange/ExchangeRate'
    raw_path: str = '/v1/stable-coin/exchange'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'quote-id': DONT_SEND,
    }
