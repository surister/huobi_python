from dataclasses import dataclass

from huobi.rest.endpoints import DONT_SEND, Endpoint
from huobi.rest.enums import HttpMethod


@dataclass
class AllOpenOrdersEndpoint(Endpoint):
    name: str = 'trading/AllOpenOrders'
    raw_path: str = '/v1/order/openOrders'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'account-id': DONT_SEND,
        'symbol': DONT_SEND,
        'side': DONT_SEND,
        'from': DONT_SEND,
        'direct': DONT_SEND,
        'size': DONT_SEND,
    }


@dataclass
class OrderDetailOfAnOrderEndpoint(Endpoint):
    name: str = 'trading/OrderDetailOfAnOrder'
    raw_path: str = '/v1/order/orders/{order_id}'
    method: HttpMethod = HttpMethod.GET


@dataclass
class OrderDetailOfAClientOrderIdEndpoint(Endpoint):
    name: str = 'trading/OrderDetailOfAClientOrderId'
    raw_path: str = '/v1/order/orders/getClientOrder'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'clientOrderId': DONT_SEND,
    }


@dataclass
class MatchResultOfAnOrderEndpoint(Endpoint):
    name: str = 'trading/MatchResultOfAnOrder'
    raw_path: str = '/v1/order/orders/{order_id}/matchresults'
    method: HttpMethod = HttpMethod.GET


@dataclass
class SearchPastOrdersEndpoint(Endpoint):
    name: str = 'trading/SearchPastOrders'
    raw_path: str = '/v1/order/orders'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'symbol': DONT_SEND,
        'types': DONT_SEND,
        'start-time': DONT_SEND,
        'end-time': DONT_SEND,
        'states': DONT_SEND,
        'from': DONT_SEND,
        'direct': DONT_SEND,
        'size': DONT_SEND,
    }


@dataclass
class SearchHistoricalOrdersWithinTwoDaysEndpoint(Endpoint):
    name: str = 'trading/SearchHistoricalOrdersWithinTwoDays'
    raw_path: str = '/v1/order/history'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'symbol': DONT_SEND,
        'start-time': DONT_SEND,
        'end-time': DONT_SEND,
        'direct': DONT_SEND,
        'size': DONT_SEND,
    }


@dataclass
class SearchMatchResultEndpoint(Endpoint):
    name: str = 'trading/SearchMatchResult'
    raw_path: str = '/v1/order/matchresults'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'symbol': DONT_SEND,
        'types': DONT_SEND,
        'start-time': DONT_SEND,
        'end-time': DONT_SEND,
        'from': DONT_SEND,
        'direct': DONT_SEND,
        'size': DONT_SEND,
    }


@dataclass
class CurrentFeeRateAppliedToTheUserEndpoint(Endpoint):
    name: str = 'trading/CurrentFeeRateAppliedToTheUser'
    raw_path: str = '/v2/reference/transact-fee-rate'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'symbols': DONT_SEND,
    }
