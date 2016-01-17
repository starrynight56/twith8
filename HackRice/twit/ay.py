from flask import Flask, render_template
#from flask import render_template
import search
app = Flask(__name__)
tweets = search.get_tweets(3)
tweet_text_1 = tweets[0]["text"]
tweet_text_2 = tweets[1]["text"]
tweet_text_3 = tweets[2]["text"]
@app.route('/')
def hello_world():
    return render_template("twitter.html", tweet1 = tweet_text_1, tweet2 = tweet_text_2, tweet3 = tweet_text_3)
if __name__ == '__main__':
    app.run()

#find a way to present twitter .html file in ay.py. and then
