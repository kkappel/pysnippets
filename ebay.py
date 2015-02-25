#!/usr/bin/python
#
# (c) 2014 by Klaus Kappel

from ebaysdk.finding import Connection as Finding
api = Finding(domain='svcs.sandbox.ebay.com', appid="NovaLisa-352a-4d18-bade-3037954d9078")
response = api.execute('findItemsAdvanced', {'keywords': 'Nikon'})
print(response.dict())
