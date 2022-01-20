from dataclasses import dataclass

from huobi.rest.endpoints import DONT_SEND, Endpoint
from huobi.rest.enums import HttpMethod


@dataclass
class LoanInterestRateAndQuotaIsolatedEndpoint(Endpoint):
    name: str = 'MarginLoanCI/LoanInterestRateAndQuotaIsolated'
    raw_path: str = '/v1/margin/loan-info'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'symbols': DONT_SEND,
    }


@dataclass
class SearchPastMarginOrdersIsolatedEndpoint(Endpoint):
    name: str = 'MarginLoanCI/SearchPastMarginOrders'
    raw_path: str = '/v1/margin/loan-orders'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'symbol': DONT_SEND,
        'states': DONT_SEND,
        'start-date': DONT_SEND,
        'end-date': DONT_SEND,
        'from': DONT_SEND,
        'direct': DONT_SEND,
        'size': DONT_SEND,
        'sub-uid': DONT_SEND,
    }


@dataclass
class BalanceOfTheMarginLoanAccountEndpoint(Endpoint):
    name: str = 'MarginLoanCI/BalanceOfTheMarginLoanAccount'
    raw_path: str = '/v1/cross-margin/accounts/balance'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'sub-uid': DONT_SEND,
    }


@dataclass
class BalanceOfTheMarginLoanAccountIsolatedEndpoint(Endpoint):
    name: str = 'MarginLoanCI/BalanceOfTheMarginLoanAccountIsolated'
    raw_path: str = '/v1/margin/accounts/balance'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'symbol': DONT_SEND,
        'sub-uid': DONT_SEND,
    }


@dataclass
class LoanInterestRateAndQuotaCrossEndpoint(Endpoint):
    name: str = 'MarginLoanCI/LoanInterestRateAndQuotaCross'
    raw_path: str = '/v1/cross-margin/loan-info'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'symbol': DONT_SEND,
        'sub-uid': DONT_SEND,
    }


@dataclass
class SearchPastMarginOrdersCrossEndpoint(Endpoint):
    name: str = 'MarginLoanCI/SearchPastMarginOrders'
    raw_path: str = '/v1/cross-margin/loan-orders'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'start-date': DONT_SEND,
        'end-date': DONT_SEND,
        'currency': DONT_SEND,
        'state': DONT_SEND,
        'from': DONT_SEND,
        'direct': DONT_SEND,
        'size': DONT_SEND,
        'sub-uid': DONT_SEND,
    }


@dataclass
class RepaymentRecordReferenceEndpoint(Endpoint):
    name: str = 'MarginLoanCI/RepaymentRecordReference'
    raw_path: str = '/v2/account/repayment'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'repayId': DONT_SEND,
        'accountId': DONT_SEND,
        'currency': DONT_SEND,
        'startTime': DONT_SEND,
        'endTime': DONT_SEND,
        'sort': DONT_SEND,
        'limit': DONT_SEND,
        'fromId': DONT_SEND,
    }
