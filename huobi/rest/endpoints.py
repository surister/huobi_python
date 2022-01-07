from abc import ABCMeta

from huobi.rest.enums import HttpMethod


class Endpoint(metaclass=ABCMeta):
    path: str
    name: str
    method: HttpMethod


class AccountsEndpoint(Endpoint):
    path = '/v1/account/accounts'
    name = 'Accounts'
    method = HttpMethod.GET
