import json
import typing
import strawberry
from datetime import datetime

from src.wrapper.twitter import TwitterWrapper


def get_timeline():
    start = datetime.now()
    tweet_wrapper = TwitterWrapper()

    out_location = "data/demo_tweets2.jsonl"
    with open(out_location, 'w') as f:
        for tweet in  tweet_wrapper.home_timeline():
            print(json.dumps(tweet._json), file=f)
        end = datetime.now()
    return DataOutput(
        status="completed",
        location=out_location,
        start=datetime.isoformat(start),
        end=datetime.isoformat(end)
    )

@strawberry.type
class DataOutput:
    status: str
    location: str
    start: str
    end: str

@strawberry.type
class Query:
    timeline: DataOutput = strawberry.field(resolver=get_timeline)

schema = strawberry.Schema(query=Query)