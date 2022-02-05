from huobi.rest.endpoints.account import (
    AccountBalanceEndpoint,
    AccountsEndpoint,
    AccountHistoryEndpoint,
    AccountLedgerEndpoint,
    AssetValuationEndpoint,
    PointBalanceEndpoint,
)
from huobi.rest.endpoints.endpoint import DONT_SEND, Endpoint
from huobi.rest.endpoints.market import (
    CandlesEndpoint,
    LastDayMarketSummaryEndpoint,
    LastTradeEndpoint,
    LatestAggregatedTickerEndpoint,
    LatestTickersForAllPairsEndpoint,
    MarketDepthEndpoint,
    MostRecentTradesEndpoint,
)
from huobi.rest.endpoints.users import (
    AggregatedBalanceEndpoint,
    DepositAddressSubUserEndpoint,
    DepositHistorySubUser,
    UIDEndpoint,
    ApiKeyQueryEndpoint,
    SubUserListEndpoint,
    SubUserStatusEndpoint,
)
from huobi.rest.endpoints.reference_data import (
    AllSupportedTradingSymbolsEndpoint,
    AllSupportedCurrenciesEndpoint,
    CurrencyChainsEndpoint,
    CurrentTimestampEndpoint,
    MarketStatusEndpoint,
)
from huobi.rest.endpoints.wallet import (
    QueryDepositAddressEndpoint,
    QueryWithdrawAddressEndpoint,
    QueryWithdrawQuotaEndpoint,
    QueryWithdrawalOrderByClientOrderIdEndpoint,
    SearchForExistedWithdrawsAndDepositsEndpoint,
)
from huobi.rest.endpoints.trading import (
    AllOpenOrdersEndpoint,
    CurrentFeeRateAppliedToTheUserEndpoint,
    OrderDetailOfAClientOrderIdEndpoint,
    OrderDetailOfAnOrderEndpoint,
    SearchPastOrdersEndpoint,
    SearchMatchResultEndpoint,
    SearchHistoricalOrdersWithinTwoDaysEndpoint,
)
from huobi.rest.endpoints.conditional_orders import (
    QueryConditionalOrderHistoryEndpoint,
    QuerySpecificConditionalOrderEndpoint,
    QueryOpenConditionalOrdersBeforeTriggeringEndpoint,
)
from huobi.rest.endpoints.margin_loan_ci import (
    BalanceOfTheMarginLoanAccountEndpoint,
    BalanceOfTheMarginLoanAccountIsolatedEndpoint,
    LoanInterestRateAndQuotaIsolatedEndpoint,
    SearchPastMarginOrdersIsolatedEndpoint,
    SearchPastMarginOrdersCrossEndpoint,
    LoanInterestRateAndQuotaCrossEndpoint,
    RepaymentRecordReferenceEndpoint,
)

from huobi.rest.endpoints.stable_coin_exchange import (
    ExchangeRateEndpoint,
    ExchangeStableCoinEndpoint,
)
from huobi.rest.endpoints.margin_loan_c2c import(
    QueryLendingBorrowOffersEndpoint,
    QueryLendingBorrowingOfferEndpoint,
    QueryLendingBorrowingTransactionsEndpoint,
    QueryC2CRepaymentsEndpoint,
    QueryC2CAccountBalanceEndpoint,
)

__all__ = [
    'AccountBalanceEndpoint',
    'AccountHistoryEndpoint',
    'AccountLedgerEndpoint',
    'AccountsEndpoint',
    'AggregatedBalanceEndpoint',
    'AllSupportedCurrenciesEndpoint',
    'AllSupportedTradingSymbolsEndpoint',
    'AllOpenOrdersEndpoint',
    'ApiKeyQueryEndpoint',
    'AssetValuationEndpoint',
    'BalanceOfTheMarginLoanAccountEndpoint',
    'BalanceOfTheMarginLoanAccountIsolatedEndpoint',
    'CandlesEndpoint',
    'CurrencyChainsEndpoint',
    'CurrentTimestampEndpoint',
    'CurrentFeeRateAppliedToTheUserEndpoint',
    'DONT_SEND',
    'DepositAddressSubUserEndpoint',
    'DepositHistorySubUser',
    'Endpoint',
    'ExchangeStableCoinEndpoint',
    'ExchangeRateEndpoint',
    'LastDayMarketSummaryEndpoint',
    'LastTradeEndpoint',
    'LatestAggregatedTickerEndpoint',
    'LatestTickersForAllPairsEndpoint',
    'LoanInterestRateAndQuotaIsolatedEndpoint',
    'LoanInterestRateAndQuotaCrossEndpoint',
    'MarketDepthEndpoint',
    'MarketStatusEndpoint',
    'MostRecentTradesEndpoint',
    'PointBalanceEndpoint',
    'OrderDetailOfAClientOrderIdEndpoint',
    'OrderDetailOfAnOrderEndpoint',
    'SearchPastOrdersEndpoint',
    'SearchMatchResultEndpoint',
    'SearchHistoricalOrdersWithinTwoDaysEndpoint',
    'QueryDepositAddressEndpoint',
    'QueryWithdrawAddressEndpoint',
    'QueryWithdrawQuotaEndpoint',
    'QueryWithdrawalOrderByClientOrderIdEndpoint',
    'QueryLendingBorrowOffersEndpoint',
    'QueryC2CRepaymentsEndpoint',
    'QueryLendingBorrowingTransactionsEndpoint',
    'QueryC2CAccountBalanceEndpoint',
    'QueryOpenConditionalOrdersBeforeTriggeringEndpoint',
    'QuerySpecificConditionalOrderEndpoint',
    'QueryConditionalOrderHistoryEndpoint',
    'QueryLendingBorrowingOfferEndpoint',
    'SearchForExistedWithdrawsAndDepositsEndpoint',
    'SubUserListEndpoint',
    'SubUserStatusEndpoint',
    'SearchPastMarginOrdersIsolatedEndpoint',
    'SearchPastMarginOrdersCrossEndpoint',
    'RepaymentRecordReferenceEndpoint',
    'UIDEndpoint',
]
