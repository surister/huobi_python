from typing import Union

from huobi.rest.constants import REST_API_HUOBI_URL
from huobi.rest.endpoints import AccountsEndpoint, AccountBalanceEndpoint, AssetValuationEndpoint, DONT_SEND, \
    LatestTickersForAllPairsEndpoint, UIDEndpoint, AggregatedBalanceEndpoint, CandlesEndpoint, \
    LatestAggregatedTickerEndpoint, MarketDepthEndpoint
from huobi.rest.request import HuobiRequest
from huobi.rest.url import Url
from huobi.rest.exceptions import CredentialKeysNotProvided


class Client:
    pass


class HuobiClient:
    def __init__(self, *, access_key: str, secret_key: str, url: Union[Url, str] = REST_API_HUOBI_URL):
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
            query_params={'symbol': symbol,
                          'period': period,
                          'size': size
                          }
        )
        return self._create_request(endpoint)

    def get_latest_aggregated_ticker(self, *, symbol):
        endpoint = LatestAggregatedTickerEndpoint(
            query_params={'symbol': symbol}
        )
        return self._create_request(endpoint)

    def get_market_depth(self, *, symbol, depth=DONT_SEND, type_step):
        endpoint = MarketDepthEndpoint(
            query_params={'symbol': symbol,
                          'depth': depth,
                          'type': type_step
                          }
        )
        return self._create_request(endpoint)
