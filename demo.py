import tweepy
import yaml
import json

secrets = yaml.safe_load(open("secrets/twitter.yml",'r'))

auth = tweepy.OAuth1UserHandler(
   secrets["consumer_key"], 
   secrets["consumer_secret"], 
   secrets["access_token"], 
   secrets["access_token_secret"],
)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

with open("data/demo_tweets.jsonl", 'w') as f:
    for tweet in public_tweets:
        print(json.dumps(tweet._json), file=f)