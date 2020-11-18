from kiteconnect import KiteConnect

apiKey = 'your key'
apiSecret = 'your key'

requestToken = 'your key'

accessToken = 'your key'

kite = KiteConnect(api_key = apiKey)


# data = kite.generate_session(requestToken,api_secret=apiSecret)
# print(data)


kite.set_access_token(accessToken)

# print(kite.orders)

"""
url to generate request token:
https://kite.trade/connect/login?api_key=dummy text
"""




