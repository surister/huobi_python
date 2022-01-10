from dataclasses import dataclass

from huobi.rest.endpoints.endpoint import DONT_SEND, Endpoint
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


@dataclass
class AccountHistoryEndpoint(Endpoint):
    name: str = 'account/AccountHistory'
    raw_path: str = '/v1/account/history'
    method: HttpMethod = HttpMethod.GET
    query_params = {'account-id': DONT_SEND,
                    'currency': DONT_SEND,
                    'transact-types': DONT_SEND,
                    'start-time': DONT_SEND,
                    'end-time': DONT_SEND,
                    'sort': DONT_SEND,
                    'size': DONT_SEND,
                    'from-id': DONT_SEND}


@dataclass
class AccountLedgerEndpoint(Endpoint):
    name: str = 'account/AccountLedger'
    raw_path: str = '/v2/account/ledger'
    method: HttpMethod = HttpMethod.GET
    query_params = {'accountId': DONT_SEND,
                    'currency': DONT_SEND,
                    'transactTypes': DONT_SEND,
                    'startTime': DONT_SEND,
                    'endTime': DONT_SEND,
                    'sort': DONT_SEND,
                    'size': DONT_SEND,
                    'limit': DONT_SEND,
                    'fromId': DONT_SEND}


@dataclass
class PointBalanceEndpoint(Endpoint):
    name: str = 'account/PointBalance'
    raw_path: str = '/v2/point/account'
    method: HttpMethod = HttpMethod.GET
    query_params = {'subUid': DONT_SEND}
