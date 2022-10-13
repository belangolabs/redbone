from pathlib import Path
from typing import Any, Dict, List

import tweepy
import yaml

SECRETS_LOCATION = "secrets/twitter.yml"


class TwitterWrapper:
    """
    Class for static/non-streaming Twitter pulls.
    """

    def __init__(self):
        self.authenticate()

    def authenticate(self):
        """
        Authenticate to API.
        """
        self.auth = self.get_authentication()
        self.api = tweepy.API(self.auth)

    @staticmethod
    def get_authentication():
        """
        Load Twitter authentication keys.
        """
        secrets = yaml.safe_load(open(SECRETS_LOCATION, "r", encoding="utf-8"))

        auth = tweepy.OAuth1UserHandler(
            secrets["consumer_key"],
            secrets["consumer_secret"],
            secrets["access_token"],
            secrets["access_token_secret"],
        )

        return auth

    def home_timeline(self):
        """
        Pull most recent timeline posts.
        """
        return self.api.home_timeline()

    def search(self, kwargs):
        """
        Pull tweets using Twitter search.
        """
        return self.api.search_tweets(**kwargs)


class TwitterStreamClient(tweepy.StreamingClient):
    """
    Wrapper around tweepy.StreamingClient
    """

    def __init__(self, output: Path, rules: List[Dict[str, Any]]):
        self.out_location = output
        secrets = yaml.safe_load(open(SECRETS_LOCATION, "r", encoding="utf-8"))
        super().__init__(secrets["bearer_token"])
        if rules:
            self.add_rules(rules)

    def add_rules(self, rules):
        """
        Add filtering rules to stream.
        > TODO: simplify how rules are generated between this and schema
        """
        tweepy_rules = [
            tweepy.StreamRule(value=rule.get("value"), tag=rule.get("tag"))
            for rule in rules
        ]
        super().add_rules(tweepy_rules)

    def on_tweet(self, tweet):
        """
        Upon appearance of matching tweet, write to output location.
        """
        with open(self.out_location, "a", encoding="utf-8") as f:
            print(tweet.data, file=f)

    def cleanup_rules(self):
        """
        StreamRules live on the client indefinitely. To use the client for
        separate stream pulls, we need to remove the previous pull's rules.

        TODO: Note that this approach
        """
        old_rules = self.get_rules()
        if old_rules:
            old_rules = old_rules.data
        for rule in old_rules:
            self.delete_rules([rule.id])
