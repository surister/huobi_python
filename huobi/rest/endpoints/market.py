from dataclasses import dataclass

from huobi.rest.endpoints import DONT_SEND, Endpoint
from huobi.rest.enums import HttpMethod


@dataclass
class CandlesEndpoint(Endpoint):
    name: str = 'market/Candles'
    raw_path: str = '/market/history/kline'
    method: HttpMethod = HttpMethod.GET
    query_params = {'symbol': DONT_SEND,
                    'period': DONT_SEND,
                    'size': DONT_SEND,
                    }


@dataclass
class LatestAggregatedTickerEndpoint(Endpoint):
    name: str = 'market/LatestAggregatedTicker'
    raw_path: str = '/market/detail/merged'
    method: HttpMethod = HttpMethod.GET
    query_params = {'symbol': DONT_SEND}


@dataclass
class MarketDepthEndpoint(Endpoint):
    name: str = 'market/Depth'
    raw_path: str = '/market/depth'
    method: HttpMethod = HttpMethod.GET
    query_params = {'symbol': DONT_SEND,
                    'depth': DONT_SEND,
                    'type': DONT_SEND,
                    }


@dataclass
class LastTradeEndpoint(Endpoint):
    name: str = 'market/LastTrade'
    raw_path: str = '/market/trade'
    method: HttpMethod = HttpMethod.GET
    query_params = {'symbol': DONT_SEND}


@dataclass
class MostRecentTradesEndpoint(Endpoint):
    name: str = 'market/MostRecentTrades'
    raw_path: str = '/market/history/trade'
    method: HttpMethod = HttpMethod.GET
    query_params = {'symbol': DONT_SEND,
                    'size': DONT_SEND,
                    }


@dataclass
class LastDayMarketSummaryEndpoint(Endpoint):
    name: str = 'market/LastDayMarketSummary'
    raw_path: str = '/market/detail/'
    method: HttpMethod = HttpMethod.GET
    query_params = {'symbol': DONT_SEND}


@dataclass
class RealTimeNAVEndpoint(Endpoint):
    name: str = 'market/RealTimeNAV'
    raw_path: str = '/market/etp'
    method: HttpMethod = HttpMethod.GET
    query_params = {'symbol': DONT_SEND}


@dataclass
class LatestTickersForAllPairsEndpoint(Endpoint):
    name: str = 'market/LatestTickersAllPairs'
    raw_path: str = '/market/tickers'
    method: HttpMethod = HttpMethod.GET


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
class CandlesEndpoint(Endpoint):
    name: str = 'market/Candles'
    raw_path: str = '/market/history/kline'
    method: HttpMethod = HttpMethod.GET
    query_params = {'symbol': DONT_SEND,
                    'period': DONT_SEND,
                    'size': DONT_SEND
                    }


@dataclass
class LatestAggregatedTickerEndpoint(Endpoint):
    name: str = 'market/LatestAggregatedTicker'
    raw_path: str = '/market/detail/merged'
    method: HttpMethod = HttpMethod.GET
    query_params = {'symbol': DONT_SEND}


@dataclass
class MarketDepthEndpoint(Endpoint):
    name: str = 'market/Depth'
    raw_path: str = '/market/depth'
    method: HttpMethod = HttpMethod.GET
    query_params = {'symbol': DONT_SEND,
                    'depth': DONT_SEND,
                    'type': DONT_SEND
                    }


@dataclass
class LastTradeEndpoint(Endpoint):
    name: str = 'market/LastTrade'
    raw_path: str = '/market/trade'
    method: HttpMethod = HttpMethod.GET
    query_params = {'symbol': DONT_SEND}


@dataclass
class MostRecentTradesEndpoint(Endpoint):
    name: str = 'market/MostRecentTrades'
    raw_path: str = '/market/history/trade'
    method: HttpMethod = HttpMethod.GET
    query_params = {'symbol': DONT_SEND,
                    'size': DONT_SEND
                    }
