from dataclasses import dataclass

from huobi.rest.endpoints.endpoint import DONT_SEND, Endpoint
from huobi.rest.enums import HttpMethod


@dataclass
class QueryDepositAddressEndpoint(Endpoint):
    name: str = 'Wallet/QueryDepositAddress'
    raw_path: str = '/v2/account/deposit/address'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'currency': DONT_SEND,
    }


@dataclass
class QueryWithdrawQuotaEndpoint(Endpoint):
    name: str = 'Wallet/QueryWithdrawQuota'
    raw_path: str = '/v2/account/withdraw/quota'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'currency': DONT_SEND,
    }


@dataclass
class QueryWithdrawAddressEndpoint(Endpoint):
    name: str = 'Wallet/QueryWithdrawAddress'
    raw_path: str = '/v2/account/withdraw/address'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'currency': DONT_SEND,
        'chain': DONT_SEND,
        'note': DONT_SEND,
        'limit': DONT_SEND,
        'fromId': DONT_SEND,
    }


@dataclass
class QueryWithdrawalOrderByClientOrderIdEndpoint(Endpoint):
    name: str = 'Wallet/QueryWithdrawalOrderByClientOrderId'
    raw_path: str = '/v1/query/withdraw/client-order-id'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'clientOrderId': DONT_SEND,
    }


@dataclass
class SearchForExistedWithdrawsAndDepositsEndpoint(Endpoint):
    name: str = 'Wallet/SearchForExistedWithdrawsAndDeposits'
    raw_path: str = '/v1/query/deposit-withdraw'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'currency': DONT_SEND,
        'type': DONT_SEND,
        'from': DONT_SEND,
        'size': DONT_SEND,
        'direct': DONT_SEND,
    }
