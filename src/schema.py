import json
from typing import Dict, Any, List, Optional
import random
import strawberry
import string
import time

from pathlib import Path
from datetime import datetime

from src.wrapper.twitter import TwitterWrapper, TwitterStreamClient


@strawberry.type
class FilterRule:
    rule: str
    tag: str


@strawberry.type
class DataOutput:
    status: str
    out_location: str
    start: str
    end: str


def generate_out_location(location_id: str):
    DATA_DIR = Path("data/")
    return (
        DATA_DIR
        / f"{location_id}_{''.join(random.choices(string.ascii_uppercase + string.digits, k=10))}.jsonl"
    )


def get_timeline():
    tweet_wrapper = TwitterWrapper()

    out_location = generate_out_location("timeline")
    try:
        with open(out_location, "w") as f:
            start = datetime.now()
            for tweet in tweet_wrapper.home_timeline():
                print(json.dumps(tweet._json), file=f)
            end = datetime.now()
        status = "completed"
    except Exception as e:
        start = datetime.now()
        status = "failure: {}".format(str(e))
        end = start
    return DataOutput(
        status=status,
        out_location=out_location,
        start=datetime.isoformat(start),
        end=datetime.isoformat(end),
    )


def run_stream(duration: int, rules: Optional[List[str]]):
    filter_rules = [{"value": rule, "tag": i} for i, rule in enumerate(rules)]
    start = datetime.now()
    out_location = generate_out_location("stream")
    try:
        stream = TwitterStreamClient(output=out_location, rules=filter_rules)
        stream.filter(
            threaded=True,
            tweet_fields=["public_metrics", "created_at", "author_id", "text"],
            user_fields=["username", "created_at", "public_metrics"],
            media_fields=["public_metrics", "media_key"],
            expansions=["author_id", "attachments.media_keys"],
        )
        time.sleep(duration)
        stream.disconnect()
        stream.cleanup_rules()
        status = "completed"
        end = datetime.now()
    except Exception as e:
        start = datetime.now()
        status = "failure: {}".format(str(e))
        end = start
    return DataOutput(
        status=status,
        out_location=out_location,
        start=datetime.isoformat(start),
        end=datetime.isoformat(end),
    )


@strawberry.type
class Query:
    timeline: DataOutput = strawberry.field(resolver=get_timeline)
    stream: DataOutput = strawberry.field(resolver=run_stream)


schema = strawberry.Schema(query=Query)
