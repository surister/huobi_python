from typing import Union

from huobi.rest.constants import (
    REST_API_HUOBI_URL,
    REST_API_HUOBI_URL_SYSTEM_STATUS,
)
from huobi.rest.endpoints import DONT_SEND
from huobi.rest.endpoints.account import (
    AccountBalanceEndpoint,
    AccountsEndpoint,
    AccountHistoryEndpoint,
    AccountLedgerEndpoint,
    AssetValuationEndpoint,
    PointBalanceEndpoint,
)
from huobi.rest.endpoints.conditional_orders import (
    QueryConditionalOrderHistoryEndpoint,
    QuerySpecificConditionalOrderEndpoint,
    QueryOpenConditionalOrdersBeforeTriggeringEndpoint,
)
from huobi.rest.endpoints.market import (
    CandlesEndpoint,
    MarketDepthEndpoint,
    MostRecentTradesEndpoint,
    LastDayMarketSummaryEndpoint,
    LastTradeEndpoint,
    LatestAggregatedTickerEndpoint,
    LatestTickersForAllPairsEndpoint,
    RealTimeNAVEndpoint,
)
from huobi.rest.endpoints.reference_data import (
    AllSupportedTradingSymbolsEndpoint,
    AllSupportedCurrenciesEndpoint,
    CurrentTimestampEndpoint,
    CurrencyChainsEndpoint,
    MarketStatusEndpoint,
)
from huobi.rest.endpoints.trading import (
    AllOpenOrdersEndpoint,
    CurrentFeeRateAppliedToTheUserEndpoint,
    MatchResultOfAnOrderEndpoint,
    OrderDetailOfAClientOrderIdEndpoint,
    OrderDetailOfAnOrderEndpoint,
    SearchPastOrdersEndpoint,
    SearchMatchResultEndpoint,
    SearchHistoricalOrdersWithinTwoDaysEndpoint,
)
from huobi.rest.endpoints.users import (
    ApiKeyQueryEndpoint,
    AggregatedBalanceEndpoint,
    UIDEndpoint,
    SubUserListEndpoint,
    SubUserStatusEndpoint,
    DepositAddressSubUserEndpoint,
    DepositHistorySubUser,
    CreateSubUserEndpoint,
    LockUnlockSubUserEndpoint,
    SetTradableMarketForSubUsersEndpoint,
    SetAssetTransferPermissionForSubUsersEndpoint,
    SetADeductionForParentAndSubUserEndpoint,
    SubUserAPIKeyCreationEndpoint,
    SubUserAPIKeyModificationEndpoint,
    SubUserAPIKeyDeletionEndpoint,
    TransferAssetBetweenParentAndSubAccountEndpoint,
)
from huobi.rest.endpoints.wallet import (
    QueryDepositAddressEndpoint,
    QueryWithdrawalOrderByClientOrderIdEndpoint,
    QueryWithdrawQuotaEndpoint,
    QueryWithdrawAddressEndpoint,
    SearchForExistedWithdrawsAndDepositsEndpoint,
)
from huobi.rest.endpoints.margin_loan_ci import (
    LoanInterestRateAndQuotaIsolatedEndpoint,
    SearchPastMarginOrdersIsolatedEndpoint,
    SearchPastMarginOrdersCrossEndpoint,
    BalanceOfTheMarginLoanAccountEndpoint,
    BalanceOfTheMarginLoanAccountIsolatedEndpoint,
    LoanInterestRateAndQuotaCrossEndpoint,
    RepaymentRecordReferenceEndpoint,
)

from huobi.rest.endpoints.stable_coin_exchange import (
    ExchangeRateEndpoint,
    ExchangeStableCoinEndpoint,
)
from huobi.rest.endpoints.margin_loan_c2c import (
    QueryLendingBorrowOffersEndpoint,
    QueryLendingBorrowingOfferEndpoint,
    QueryLendingBorrowingTransactionsEndpoint,
    QueryC2CRepaymentsEndpoint,
    QueryC2CAccountBalanceEndpoint,
)
from huobi.rest.endpoints.etp import (
    ReferenceDataOfETPEndpoint,
    ETPCreationAndRedemptionHistoryEndpoint,
    SpecificETPCreationOrRedemptionRecordEndpoint,
    PositionRebalanceHistoryEndpoint,
    HoldingLimitOfLeveragedETPEndpoint,
)
from huobi.rest.exceptions import CredentialKeysNotProvided
from huobi.rest.request import HuobiRequest
from huobi.rest.url import Url


class Client:
    def _create_request(self, endpoint, url=None, json=None):
        if url:
            url = Url(url=url)

        req = HuobiRequest(
            url=url or self.huobi_api_url,
            access_key=self.access_key,
            secret_key=self.secret_key,
            endpoint=endpoint,
            json=json
        )
        return req.execute()


class HuobiClient(Client):
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

    def get_accounts(self):
        endpoint = AccountsEndpoint()
        return self._create_request(endpoint)

    def get_balance(self, *, account_id):
        endpoint = AccountBalanceEndpoint(
            path_params={
                'account_id': account_id,
            }
        )
        return self._create_request(endpoint)

    def get_asset_valuation(self, account_type=DONT_SEND):
        endpoint = AssetValuationEndpoint(
            query_params={
                'accountType': account_type,
            }
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

    def get_candles(self, *, currency, period, size=DONT_SEND):
        endpoint = CandlesEndpoint(
            query_params={
                'symbol': currency,
                'period': period,
                'size': size,
            }
        )
        return self._create_request(endpoint)

    def get_latest_aggregated_ticker(self, *, currency):
        endpoint = LatestAggregatedTickerEndpoint(
            query_params={
                'symbol': currency,
            }
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

    def get_last_trade(self, *, currency):
        endpoint = LastTradeEndpoint(
            query_params={
                'symbol': currency,
            }
        )
        return self._create_request(endpoint)

    def get_most_recent_trades(self, *, currency, size=DONT_SEND):
        endpoint = MostRecentTradesEndpoint(
            query_params={
                'symbol': currency,
                'size': size,
            }
        )
        return self._create_request(endpoint)

    def get_last_day_market_summary(self, *, currency):
        endpoint = LastDayMarketSummaryEndpoint(
            query_params={
                'symbol': currency,
            }
        )
        return self._create_request(endpoint)

    def get_real_time_nav(self, *, currency):
        endpoint = RealTimeNAVEndpoint(
            query_params={
                'symbol': currency,
            }
        )
        return self._create_request(endpoint)

    def get_account_history(self, *,
                            account_id,
                            currency=DONT_SEND,
                            transact_types=DONT_SEND,
                            start_time=DONT_SEND,
                            end_time=DONT_SEND,
                            sort=DONT_SEND,
                            size=DONT_SEND,
                            from_id=DONT_SEND):
        endpoint = AccountHistoryEndpoint(
            query_params={
                'account-id': account_id,
                'currency': currency,
                'transact-types': transact_types,
                'start-time': start_time,
                'end-time': end_time,
                'sort': sort,
                'size': size,
                'from-id': from_id,
            }
        )
        return self._create_request(endpoint)

    def get_account_ledger(self,
                           *,
                           account_id,
                           currency=DONT_SEND,
                           transact_types=DONT_SEND,
                           start_time=DONT_SEND,
                           end_time=DONT_SEND,
                           sort=DONT_SEND,
                           size=DONT_SEND,
                           limit=DONT_SEND,
                           from_id=DONT_SEND):
        endpoint = AccountLedgerEndpoint(
            query_params={
                'accountId': account_id,
                'currency': currency,
                'transactTypes': transact_types,
                'startTime': start_time,
                'endTime': end_time,
                'sort': sort,
                'size': size,
                'limit': limit,
                'fromId': from_id,
            }
        )
        return self._create_request(endpoint)

    def get_point_balance(self, sub_uid=DONT_SEND):
        endpoint = PointBalanceEndpoint(
            query_params={'subUid': sub_uid}
        )
        return self._create_request(endpoint)

    def get_api_key(self, *, uid, access_key=DONT_SEND):
        endpoint = ApiKeyQueryEndpoint(
            query_params={
                'uid': uid,
                'accessKey': access_key,
            }
        )
        return self._create_request(endpoint)

    def get_sub_user_list(self, *, from_id=DONT_SEND):
        endpoint = SubUserListEndpoint(
            query_params={
                'fromId': from_id,
            }
        )
        return self._create_request(endpoint)

    def get_sub_user_status(self, *, sub_uid):
        endpoint = SubUserStatusEndpoint(
            query_params={
                'subUid': sub_uid,
            }
        )
        return self._create_request(endpoint)

    def get_deposit_address_sub_user(self, *, sub_uid, currency):
        endpoint = DepositAddressSubUserEndpoint(
            query_params={
                'subUid': sub_uid,
                'currency': currency,
            }
        )
        return self._create_request(endpoint)

    def get_deposit_history_sub_user(self,
                                     *,
                                     sub_uid,
                                     currency=DONT_SEND,
                                     start_time=DONT_SEND,
                                     end_time=DONT_SEND,
                                     sort=DONT_SEND,
                                     limit=DONT_SEND,
                                     from_id=DONT_SEND):
        endpoint = DepositHistorySubUser(
            query_params={
                'subUid': sub_uid,
                'currency': currency,
                'startTime': start_time,
                'endTime': end_time,
                'sort': sort,
                'limit': limit,
                'fromId': from_id,
            }
        )
        return self._create_request(endpoint)

    def get_all_supported_trading_symbols(self):
        endpoint = AllSupportedTradingSymbolsEndpoint()
        return self._create_request(endpoint)

    def get_all_supported_currencies(self):
        endpoint = AllSupportedCurrenciesEndpoint()
        return self._create_request(endpoint)

    # TODO maybe it need a refactor
    def get_currency_chains(self, currency=DONT_SEND, authorized_user=DONT_SEND):
        endpoint = CurrencyChainsEndpoint(
            query_params={
                'currency': currency,
                'authorizedUser': authorized_user,
            }
        )
        return self._create_request(endpoint)

    def get_system_timestamp(self):
        endpoint = CurrentTimestampEndpoint()
        return self._create_request(endpoint)

    def get_market_status(self):
        endpoint = MarketStatusEndpoint()
        return self._create_request(endpoint)

    def get_system_status(self):
        endpoint = ...  # FIXME
        return self._create_request(endpoint=..., url=REST_API_HUOBI_URL_SYSTEM_STATUS)

    def get_query_deposit_address(self, *, currency):
        endpoint = QueryDepositAddressEndpoint(
            query_params={
                'currency': currency,
            }
        )
        return self._create_request(endpoint)

    def get_query_withdraw_quota(self, *, currency):
        endpoint = QueryWithdrawQuotaEndpoint(
            query_params={
                'currency': currency,
            }
        )
        return self._create_request(endpoint)

    def get_query_withdraw_address(self, *, currency, chain=DONT_SEND, note=DONT_SEND,
                                   limit=DONT_SEND, from_id=DONT_SEND):
        endpoint = QueryWithdrawAddressEndpoint(
            query_params={
                'currency': currency,
                'chain': chain,
                'note': note,
                'limit': limit,
                'fromId': from_id,
            }
        )
        return self._create_request(endpoint)

    def get_query_withdrawal_order_by_client_order_id(self, *, client_order_id):
        endpoint = QueryWithdrawalOrderByClientOrderIdEndpoint(
            query_params={
                'clientOrderId': client_order_id,
            }
        )
        return self._create_request(endpoint)

    def get_search_for_existed_withdraws_and_deposits(self, *, currency=DONT_SEND, transfer_type,
                                                      from_id=DONT_SEND, size=DONT_SEND,
                                                      direct=DONT_SEND):
        endpoint = SearchForExistedWithdrawsAndDepositsEndpoint(
            query_params={
                'currency': currency,
                'type': transfer_type,
                'from': from_id,
                'size': size,
                'direct': direct,
            }
        )
        return self._create_request(endpoint)

    def get_all_open_borders(self, account_id=DONT_SEND, currency=DONT_SEND, side=DONT_SEND,
                             from_id=DONT_SEND, direct=DONT_SEND, size=DONT_SEND):
        endpoint = AllOpenOrdersEndpoint(
            query_params={
                'account-id': account_id,
                'symbol': currency,
                'side': side,
                'from': from_id,
                'direct': direct,
                'size': size,
            }
        )
        return self._create_request(endpoint)

    def get_current_fee_rate_applied_to_the_user(self, *, currencies):
        endpoint = CurrentFeeRateAppliedToTheUserEndpoint(
            query_params={
                'symbols': currencies,
            }
        )
        return self._create_request(endpoint)

    def get_order_detail_of_an_order(self, *, order_id):
        endpoint = OrderDetailOfAnOrderEndpoint(
            path_params={
                'order_id': order_id,
            }
        )
        return self._create_request(endpoint)

    def get_order_detail_of_a_client_oder_id(self, *, client_order_id):
        endpoint = OrderDetailOfAClientOrderIdEndpoint(
            query_params={
                'clientOrderId': client_order_id,
            }
        )
        return self._create_request(endpoint)

    def get_match_result_of_an_order(self, *, order_id):
        endpoint = MatchResultOfAnOrderEndpoint(
            path_params={
                'order_id': order_id,
            }
        )
        return self._create_request(endpoint)

    def get_search_past_orders(self, *, currency, types=DONT_SEND,
                               start_time=DONT_SEND, end_time=DONT_SEND,
                               states, from_id=DONT_SEND, direct=DONT_SEND,
                               size=DONT_SEND):
        endpoint = SearchPastOrdersEndpoint(
            query_params={
                'symbol': currency,
                'types': types,
                'start-time': start_time,
                'end-time': end_time,
                'states': states,
                'from': from_id,
                'direct': direct,
                'size': size,
            }
        )
        return self._create_request(endpoint)

    def get_search_historical_order_within_two_days(self, *, currency=DONT_SEND, start_time=DONT_SEND,
                                                    end_time=DONT_SEND, direct=DONT_SEND, size=DONT_SEND):
        endpoint = SearchHistoricalOrdersWithinTwoDaysEndpoint(
            query_params={
                'symbol': currency,
                'start-time': start_time,
                'end-time': end_time,
                'direct': direct,
                'size': size,
            }
        )
        return self._create_request(endpoint)

    def get_search_match_result(self, *, currency, types=DONT_SEND, start_time=DONT_SEND,
                                end_time=DONT_SEND, from_id=DONT_SEND, direct=DONT_SEND,
                                size=DONT_SEND):
        endpoint = SearchMatchResultEndpoint(
            query_params={
                'symbol': currency,
                'types': types,
                'start-time': start_time,
                'end-time': end_time,
                'from': from_id,
                'direct': direct,
                'size': size,
            }
        )
        return self._create_request(endpoint)

    def get_query_conditional_order_history(self, *, account_id=DONT_SEND, currency, order_side=DONT_SEND,
                                            order_type=DONT_SEND, order_status, start_time=DONT_SEND,
                                            end_time=DONT_SEND, sort=DONT_SEND, limit=DONT_SEND,
                                            from_id=DONT_SEND):
        endpoint = QueryConditionalOrderHistoryEndpoint(
            query_params={
                'accountId': account_id,
                'symbol': currency,
                'orderSide': order_side,
                'orderType': order_type,
                'orderStatus': order_status,
                'startTime': start_time,
                'endTime': end_time,
                'sort': sort,
                'limit': limit,
                'fromId': from_id,
            }
        )
        return self._create_request(endpoint)

    def get_query_specific_conditional_order(self, *, client_order_id):
        endpoint = QuerySpecificConditionalOrderEndpoint(
            query_params={
                'clientOrderId': client_order_id,
            }
        )
        return self._create_request(endpoint)

    def get_query_open_conditional_orders_before_triggering(self, account_id=DONT_SEND, currency=DONT_SEND,
                                                            order_side=DONT_SEND, order_type=DONT_SEND,
                                                            sort=DONT_SEND, limit=DONT_SEND, from_id=DONT_SEND):
        endpoint = QueryOpenConditionalOrdersBeforeTriggeringEndpoint(
            query_params={
                'accountId': account_id,
                'symbol': currency,
                'orderSide': order_side,
                'orderType': order_type,
                'sort': sort,
                'limit': limit,
                'fromId': from_id,
            }
        )
        return self._create_request(endpoint)

    def get_loan_interest_rate_and_quota_isolated(self, currencies=DONT_SEND):
        endpoint = LoanInterestRateAndQuotaIsolatedEndpoint(
            query_params={
                'symbols': currencies,
            }
        )
        return self._create_request(endpoint)

    def get_search_past_margin_order_isolated(self, *, currency, states=DONT_SEND, start_date=DONT_SEND,
                                              end_date=DONT_SEND, from_id=DONT_SEND, direct=DONT_SEND,
                                              size=DONT_SEND, sub_uid=DONT_SEND):
        endpoint = SearchPastMarginOrdersIsolatedEndpoint(
            query_params={
                'symbol': currency,
                'states': states,
                'start-date': start_date,
                'end-date': end_date,
                'from': from_id,
                'direct': direct,
                'size': size,
                'sub-uid': sub_uid,
            }
        )
        return self._create_request(endpoint)

    def get_balance_of_the_margin_loan_account(self, sub_uid=DONT_SEND):
        endpoint = BalanceOfTheMarginLoanAccountEndpoint(
            query_params={
                'sub-uid': sub_uid,
            }
        )
        return self._create_request(endpoint)

    def get_balance_of_the_margin_loan_account_isolated(self, currency=DONT_SEND, sub_uid=DONT_SEND):
        endpoint = BalanceOfTheMarginLoanAccountIsolatedEndpoint(
            query_params={
                'currency': currency,
                'sub-uid': sub_uid,
            }
        )
        return self._create_request(endpoint)

    def get_loan_interest_rate_and_quota_cross(self):
        endpoint = LoanInterestRateAndQuotaCrossEndpoint()
        return self._create_request(endpoint)

    def get_search_past_margin_order_cross(self, *, currency=DONT_SEND, state=DONT_SEND,
                                           start_date=DONT_SEND, end_date=DONT_SEND,
                                           from_id=DONT_SEND, direct=DONT_SEND,
                                           size=DONT_SEND, sub_uid=DONT_SEND):
        endpoint = SearchPastMarginOrdersCrossEndpoint(
            query_params={
                'start-date	': start_date,
                'end-date	': end_date,
                'currency': currency,
                'state': state,
                'from': from_id,
                'direct': direct,
                'size': size,
                'sub-uid': sub_uid,
            }
        )
        return self._create_request(endpoint)

    def get_repayment_record_reference(self, repay_id=DONT_SEND, account_id=DONT_SEND,
                                       currency=DONT_SEND, start_time=DONT_SEND,
                                       end_time=DONT_SEND, sort=DONT_SEND,
                                       limit=DONT_SEND, from_id=DONT_SEND):
        endpoint = RepaymentRecordReferenceEndpoint(
            query_params={
                'repayId': repay_id,
                'accountId': account_id,
                'currency': currency,
                'startTime': start_time,
                'endTime': end_time,
                'sort': sort,
                'limit': limit,
                'fromId': from_id,
            }
        )
        return self._create_request(endpoint)

    def get_exchange_rate(self, *, currency, amount, type_exchange):
        endpoint = ExchangeRateEndpoint(
            query_params={
                'currency': currency,
                'amount': amount,
                'type': type_exchange,
            }
        )
        return self._create_request(endpoint)

    def get_query_lending_borrow_offers(self, *, account_id=DONT_SEND, currency=DONT_SEND,
                                        side=DONT_SEND, offer_status,
                                        start_time=DONT_SEND, end_time=DONT_SEND,
                                        limit=DONT_SEND, from_id=DONT_SEND):
        endpoint = QueryLendingBorrowOffersEndpoint(
            query_params={
                'accountId': account_id,
                'currency': currency,
                'side': side,
                'offerStatus': offer_status,
                'startTime': start_time,
                'endTime': end_time,
                'limit': limit,
                'fromId': from_id,
            }
        )
        return self._create_request(endpoint)

    def get_exchange_stable_coin(self, *, quote_id):
        endpoint = ExchangeStableCoinEndpoint(
            query_params={
                'quote-id': quote_id,
            }
        )
        return self._create_request(endpoint)

    def get_query_lending_borrowing_offer(self, *, offer_id):
        endpoint = QueryLendingBorrowingOfferEndpoint(
            query_params={
                'offerId': offer_id,
            }
        )
        return self._create_request(endpoint)

    def get_query_lending_borrowing_transactions(self, *, account_id=DONT_SEND, currency=DONT_SEND,
                                                 side=DONT_SEND, transact_status,
                                                 start_time=DONT_SEND, end_time=DONT_SEND,
                                                 limit=DONT_SEND, from_id=DONT_SEND):
        endpoint = QueryLendingBorrowingTransactionsEndpoint(
            query_params={
                'accountId': account_id,
                'currency': currency,
                'side': side,
                'transactStatus': transact_status,
                'startTime': start_time,
                'endTime': end_time,
                'limit': limit,
                'fromId': from_id,
            }
        )
        return self._create_request(endpoint)

    def get_query_c2c_repayments(self, repay_id=DONT_SEND, account_id=DONT_SEND,
                                 currency=DONT_SEND,
                                 start_time=DONT_SEND, end_time=DONT_SEND,
                                 limit=DONT_SEND, from_id=DONT_SEND):
        endpoint = QueryC2CRepaymentsEndpoint(
            query_params={
                'repayId': repay_id,
                'accountId': account_id,
                'currency': currency,
                'startTime': start_time,
                'endTime': end_time,
                'limit': limit,
                'fromId': from_id,
            }
        )
        return self._create_request(endpoint)

    def get_query_c2c_account_balance(self, *, account_id, currency=DONT_SEND):
        endpoint = QueryC2CAccountBalanceEndpoint(
            query_params={
                'accountId': account_id,
                'currency': currency,
            }
        )
        return self._create_request(endpoint)

    def post_create_sub_user(self, *, payload: dict):
        endpoint = CreateSubUserEndpoint()
        return self._create_request(endpoint, json=payload)

    def post_lock_unlock_sub_user(self, *, sub_uid, action):
        endpoint = LockUnlockSubUserEndpoint()
        json = {
            'subUid': sub_uid,
            'action': action,
        }
        return self._create_request(endpoint, json=json)

    def post_set_tradable_market_for_sub_user(self, *, payload: dict):  # ERROR 500, NOT OUR FAULT
        endpoint = SetTradableMarketForSubUsersEndpoint()
        return self._create_request(endpoint, json=payload)

    def post_set_asset_transfer_permissions_for_sub_user(self, *, payload: dict):  # ERROR 500
        endpoint = SetAssetTransferPermissionForSubUsersEndpoint()
        return self._create_request(endpoint, json=payload)

    def post_sub_user_api_key_creation(self, *, otp_token, sub_uid, note, permission,
                                       ip_addresses=''):
        endpoint = SubUserAPIKeyCreationEndpoint()
        payload = {
            'otpToken': otp_token,
            'subUid': sub_uid,
            'note': note,
            'permission': permission,   # Maybe need a enum
            'ipAddresses': ip_addresses
        }
        return self._create_request(endpoint, json=payload)

    def post_transfer_asset_between_parent_and_sub_account(self, *, sub_uid, currency, amount, type_transfer):
        endpoint = TransferAssetBetweenParentAndSubAccountEndpoint()
        payload = {
            'sub-uid': sub_uid,
            'currency': currency,
            'amount': amount,
            'type': type_transfer,  # Maybe need a enum
        }
        return self._create_request(endpoint, json=payload)

    def post_sub_user_api_key_modification(self, *, sub_uid, access_key, permission=None, note=None, ip_addresses=None):
        endpoint = SubUserAPIKeyModificationEndpoint()
        payload = {
            'subUid': sub_uid,
            'accessKey': access_key,
            'note': note,
            'permission': permission,  # Should be write without space Maybe need a enum
            'ipAddresses': ip_addresses
        }
        return self._create_request(endpoint, json=payload)

    def post_set_a_deduction_for_parent_and_sub_user(self, *, payload: dict):   # Error 500
        endpoint = SetADeductionForParentAndSubUserEndpoint()
        return self._create_request(endpoint, json=payload)

    def post_sub_user_api_key_deletion(self, *, sub_uid, access_key):
        endpoint = SubUserAPIKeyDeletionEndpoint()
        payload = {
            'subUid': sub_uid,
            'accessKey': access_key,
        }
        return self._create_request(endpoint, json=payload)

    def get_reference_data_of_etp(self, *, etp_name):
        endpoint = ReferenceDataOfETPEndpoint(
            query_params={
                'etpName': etp_name,
            }
        )
        return self._create_request(endpoint)

    def get_etp_creation_and_redemption_history(self, *, etp_names, currencies=DONT_SEND,
                                                transact_id=DONT_SEND, transact_status=DONT_SEND,
                                                start_time=DONT_SEND, end_time=DONT_SEND,
                                                sort=DONT_SEND, limit=DONT_SEND, from_id=DONT_SEND):
        endpoint = ETPCreationAndRedemptionHistoryEndpoint(
            query_params={
                'etpNames': etp_names,
                'currencies': currencies,
                'transactTypes': transact_id,
                'transactStatus': transact_status,
                'startTime': start_time,
                'endTime': end_time,
                'sort': sort,
                'limit': limit,
                'fromId': from_id,
            }
        )
        return self._create_request(endpoint)

    def get_specific_etp_creation_or_redemption_record(self, *, transact_id):
        endpoint = SpecificETPCreationOrRedemptionRecordEndpoint(
            query_params={
                'transactId': transact_id,
            }
        )
        return self._create_request(endpoint)

    def get_position_rebalance_history(self, *, symbol, rebal_types=DONT_SEND, start_time=DONT_SEND,
                                       end_time=DONT_SEND, sort=DONT_SEND, limit=DONT_SEND,
                                       from_id=DONT_SEND):
        endpoint = PositionRebalanceHistoryEndpoint(
            query_params={
                'symbol': symbol,
                'rebalTypes': rebal_types,
                'startTime': start_time,
                'endTime': end_time,
                'sort': sort,
                'limit': limit,
                'fromId': from_id,
            }
        )
        return self._create_request(endpoint)

    def get_holding_limit_of_leveraged_etp(self, *, currency):
        endpoint = HoldingLimitOfLeveragedETPEndpoint(
            query_params={
                'currency': currency,
            }
        )
        return self._create_request(endpoint)
