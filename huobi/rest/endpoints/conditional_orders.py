from dataclasses import dataclass

from huobi.rest.endpoints import DONT_SEND, Endpoint
from huobi.rest.enums import HttpMethod


@dataclass
class QueryOpenConditionalOrdersBeforeTriggeringEndpoint(Endpoint):
    name: str = 'ConditionalOrders/QueryOpenConditionalOrdersBeforeTriggering'
    raw_path: str = '/v2/algo-orders/opening'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'accountId': DONT_SEND,
        'symbol': DONT_SEND,
        'orderSide': DONT_SEND,
        'orderType': DONT_SEND,
        'sort': DONT_SEND,
        'limit': DONT_SEND,
        'fromId': DONT_SEND,
    }


@dataclass
class QueryConditionalOrderHistoryEndpoint(Endpoint):
    name: str = 'ConditionalOrders/QueryConditionalOrderHistory'
    raw_path: str = '/v2/algo-orders/history'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'accountId': DONT_SEND,
        'symbol': DONT_SEND,
        'orderSide': DONT_SEND,
        'orderType': DONT_SEND,
        'orderStatus': DONT_SEND,
        'startTime': DONT_SEND,
        'endTime': DONT_SEND,
        'sort': DONT_SEND,
        'limit': DONT_SEND,
        'fromId': DONT_SEND,
    }


@dataclass
class QuerySpecificConditionalOrderEndpoint(Endpoint):
    name: str = 'ConditionalOrders/QuerySpecificConditionalOrder'
    raw_path: str = '/v2/algo-orders/specific'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'clientOrderId': DONT_SEND,
    }
