

### Features:
  - [ ] Fully Support the Rest Api
    - [ ] Common API Category
    - [x] Market Data API Category
    - [ ] Account API Category
    - [ ] Order API Category
    - [ ] Margin API Category
    - [ ] Cross Margin API Category
    - [x] Basic project structure
    - [x] API authentication
    - [x] Test first working endpoint
    - [ ] Test all marketplace data endpoints
  - [ ] Fully Support the WSS Api

#### Reference Data Features
- [x] All Supported Trading Symbols
- [x] All Supported Currencies
- [x] Current Timestamp
- [x] System Status
- [x] Currency & Chains
- [x] Market Status

#### Market Data API Category
- [x] Klines
- [x] Latest Aggregated Ticker
- [x] Latest Tickers for All Pairs
- [x] Market Depth
- [x] Last Trade
- [x] Most Recent Trades
- [x] Last 24h Market Summary
- [x] Real time NAV

#### Account API Category
- [x] All Accounts of the Current User
- [x] Account Balance of a Specific Account
- [ ] Total Valuation of Platform Assets
- [x] Asset Valuation
- [ ] Asset Transfer
- [x] Account History
- [x] Account Ledger
- [ ] Transfer Fund Between Spot Account and Future Contract Account
- [x] Point Balance
- [ ] Point Transfer

#### Wallet
- [x] Query Deposit Address
- [x] Query Withdraw Quota
- [x] Query Withdraw Address
- [ ] Create a Withdraw Request
- [x] Query withdrawal order by client order id
- [ ] Cancel a Withdraw Request
- [x] Search for Existed Withdraws and Deposits

#### Sub user Management
- [ ] Set a deduction for parent and sub user
- [x] API key query
- [x] Get UID
- [ ] Sub user creation
- [x] Get Sub User's List
- [ ] Lock/Unlock Sub User
- [x] Get Sub User's Status
- [ ] Set Tradable Market for Sub Users
- [ ] Set Asset Transfer Permission for Sub Users
- [x] Get Sub User's Account List
- [ ] Sub user API key creation
- [ ] Sub user API key modification
- [ ] Sub user API key deletion
- [ ] Transfer Asset between Parent and Sub Account
- [x] Query Deposit Address of Sub User
- [x] Query Deposit History of Sub User
- [x] Get the Aggregated Balance of all Sub-users
- [x] Get Account Balance of a Sub-User

#### Trading
- [ ] Place a New Order
- [ ] Place a Batch of Orders
- [ ] Submit Cancel for an Order
- [ ] Submit Cancel for an Order (based on client order ID)
- [x] Get All Open Orders
- [ ] Submit Cancel for Multiple Orders by Criteria
- [ ] Submit Cancel for Multiple Orders by IDs
- [ ] Dead man’s switch
- [x] Get the Order Detail of an Order
- [x] Get the Order Detail of an Order (based on client order ID)
- [x] Get the Match Result of an Order
- [x] Search Past Orders
- [x] Search Historical Orders within 48 Hours
- [x] Search Match Results
- [x] Get Current Fee Rate Applied to The User

#### Conditional Order
- [ ] Place a conditional order
- [ ] Cancel conditional orders (before triggering)
- [x] Query open conditional orders (before triggering)
- [x] Query conditional order history
- [x] Query a specific conditional order

#### Margin Loan (Cross/Isolated)
- [ ] Repay Margin Loan（Cross/Isolated ）
- [ ] Transfer Asset from Spot Trading Account to Isolated Margin Account（Isolated)
- [ ] Transfer Asset from Isolated Margin Account to Spot Trading Account（Isolated)
- [x] Get Loan Interest Rate and Quota（Isolated）
- [ ] Request a Margin Loan（Isolated）
- [ ] Repay Margin Loan（Isolated）
- [x] Search Past Margin Orders（Isolated）
- [x] Get the Balance of the Margin Loan Account（Isolated）
- [ ] Transfer Asset from Spot Trading Account to Cross Margin Account（Cross）
- [ ] Transfer Asset from Cross Margin Account to Spot Trading Account（Cross）
- [x] Get Loan Interest Rate and Quota（Cross）
- [ ] Request a Margin Loan（Cross）
- [ ] Repay Margin Loan（Cross）
- [x] Search Past Margin Orders（Cross）
- [x] Get the Balance of the Margin Loan Account（Cross）
- [x] Repayment Record Reference

#### Margin Loan C2C
- [ ] Place a lending/borrowing offer
- [ ] Cancel a lending/borrowing offer
- [ ] Cancel all lending/borrowing offers
- [x] Query lending/borrow offers
- [x] Query a lending/borrowing offer
- [x] Query lending/borrowing transactions
- [ ] Repay a borrowing offer
- [x] Query C2C repayments
- [ ] Transfer asset
- [x] Query C2C account balance

#### Stable Coin Exchange
- [x] Get Exchange Rate
- [x] Exchange Stable Coin

#### ETP
- [x] Get reference data of ETP
- [ ] ETP Creation
- [ ] ETP Redemption
- [x] Get ETP Creation & Redemption History
- [x] Get Specific ETP Creation or Redemption Record
- [x] Get Position Rebalance History
- [ ] Submit Cancel for and ETP Order
- [ ] Batch Cancellation for ETP Orders
- [x] Get Holding Limit of  Leveraged ETP