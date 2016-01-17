# __author__ = 'Nicholas'
# from flask import Flask, jsonify, render_template, request
# app = Flask(__name__)
# import codecs
# import json
# import sys
# import codecs
# sys.stdout = codecs.getwriter('utf8')(sys.stdout)
# from TwitterSearch import *
# try:
#     tso = TwitterSearchOrder() # create a TwitterSearchOrder object
#     tso.set_keywords(['I hate']) # let's define all words we would like to have a look for
#     tso.set_language('en') # we want to see German tweets only
#     tso.set_include_entities(False) # and don't give us all those entity information
#
#     # it's about time to create a TwitterSearch object with our secret tokens
#     ts = TwitterSearch(
#         consumer_key = 'yXhNsDUxeJ4zyGjSMba9ovnca',
#         consumer_secret = 'rVNSBiC8PF4M07DKrF832VVyFQyCcRMPqB9MLPTDTsRLfqSvwu',
#         access_token = '98960898-Udrqkng1nxTbRTRaAwIr6kAmRGA7jYznMB90P0bzB',
#         access_token_secret = 'fxYrGoXKoLqqD3vMHDTERxBL0dG2564RoosrypBh7arEu'
#      )
#
#      # this is where the fun actually starts :)
#     f = codecs.open("jsonoutput.json", mode='w', encoding="utf-8", errors='strict', buffering=1)
#     #for tweet in ts.search_tweets_iterable(tso):
#     #    info = ({'id' : tweet['id' ] , 'user' : tweet['user']['screen_name'] , 'text' : tweet['text']})
#     #    print tweet
#     #    json.dumps(info, indent = 1, ensure_ascii=False)
#     #    print(json.dumps(info))
#     #    write_this = unicode( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
#     #    f.write(write_this + '\n')
#
#
#
#
#     def get_tweets():
#         tweets = []
#         for tweet in ts.search_tweets_iterable(tso):
#             info = ({'id' : tweet['id' ] , 'user' : tweet['user']['screen_name'] , 'text' : tweet['text']})
#         #    return jsonify(id=tweet['id'] , user=tweet['user']['screen_name'] , text=tweet['text'])
#         #    print tweet
#             json.dumps(info, indent = 1, ensure_ascii=False)
#         #    tweets.append(info)
#         #return jsonify(tweets)
#
# except TwitterSearchException as e: # take care of all those ugly errors if there are some
#     print(e)
#
# get_tweets()