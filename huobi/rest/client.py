from typing import Union

from huobi.rest.constants import REST_API_HUOBI_URL
from huobi.rest.endpoints import (
    AccountBalanceEndpoint,
    AccountsEndpoint,
    AccountHistoryEndpoint,
    AccountLedgerEndpoint,
    AggregatedBalanceEndpoint,
    AssetValuationEndpoint,
    CandlesEndpoint,
    DONT_SEND,
    LastDayMarketSummaryEndpoint,
    LastTradeEndpoint,
    LatestAggregatedTickerEndpoint,
    LatestTickersForAllPairsEndpoint,
    MarketDepthEndpoint,
    MostRecentTradesEndpoint,
    PointBalanceEndpoint,
    UIDEndpoint,
)
from huobi.rest.request import HuobiRequest
from huobi.rest.url import Url
from huobi.rest.exceptions import CredentialKeysNotProvided


class Client:
    pass


class HuobiClient:
    def __init__(self,
                 *,
                 access_key: str,
                 secret_key: str,
                 url: Union[Url, str] = REST_API_HUOBI_URL):
        self.access_key = access_key
        self.secret_key = secret_key
        self.huobi_api_url = Url(url) if isinstance(url, str) else url

        if self.access_key is None or self.secret_key is None:
            raise CredentialKeysNotProvided('Secret key or Access key cannot be None')

    def _create_request(self, endpoint):
        req = HuobiRequest(
            url=self.huobi_api_url,
            access_key=self.access_key,
            secret_key=self.secret_key,
            endpoint=endpoint,
        )
        return req.execute()

    def get_accounts(self):
        endpoint = AccountsEndpoint()
        return self._create_request(endpoint)

    def get_balance(self, *, account_id):
        endpoint = AccountBalanceEndpoint(
            path_params={'account_id': account_id},
        )
        return self._create_request(endpoint)

    def get_asset_valuation(self, account_type=DONT_SEND):
        endpoint = AssetValuationEndpoint(
            query_params={'accountType': account_type}
        )
        return self._create_request(endpoint)

    def get_latest_tickers_for_all_pairs(self):
        endpoint = LatestTickersForAllPairsEndpoint()
        return self._create_request(endpoint)

    def get_uid(self):
        endpoint = UIDEndpoint()
        return self._create_request(endpoint)

    def get_aggregated_balance(self):
        endpoint = AggregatedBalanceEndpoint()
        return self._create_request(endpoint)

    def get_candles(self, *, symbol, period, size=DONT_SEND):
        endpoint = CandlesEndpoint(
            query_params={
                'symbol': symbol,
                'period': period,
                'size': size,
            }
        )
        return self._create_request(endpoint)

    def get_latest_aggregated_ticker(self, *, symbol):
        endpoint = LatestAggregatedTickerEndpoint(
            query_params={'symbol': symbol}
        )
        return self._create_request(endpoint)

    def get_market_depth(self, *, symbol, type_step, depth=DONT_SEND):
        endpoint = MarketDepthEndpoint(
            query_params={
                'symbol': symbol,
                'type': type_step,
                'depth': depth,
            }
        )
        return self._create_request(endpoint)

    def get_last_trade(self, *, symbol):
        endpoint = LastTradeEndpoint(
            query_params={'symbol': symbol}
        )
        return self._create_request(endpoint)

    def get_most_recent_trades(self, *, symbol, size=DONT_SEND):
        endpoint = MostRecentTradesEndpoint(
            query_params={'symbol': symbol,
                          'size': size}
        )
        return self._create_request(endpoint)

    def get_last_day_market_summary(self, *, symbol):
        endpoint = LastDayMarketSummaryEndpoint(
            query_params={'symbol': symbol}
        )
        return self._create_request(endpoint)

    def get_real_time_nav(self, *, symbol):
        endpoint = LastDayMarketSummaryEndpoint(
            query_params={'symbol': symbol}
        )
        return self._create_request(endpoint)

    def get_account_history(self, *, account_id, currency=DONT_SEND, transant_types=DONT_SEND,
                            start_time=DONT_SEND, end_time=DONT_SEND, sort=DONT_SEND,
                            size=DONT_SEND, from_id=DONT_SEND):
        endpoint = AccountHistoryEndpoint(
            query_params={'account-id': account_id,
                          'currency': currency,
                          'transact-types': transant_types,
                          'start-time': start_time,
                          'end-time': end_time,
                          'sort': sort,
                          'size': size,
                          'from-id': from_id}
        )
        return self._create_request(endpoint)

    def get_account_ledger(self, *, account_id, currency=DONT_SEND,
                           transact_types=DONT_SEND, start_time=DONT_SEND,
                           end_time=DONT_SEND, sort=DONT_SEND, size=DONT_SEND,
                           limit=DONT_SEND, from_id=DONT_SEND):
        endpoint = AccountLedgerEndpoint(
            query_params={'accountId': account_id,
                          'currency': currency,
                          'transactTypes': transact_types,
                          'startTime': start_time,
                          'endTime': end_time,
                          'sort': sort,
                          'size': size,
                          'limit': limit,
                          'fromId': from_id}
        )
        return self._create_request(endpoint)

    def get_point_balance(self, sub_uid=DONT_SEND):
        endpoint = PointBalanceEndpoint(
            query_params={'subUid': sub_uid}
        )
        return self._create_request(endpoint)
