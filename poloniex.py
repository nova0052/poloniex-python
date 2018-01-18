import requests
import time
import json
import hmac,hashlib
import urllib

#Public API methods

def returnTicker():
    ticker = requests.get('https://poloniex.com/public?command=returnTicker')
    return json.loads(ticker.text)

def return24Volume():
    vol24 = requests.get('https://poloniex.com/public?command=return24hVolume')
    return json.loads(vol24.text)

def returnOrderBook(air, depth):
    payload = {'depth': depth, 'currencyPair': pair}
    book = requests.get('https://poloniex.com/public?command=returnOrderBook', params = payload)
    return json.loads(book.text)

def returnTradeHistory(pair, start, end):
    payload = {'end': end, 'start': start, 'currencyPair': pair}
    trades = requests.get('https://poloniex.com/public?command=returnTradeHistory', params = payload)
    return json.loads(trades.text)

def returnChartData(pair, start, end, period):
    payload = {'period': period, 'end': end, 'start': start, 'currencyPair': pair}
    chart = requests.get('https://poloniex.com/public?command=returnChartData', params = payload)
    return json.loads(chart.text)

def returnCurrencies():
    currencies = requests.get('https://poloniex.com/public?command=returnCurrencies')
    return json.loads(currencies.text)

def returnLoanOrders(currency):
    payload = {'currency': currency}
    loans = requests.get('https://poloniex.com/public?command=returnLoanOrders', params = payload)
    return json.loads(loans.text)

#Trading API methods

class account:
    def __init__(self, APIKey, Secret):
        self.APIKey = APIKey
        self.Secret = Secret

    def apiCall(self, body):
        body['nonce'] = int(time.time() * 1000)
        data = urllib.urlencode(body)
        sign = hmac.new(self.Secret, data, hashlib.sha512).hexdigest()
        headers = {"Sign": sign, "Key": self.APIKey}
        call = requests.post('https://poloniex.com/tradingApi', headers=headers, data=body)
        return call.text

    def returnBalances(self):
        body = {"command": "returnBalances"}
        balances = json.loads(self.apiCall(body))
        return balances

    def returnCompleteBalances(self):
        body = {"command": "returnCompleteBalances"}
        balances = json.loads(self.apiCall(body))
        return balances

    def returnDepositAddresses(self):
        body = {"command": "returnDepositAddresses"}
        addresses = json.loads(self.apiCall(body))
        return addresses

    def generateNewAddress(self, currrency):
        body = {"command": "generateNewAddress", "currency": currency}
        address = json.loads(self.apiCall(body))
        return address

    def returnDepositsWithdrawals(self, start, end):
        body = {'command': 'returnDepositsWithdrawals', 'start': start, 'end': end}
        depswits = json.loads(self.apiCall(body))
        return depswits

    def returnOpenOrders(self, currencyPair):
        body = {'command': 'returnOpenOrders', 'currencyPair': currencyPair}
        orders = json.loads(self.apiCall(body))
        return orders

    def returnTradeHistory(self, currencyPair, start=None, end=None):
        body = {'command': 'returnTradeHistory', 'currencyPair': currencyPair, 'start': start, 'end': end}
        trades = json.loads(self.apiCall(body))
        return trades

    def returnOrderTrades(self, orderNumber):
        body = {'command': 'returnOrderTrades', 'orderNumber': orderNumber}
        trades = json.loads(self.apiCall(body))
        return trades

    def buy(self, currencyPair, rate, amount, fillOrKill=0, immediateOrCancel=0, postOnly=0):
        body = {'command': 'buy', 'currencyPair': currencyPair,  'rate': rate, 'amount': amount, 'fillOrKill': fillOrKill, 'immediateOrCancel': immediateOrCancel, 'postOnly': postOnly}
        order = json.loads(self.apiCall(body))
        return order

    def sell(self, currencyPair, rate, amount, fillOrKill=0, immediateOrCancel=0, postOnly=0):
        body = {'command': 'sell', 'currencyPair': currencyPair,  'rate': rate, 'amount': amount, 'fillOrKill': fillOrKill, 'immediateOrCancel': immediateOrCancel, 'postOnly': postOnly}
        order = json.loads(self.apiCall(body))
        return order

    def cancelOrder(self, orderNumber):
        body = {'command': 'cancelOrder', 'orderNumber': orderNumber}
        cancel = json.loads(self.apiCall(body))
        return cancel

    def moveOrder(self, orderNumber, rate, amount=None, immediateOrCancel=None, postOnly=None):
        body = {'command': 'moveOrder', 'rate': rate, 'amount': amount, 'immediateOrCancel': immediateOrCancel, 'postOnly': postOnly}
        order = json.loads(self.apiCall(body))
        return order

    def withdraw(self, currency, amount, address, paymentId=None):
        body = {'command': 'withdraw', 'currency': currency, 'amount': amount, 'address': address, 'paymentId': paymentId}
        wit = json.loads(self.apiCall(body))
        return wit

    def returnFeeinfo(self):
        body = {'command': returnFeeinfo}
        fees = json.loads(self.apiCall(body))
        return fees

    def returnAvailableAccountBalances(self, account=None):
        body= {'command': 'returnAvailableAccountBalances', 'account': account}
        balances = json.loads(self.apiCall(body))
        return balances

    def returnTradableBalances(self):
        body = {'command': 'returnTradableBalances'}
        balances = json.loads(self.apiCall(body))
        return balances

    def transferBalance(self, currency, amount, fromAccount, toAccount):
        body = {'command': 'transferBalance', 'currency': currency, 'amount': amount, 'fromAccount': fromAccount, 'toAccount': toAccount}
        transfer = json.loads(self.apiCall(body))
        return transfer

    def returnMarginAccountSummary(self):
        body = {'command': 'returnMarginAccountSummary'}
        summary = json.loads(self.apiCall(body))
        return summary

    def marginBuy(self, currencyPair, rate, amount, lendingRate=None):
        body = {'command': 'marginBuy', 'currencyPair': currencyPair, 'rate': rate, 'amount': amount, 'lendingRate': lendingRate}
        marginOrder = json.loads(self.apiCall(body))
        return marginOrder

    def marginSell(self, currencyPair, rate, amount, lendingRate=None):
        body = {'command': 'marginSell', 'currencyPair': currencyPair, 'rate': rate, 'amount': amount, 'lendingRate': lendingRate}
        marginOrder = json.loads(self.apiCall(body))
        return marginOrder

    def getMarginPosition(self, currencyPair):
        body = {'command': getMarginPosition, 'currencyPair': currencyPair}
        position = json.loads(self.apiCall(body))
        return position

    def closeMarginPosition(self, currencyPair):
        body = {'command': closeMarginPosition, 'currencyPair': currencyPair}
        close = json.loads(self.apiCall(body))
        return close

    def createLoanOffer(self, currency, amount, duration, autoRenew, lendingRate):
        body = {'command': 'createLoanOffer', 'amount': amount, 'duration': duration, 'autoRenew': autoRenew, 'lendingRate': lendingRate}
        create = json.loads(self.apiCall(body))
        return create

    def cancelLoanOffer(self, orderNumber):
        body = {'command': 'cancelLoanOffer', 'orderNumber': orderNumber}
        cancel = json.loads(self.apiCall(body))
        return cancel

    def returnOpenLoanOffers(self):
        body = {'command': 'returnOpenLoanOffers'}
        offers = json.loads(self.apiCall(body))
        return offers

    def returnActiveLoans(self):
        body = {'command': 'returnActiveLoans'}
        loans = json.loads(self.apiCall(body))
        return loans

    def returnLendingHistory(self, start, end, limit=None):
        body = {'command': 'returnLendingHistory', 'start': start, 'end': end, 'limit': limit}
        history = json.loads(self.apiCall(body))
        return history

    def toggleAutoRenew(self, orderNumber):
        body = {'command': toggleAutoRenew, 'orderNumber': orderNumber}
        toggle = json.loads(self.apiCall(body))
        return toggle
