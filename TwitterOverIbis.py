from twitterscraper import query_tweets
import datetime as dt
import ibis
import time
m = ibis.IBISMaster("/dev/ttyUSB0", debug=True)

var = 1
while var == 1:

    for tweet in query_tweets ("#35c3", 1,begindate=dt.date.today(),enddate = dt.date.today() + dt.timedelta(days=1))[:5]:
        for x in range(0, len(tweet.text)-1):
            #print(tweet.text.upper()[x:x + 24]) 
            m.DS009(tweet.text.upper()[x:x + 24])
            time.sleep(0.1)


