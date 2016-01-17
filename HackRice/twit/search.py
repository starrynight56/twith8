__author__ = 'Nicholas'
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)
import sys
import codecs
from TwitterSearch import *
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['I hate']) # search for "I hate"
    tso.set_language('en') # English only
    tso.set_include_entities(False) # don't get too much information

    ts = TwitterSearch(
        consumer_key = 'yXhNsDUxeJ4zyGjSMba9ovnca',
        consumer_secret = 'rVNSBiC8PF4M07DKrF832VVyFQyCcRMPqB9MLPTDTsRLfqSvwu',
        access_token = '98960898-Udrqkng1nxTbRTRaAwIr6kAmRGA7jYznMB90P0bzB',
        access_token_secret = 'fxYrGoXKoLqqD3vMHDTERxBL0dG2564RoosrypBh7arEu'
     )

    def get_tweets(amount):
        tweets = []
        counter = 0
        for tweet in ts.search_tweets_iterable(tso):
            if (counter < amount):
                info = ({'id' : tweet['id' ] , 'user' : tweet['user']['screen_name'] , 'text' : tweet['text']})
                tweets.append(info)
                counter += 1
            else:
                break
        return tweets
except TwitterSearchException as e:
    print(e)
