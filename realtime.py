import urllib3  # works fine with Python 2.7.9 (not 3.4.+)
import json
import time

def fetchPreMarket(symbol, exchange):
    http = urllib3.PoolManager()
    link = "http://finance.google.com/finance/info?client=ig&q="
    url = link+"%s:%s" % (exchange, symbol)
    u = http.request('GET',url)
    content = u.read()
    
    print ("hello, world!")
    
    data = json.loads(content[3:])
    info = data[0]
    t = str(info["elt"])    # time stamp
    l = float(info["l"])    # close price (previous trading day)
    p = float(info["el"])   # stock price in pre-market (after-hours)
    return (t,l,p)

	
p0 = 0
while True:
    t, l, p = fetchPreMarket("AAPL","NASDAQ")
    if(p!=p0):
        p0 = p
        print("%s\t%.2f\t%.2f\t%+.2f\t%+.2f%%" % (t, l, p, p-l,
                                                 (p/l-1)*100.))
    time.sleep(60)
