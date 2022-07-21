import json

from redbone.wrapper.twitter import TwitterWrapper

tweet_wrapper = TwitterWrapper()

# TODO on interface
public_tweets = tweet_wrapper.home_timeline()

with open("data/demo_tweets2.jsonl", 'w') as f:
    for tweet in public_tweets:
        print(json.dumps(tweet._json), file=f)