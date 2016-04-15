# DataAnalysis Homework1 M10323003 HenryLee
# Twitter Data => json,log.csv
import twitter
import urlparse
import logging
import time
import sys
from datetime import datetime
from IO_json import *
#from pprint import pprint as pp

class TwitterCrawler(object):
    # TwitterCrawler class allows the Connection to Twitter via
    # OAuth once you have registered with twitter and receive
    # the necessary credentials

    # initialze and get the twitter credentials
    def __init__(self):
        print ' start __init__()'
        consumer_key = 'YwVJQ6C4yVONnAiFDhn6LNkAw'
        consumer_secret = 'cYtkFMOpLrRtBEudQPfFfdvUrvb7fvCEJ9R3NLwTGyk0StgM2r'
        access_token = '2651066418-CJ5AYIGhfp9IbycQxUUaBQa64YBpF7pRjLz7s9w'
        access_secret = 'RosOEC6HPolnsXwye6Drfrry8GWsRfcur4xCo7QfogXl0'
        
        self.consumer_key=consumer_key
        self.consumer_secret=consumer_secret
        self.access_token=access_token
        self.access_secret=access_secret
        
        self.retries=3
        
        # authenticate credentials with twitter using oauth
        self.auth = twitter.oauth.OAuth(access_token, access_secret,
                                        consumer_key, consumer_secret)
        # create registered Twitter api
        self.api = twitter.Twitter(auth=self.auth)
        
        # logger initialisation
        appName = 'henrylee_crawler'
        self.logger=logging.getLogger(appName)
        
        # create console handler and set level to debug
        logPath='log'
        fileName= appName
        fileHandler = logging.FileHandler("{0}/{1}.log".format(logPath,fileName))
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        fileHandler.setFormatter(formatter)
        self.logger.addHandler(fileHandler)
        self.logger.setLevel(logging.DEBUG)
        
        # Save to Json file initialisation
        jsonFpath ='data/json'
        jsonFname ='twitterdata16413001'
        self.jsonSaver = IO_json(jsonFpath, jsonFname)

        # save to MongoDB initialisation
        # self.mongoSaver = IO.mongo(db='twtr01_db', coll='twtr01_coll')              
        print 'end __init__()'
         
    # search twitter with query q (ie: "apacheSpark") and max.result
    def searchTwitter(self, q, max_res=10, **kwargs):
            print 'start searchTwitter()'
            search_results = self.api.search.tweets(q=q,count=10,**kwargs)
            statuses=search_results['statuses']
            max_results = min(1000,max_res)
        
            while True:
                try:
                    next_results = search_results['search_metadata']['next_results']
                    #self.logger.info('info in searchTwitter-next_results: %s'% next_result[1:])
                except KeyError as e:
                #self.logger.error('error in searchTwitter: %s', %(e))
                    break
            
                next_results = urlparse.parse_qsl(next_results[1:])
                # next_results=urllib.parse.parse_qsl(next_results[1:])
                #self.logger.info('info in searchTwitter-next_results[max_id]:',next_results[0:])
                kwargs = dict(next_results)
                log_string = 'info in searchTwitter-next_results[max_id]:%s'% kwargs['max_id']
                print log_string
                self.logger.info(log_string)
                print 'searching Tweets'
                search_results=self.api.search.tweets(**kwargs)
                statuses+=search_results['statuses']
                self.saveTweets(search_results['statuses'])
            
                #if len(statuses) > max_results:
                #    self.logger.info('info in searchTwitter-got %i tweets - max %i' %(len(statuses), max_results))
                #    break
            
            #return statuses
            print 'end searchTwitter()'
        
    def saveTweets(self, statuses):
        # Saving to Json file
            print 'start saveTweets()'
            self.jsonSaver.save(statuses)
            
            print 'end saveTweets()'              
            # Saving to MongoDB
            # for s in statuses:
            #    self.mongoSaver.save(s)
       
     # parse tweets as it's collected to extract id, creation #date, user id, tweet text
    def parseTweets(self, statuses):
            print 'start parseTweets()'
            return [ (status['id'],
                      status['created_at'],
                      status['user']['id'],
                      status['user']['name'],
                      status['text'],
                      url['expanded_url'])
                          for status in statuses
                              for url in status['entities']['urls'] ]
    
     # make a twitter api call whilst managing rate limit and errors
    def getTweets(self,q,max_res=10):
        print 'start getTweets()'
        
        def handleError(e, wait_period=2,sleep_when_rate_limited=True):
              
               print 'start handleError()'
               if wait_period > 3600 : #seconds
                   #self.logger.error('Too many retries in getTweets: %s', %(e))
                   raise e
                   
               if e.e.code == 401:
                   #self.logger.error('error 401* not authorised* in getTweets: %s', %(e))
                   print '401'
                   return None
               elif e.e.code == 404:
                   #self.logger.error('error 404 * not found * in getTweets: %s', %(e))
                   print '404'
                   return None
               elif e.e.code == 429:
                   print '429'
                   #self.logger.error('error 429 * api rate limit exceeded * in getTweets: %s',%(e))
                   if sleep_when_rate_limited:
                        #self.logger.error('error 429 * retrying in 15 minutes * in getTweets: %s',%(e))
                        sys.stderr.flush()
                        time.sleep(60*15+5)
                        #self.logger.info('error 429 * retring now * in getTweets: %s',%(e))
                        return 2
                   else:
                        raise e # caller must handle the rate limiting issus
               elif e.e.code in (500,502,503,504):
                    print '500 502 503 504'
                    self.logger.info('encountered %i error. retrying in %i seconds' %(e.e.code,wait_period))
                    time.sleep(wait_period)
                    wait_period*=1.5
                    return wait_period
               else:
                    #self.logger.error('exit - aborting - %s', %(e))
                    raise e
                    
        while True:
               wait_period=2
               try:
                    self.searchTwitter(q,max_res=1000)
               except twitter.api.TwitterHTTPError as e:
                    print 'Error happened'
                    print e
                    error_count =0
                    wait_period = handleError(e, wait_period)
                 #if wait_period is None:
                 #    return

t=TwitterCrawler()
q="a"
tsearch=t.getTweets(q)
pp(tsearch[1])
                     
            
                       
                            
                             
          

