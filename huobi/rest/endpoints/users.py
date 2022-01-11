from dataclasses import dataclass

from huobi.rest.endpoints.endpoint import Endpoint, DONT_SEND
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


@dataclass
class ApiKeyQueryEndpoint(Endpoint):
    name: str = 'subuser/ApiKey'
    raw_path: str = '/v2/user/api-key'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'uid': DONT_SEND,
        'accessKey': DONT_SEND,
    }


@dataclass
class SubUserListEndpoint(Endpoint):
    name: str = 'subuser/SubUserList'
    raw_path: str = '/v2/sub-user/user-list'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'fromId': DONT_SEND,
    }


@dataclass
class SubUserStatusEndpoint(Endpoint):
    name: str = 'subuser/SubUserStatus'
    raw_path: str = '/v2/sub-user/user-state'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'subUid': DONT_SEND,
    }


@dataclass
class DepositAddressSubUserEndpoint(Endpoint):
    name: str = 'subuser/DepositAddressSubUser'
    raw_path: str = '/v2/sub-user/deposit-address'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'subUid': DONT_SEND,
        'currency': DONT_SEND,
    }


@dataclass
class DepositHistorySubUser(Endpoint):
    name: str = 'subuser/DepositHistorySubUser'
    raw_path: str = '/v2/sub-user/query-deposit'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'subUid': DONT_SEND,
        'currency': DONT_SEND,
        'startTime': DONT_SEND,
        'endTime': DONT_SEND,
        'sort': DONT_SEND,
        'limit': DONT_SEND,
        'fromId': DONT_SEND,
    }
