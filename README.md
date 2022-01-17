<h1 align="center"> HUOBIPY </h1>
<div align="center">
<a href="https://www.huobi.com/"><img src="https://img.shields.io/static/v1?label=&labelColor=505050&message=Huobi&color=%230076D6&style=flat&logo=google-chrome&logoColor=%230076D6" alt="website"/></a>
<a href="https://huobiapi.github.io/docs"><img src="https://img.shields.io/static/v1?label=&labelColor=505050&message=Huobi API DOCS&color=%230076D6&style=flat&logo=google-chrome&logoColor=%230076D6" alt="website"/></a>

</div>
<div align="center">
<i>This packages intents to be an idiomatic PythonApi wrapper for Huobi</i>

<a href="https://github.com/surister/huobi_python/stargazers"><img src="https://img.shields.io/github/stars/surister/huobi_python" alt="Stars Badge"/></a>
</div>

### Contents:
  - [Current Services](#Current-Services)
  - [REST API Endpoints](#REST-API-endpoints)
  - [WEBSOCKET API Endpoints](#WEBSOCKET-API-Endpoints)

### Tutorial:
  - [How to install](#How-To-Install)
  - [Examples](#Examples)

### Project Info:
  - [Getters in-depth](#Getters-In-Depth)
    - [Reference Data](#Reference-Data-Getters)
  - [Post in-depth](#Post-In-Depth)
  - [Planned Features](#Planned-Features)
  - [Changelog](#Changelog)


## Current Services
- REST API ❌
- WEBSOCKET API ❌

## REST API Endpoints
- Reference Data ✔️

- Market Data ✔️

- Account ❌

- Wallet ❌

- Sub-User Management ❌

- Trading ❌

- Conditional Orders ❌

- Margin Loan ❌

- Stable Coin Exchange ❌


## WEBSOCKET API Endpoints
- Market Data ❌
- Account Data ❌
- Orders ❌

## How To Install

## Examples

### *Prerequisites*
- You need a Secret Key and Access Key to the API provided by [Huobi](https://www.huobi.com/en-us/apikey/). Please do not publish your own keys and remember that once the key is created, the secret key will not be able to be consulted in the future, so save it.
- If you are going to play with the sub users endpoints, check that you have, at least, one created. Click [here](https://account.huobi.com/en-us/subaccount/management/) to create one
- To get started, you must have a HuobiClient instance with your **Secret key and Access Key**.
```py
from huobi.rest.client import HuobiClient

client = HuobiClient(access_key= 'Your_Access_Key', secret_key='Your_Secret_Key')
```

### Example 1 (Get Last Day Summary of Bitcoin in USDT)
```py
req = client.get_last_day_market_summary(currency='btcusdt')
```
```py
# Output
{"ch":"market.btcusdt.detail","status":"ok","ts":1642083312575,"tick":{"id":293383444638,"low":43320.23,"high":44355.58,"open":43754.74,"close":43997.15,"vol":2.6205615363949648E8,"amount":5988.949391700904,"version":293383444638,"count":523165}}
```
### Example 2 (Get your own UserID)
```py
req = client.get_uid()
```
```py
# Output
{"code":200,"data":'Here will appear your UID',"ok":true}
```
### Example 3 (Get most recent trade from Ethereum to USDT)
```py
req = client.get_most_recent_trades(currency='ethusdt', size=1)
```
```py
# Output
{"ch":"market.ethusdt.trade.detail","status":"ok","ts":1642083884643,"data":[{"id":144000086587,"ts":1642083884611,"data":[{"id":144000086587454187344074844,"ts":1642083884611,"trade-id":102351374009,"amount":0.0711,"price":3385.64,"direction":"buy"}]}]}
```





## Getters In-Depth

### Reference Data Getters:

## Post In-Depth

## Planned Features
* Currency Enum
* Candles Graphic Draw

## Changelog

#### 2022-01-07 - 2022-01-09
* Add basic project structure
* Add working API authentication
* Add endpoint/request scheme
* Add all market endpoints
* Add some account & user endpoints
* Add flake8 testing
#### 2022-1-10 - 2022-01-17
* Add reference data endpoints
* Add wallet endpoints (GETS)
* Add conditional orders endpoint (GETS)
* Add trading endpoints (GETS)