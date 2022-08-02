from typing import Any, Dict
import tweepy
import yaml


class TwitterWrapper():

    def __init__(self):
        self.authenticate()

    def authenticate(self):
        self.auth = self.get_authentication()
        self.api = tweepy.API(self.auth)

    @staticmethod
    def get_authentication():
        secrets = yaml.safe_load(open("secrets/twitter.yml",'r'))

        auth = tweepy.OAuth1UserHandler(
        secrets["consumer_key"], 
        secrets["consumer_secret"], 
        secrets["access_token"], 
        secrets["access_token_secret"],
        )

        return auth

    def home_timeline(self):
        return self.api.home_timeline()

if __name__ == '__main__':
    wrapper = TwitterWrapper()