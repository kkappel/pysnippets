#!/usr/bin/python

import ystockquote
from pprint import pprint

GEMKTO = ['A0S9GB.DE', '^GDAXI']
# 'A0H08C.DE'

for sym in GEMKTO:
   print sym
   a = ystockquote.get_historical_prices(sym, '2014-10-01', '2014-10-02')
   pprint(a)

# pprint(ystockquote.get_historical_prices('DAI.DE', '2014-10-01', '2014-10-31'))
# pprint(ystockquote.get_historical_prices('DAX', '2014-10-01', '2014-10-31'))
# pprint(ystockquote.get_all('GOOG'))
# print(ystockquote.get_price_book('GOOG'))
# print(ystockquote.get_bid_realtime('GOOG'))


# get symbol

query = 'BMW'
url = 'http://d.yimg.com/autoc.finance.yahoo.com/autoc?query=%s&callback=YAHOO.Finance.SymbolSuggest.ssCallback' % (query)

#j = urlopen(url)

#print j
