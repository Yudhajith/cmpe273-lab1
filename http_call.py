import requests

r = requests.get('https://webhook.site/e8deb2cb-9e76-4703-aa29-32d2b5c2af37')
s = requests.get('https://webhook.site/e8deb2cb-9e76-4703-aa29-32d2b5c2af37')
t = requests.get('https://webhook.site/e8deb2cb-9e76-4703-aa29-32d2b5c2af37')

print (r.headers['Date'])
print (s.headers['Date'])
print (t.headers['Date'])