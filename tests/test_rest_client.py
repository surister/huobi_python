import os
import time
from unittest import TestCase

from huobi.rest.client import HuobiClient


# TODO Finish tests


class TestRestHuobiClient(TestCase):
    def setUp(self) -> None:
        self.client = HuobiClient(access_key=os.getenv('TEST_ACCESS_KEY'), secret_key=os.getenv('TEST_SECRET_KEY'))

    def tearDown(self) -> None:
        # We add 1 second between tests to not reach API limits
        time.sleep(1)

    def assertHttpCodeIs200(self, request):
        self.assertEqual(request.status_code, 200)

    def test_get_accounts(self):
        request = self.client.get_accounts()
        self.assertHttpCodeIs200(request)

        self.account_code = request.json()['']  # Todo Get account

    def test_get_balance(self):
        request = self.client.get_balance(self.account_code)

        self.assertHttpCodeIs200(request)

    def test_get_asset_valuation(self):
        self.fail()

    def test_get_latest_tickers_for_all_pairs(self):
        self.fail()

    def test_get_uid(self):
        self.fail()

    def test_get_aggregated_balance(self):
        self.fail()

    def test_get_candles(self):
        self.fail()

    def test_get_latest_aggregated_ticker(self):
        self.fail()

    def test_get_market_depth(self):
        self.fail()

    def test_get_last_trade(self):
        self.fail()

    def test_get_most_recent_trades(self):
        self.fail()

    def test_get_last_day_market_summary(self):
        self.fail()

    def test_get_real_time_nav(self):
        self.fail()

    def test_get_account_history(self):
        self.fail()

    def test_get_account_ledger(self):
        self.fail()

    def test_get_point_balance(self):
        self.fail()

    def test_get_api_key(self):
        self.fail()

    def test_get_sub_user_list(self):
        self.fail()

    def test_get_sub_user_status(self):
        self.fail()

    def test_get_deposit_address_sub_user(self):
        self.fail()

    def test_get_deposit_history_sub_user(self):
        self.fail()
