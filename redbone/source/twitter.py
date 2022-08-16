import tweepy
import yaml


class TwitterWrapper:
    def __init__(self):
        self.authenticate()

    def authenticate(self):
        self.auth = self.get_authentication()
        self.api = tweepy.API(self.auth)

    @staticmethod
    def get_authentication():
        secrets = yaml.safe_load(open("secrets/twitter.yml", "r"))

        auth = tweepy.OAuth1UserHandler(
            secrets["consumer_key"],
            secrets["consumer_secret"],
            secrets["access_token"],
            secrets["access_token_secret"],
        )

        return auth

    def home_timeline(self):
        return self.api.home_timeline()

    def search(self, kwargs):
        return self.api.search_tweets(**kwargs)


class TwitterStreamClient(tweepy.StreamingClient):
    def __init__(self, output, rules):
        self.out_location = output
        secrets = yaml.safe_load(open("secrets/twitter.yml", "r"))
        super().__init__(secrets["bearer_token"])
        if rules:
            self.add_rules(rules)

    def add_rules(self, rules):
        # TODO: simplify how rules are generated between this and schema
        tweepy_rules = [
            tweepy.StreamRule(value=rule.get("value"), tag=rule.get("tag"))
            for rule in rules
        ]
        super().add_rules(tweepy_rules)

    def on_tweet(self, tweet):
        with open(self.out_location, "a") as f:
            print(tweet.data, file=f)

    def cleanup_rules(self):
        old_rules = self.get_rules()
        if old_rules:
            old_rules = old_rules.data
        for rule in old_rules:
            self.delete_rules([rule.id])
