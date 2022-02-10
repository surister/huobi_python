from dataclasses import dataclass

from huobi.rest.endpoints.endpoint import DONT_SEND, Endpoint
from huobi.rest.enums import HttpMethod


@dataclass
class ReferenceDataOfETPEndpoint(Endpoint):
    name: str = 'etp/ReferenceDataOfETP'
    raw_path: str = '/v2/etp/reference'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'etpName': DONT_SEND,
    }


@dataclass
class ETPCreationAndRedemptionHistoryEndpoint(Endpoint):
    name: str = 'etp/ETPCreationAndRedemptionHistory'
    raw_path: str = '/v2/etp/transactions'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'etpNames': DONT_SEND,
        'currencies': DONT_SEND,
        'transactTypes': DONT_SEND,
        'transactStatus': DONT_SEND,
        'startTime': DONT_SEND,
        'endTime': DONT_SEND,
        'sort': DONT_SEND,
        'limit': DONT_SEND,
        'fromId': DONT_SEND,
    }


@dataclass
class SpecificETPCreationOrRedemptionRecordEndpoint(Endpoint):
    name: str = 'etp/SpecificETPCreationOrRedemptionRecord'
    raw_path: str = '/v2/etp/transaction'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'transactId': DONT_SEND,
    }


@dataclass
class PositionRebalanceHistoryEndpoint(Endpoint):
    name: str = 'etp/PositionRebalanceHistory'
    raw_path: str = '/v2/etp/rebalance'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'symbol': DONT_SEND,
        'rebalTypes': DONT_SEND,
        'startTime': DONT_SEND,
        'endTime': DONT_SEND,
        'sort': DONT_SEND,
        'limit': DONT_SEND,
        'fromId': DONT_SEND,
    }


@dataclass
class HoldingLimitOfLeveragedETPEndpoint(Endpoint):
    name: str = 'etp/HoldingLimitOfLeveragedETP'
    raw_path: str = '/v2/etp/limit'
    method: HttpMethod = HttpMethod.GET
    query_params = {
        'currency': DONT_SEND,
    }
