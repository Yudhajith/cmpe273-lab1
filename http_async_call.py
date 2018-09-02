from requests_futures.sessions import FuturesSession

session = FuturesSession()

future_one = session.get('https://webhook.site/e8deb2cb-9e76-4703-aa29-32d2b5c2af37')
future_two = session.get('https://webhook.site/e8deb2cb-9e76-4703-aa29-32d2b5c2af37')
future_three = session.get('https://webhook.site/e8deb2cb-9e76-4703-aa29-32d2b5c2af37')

response_one = future_one.result()
response_two = future_two.result()
response_three = future_three.result()


print (response_one.headers['Date'])
print (response_two.headers['Date'])
print (response_three.headers['Date'])
