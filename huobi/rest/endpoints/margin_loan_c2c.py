from dataclasses import dataclass

from huobi.rest.endpoints import DONT_SEND, Endpoint
from huobi.rest.enums import HttpMethod


@dataclass
class QueryLendingBorrowOffersEndpoint(Endpoint):
    name: str = 'MarginLoanC2C/QueryLendingBorrowOffer'
    raw_path: str = '/v2/c2c/offers'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'accountId': DONT_SEND,
        'currency': DONT_SEND,
        'side': DONT_SEND,
        'offerStatus': DONT_SEND,
        'startTime': DONT_SEND,
        'endTime': DONT_SEND,
        'limit': DONT_SEND,
        'fromId': DONT_SEND,
    }


@dataclass
class QueryLendingBorrowingOfferEndpoint(Endpoint):
    name: str = 'MarginLoanC2C/QueryLendingBorrowingOffer'
    raw_path: str = '/v2/c2c/offer'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'offerID': DONT_SEND,
    }


@dataclass
class QueryLendingBorrowingTransactionsEndpoint(Endpoint):
    name: str = 'MarginLoanC2C/QueryLendingBorrowingTransactions'
    raw_path: str = '/v2/c2c/transactions'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'accountId': DONT_SEND,
        'currency': DONT_SEND,
        'side': DONT_SEND,
        'transactStatus': DONT_SEND,
        'startTime': DONT_SEND,
        'endTime': DONT_SEND,
        'limit': DONT_SEND,
        'fromId': DONT_SEND,
    }


@dataclass
class QueryC2CRepaymentsEndpoint(Endpoint):
    name: str = 'MarginLoanC2C/QueryC2CRepayments'
    raw_path: str = '/v2/c2c/repayment'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'repayId': DONT_SEND,
        'accountId': DONT_SEND,
        'currency': DONT_SEND,
        'startTime': DONT_SEND,
        'endTime': DONT_SEND,
        'limit': DONT_SEND,
        'fromId': DONT_SEND,
    }


@dataclass
class QueryC2CAccountBalanceEndpoint(Endpoint):
    name: str = 'MarginLoanC2C/QueryC2CAccountBalance'
    raw_path: str = '/v2/c2c/account'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'accountId': DONT_SEND,
        'currency': DONT_SEND,
    }
